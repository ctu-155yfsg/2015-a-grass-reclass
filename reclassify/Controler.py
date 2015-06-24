#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Controler class
"""

#-----------------------------------------------------------------------------------------
#Import
try:
    #wxPython
    import wx
    #python std library
    import sys
    import os
    import re
    #GRASS modules and packages
    from core.gcmd import RunCommand
    from grass.script import parser, run_command
    import atexit
    from gui_core.gselect import Select
    #our modules and packages
    from OurApp import OurApp
    from MainFrame import MainFrame
    from Layout import *

except ImportError as err:
    print(u"ImportError: {}".format(err))
    sys.exit("-1")
#-----------------------------------------------------------------------------------------
class Controler:
    """
    Specifies widgets behaviour.
    All program logic is there.
    Rest is just a layout. (Except Select class used in InputOutputPanel class)
    """
    #-----------------------------------------------------------------------------------------

    def __init__(self, OurAppObject):

        self.app = OurAppObject

        #BINDINGS
        self.app.mainFrame.controlPanel.okButton.Bind(wx.EVT_BUTTON, self.__okButtonClicked)
        self.app.mainFrame.controlPanel.cancelButton.Bind(wx.EVT_BUTTON, self.__cancelButtonClicked)

        self.app.mainFrame.reclassifyPanel.addButton.Bind(wx.EVT_BUTTON, self.__addButtonClicked)
        self.app.mainFrame.reclassifyPanel.deleteButton.Bind(wx.EVT_BUTTON, self.__deleteButtonClicked)
        self.app.mainFrame.reclassifyPanel.previewButton.Bind(wx.EVT_BUTTON, self.__previewButtonClicked)

        self.app.mainFrame.inputOutputPanel.input.Bind(wx.EVT_TEXT, self.__onInputRasterSelect)


    #-----------------------------------------------------------------------------------------


    def __addButtonClicked(self, event):
        """
        Append one row to the reclassify table.
        :param event:
        :return: void
        """
        self.app.mainFrame.reclassifyPanel.table.AppendRows(numRows=1)
        rowsNumber = self.app.mainFrame.reclassifyPanel.table.GetNumberRows()
        self.app.mainFrame.reclassifyPanel.table.SetCellEditor(rowsNumber - 1, 3, wx.grid.GridCellTextEditor())
    #-----------------------------------------------------------------------------------------


    def __deleteButtonClicked(self, event):
        """
        Removes selected rows from the reclassify table.
        :param event:
        :return: void
        """
        selectedRows = self.app.mainFrame.reclassifyPanel.table.GetSelectedRows()
        selectedRows = sorted(selectedRows, reverse=True)

        for I in selectedRows:
            self.app.mainFrame.reclassifyPanel.table.DeleteRows(pos=I, numRows=1)

    #-----------------------------------------------------------------------------------------


    def __getRasterMinMax(self):
        """
        Find out MIN and MAX values in the raster (data range) using r.describe.
        :return: list containing min and max values in the raster: [MIN, MAX]
        """
        inputMap = self.app.mainFrame.inputOutputPanel.input.GetValue()

        rasterMinMax = []

        rasterInfo = RunCommand('r.describe',
                                map=inputMap,
                                read=True,
                                flags='rn')

        if 'thru' in rasterInfo:
            #min thru max was returned
            ras = re.split('thru', rasterInfo)
            rasterMinMax.append(float(ras[0]))
            rasterMinMax.append(float(ras[1]))
        else:
            #min - max was returned
            ras = re.split('-', rasterInfo)
            rasterMinMax.append(float(ras[0]))
            rasterMinMax.append(float(ras[1]))

        rasterInfoStatusBar = RunCommand('r.describe',
                                         map=inputMap,
                                         read=True,
                                         nv='NULL')

        self.app.mainFrame.statustBar.SetStatusText("")
        self.app.mainFrame.statustBar.SetStatusText("Data range/categories: {}".format(rasterInfoStatusBar))

        return rasterMinMax
    #-----------------------------------------------------------------------------------------


    def __splitToSameIntervals(self, numberOfIntervals):
        """
        Calculates intervals based on numberOfIntervals that can be used to describe raster map.
        Categories or data range obtained from r.describe are printed to statusBar.
        :param numberOfIntervals:
        :return: list of intervals [ilist1, ilist2, ...], intervals are also lists - ilist = [left, right]
        """
        try:
            intervals = []

            Min, Max = self.__getRasterMinMax()
            Min = float(Min)
            Max = float(Max)
            length = Max - Min

            try:
                step = length/numberOfIntervals
            except ZeroDivisionError:
                intervals.append([Min, Max])
                return intervals

            l = Min
            for i in range(numberOfIntervals):

                p = l + step

                if( ((Max-p) / step) < 1 ):
                    intervals.append([l, Max])
                    break

                intervals.append([l, p])
                l = p + 1
        except:
            #cannot count intervals
            raise Exception
        else:
            return intervals
    #-----------------------------------------------------------------------------------------


    def __reclassify(self, inputMap, outputMap):
        """
        Create rules file based on data in the table.
        Calls r.reclass with given input and output map.
        Deletes rules file in the end.
        Data intervals which are not covered by the table are set to NULL.
        Overwrite is set to True.
        :param inputMap:
        :param outputMap:
        :return: void
        """
        rowNum = self.app.mainFrame.reclassifyPanel.table.GetNumberRows()
        tempRulesFile = open('Rules.tmp', 'w')

        for row in range(0, rowNum, 1):
            fr = self.app.mainFrame.reclassifyPanel.table.GetCellValue(row, 0)
            to = self.app.mainFrame.reclassifyPanel.table.GetCellValue(row, 1)
            equals = self.app.mainFrame.reclassifyPanel.table.GetCellValue(row, 2)
            label = self.app.mainFrame.reclassifyPanel.table.GetCellValue(row, 3)

            tempRulesFile.write('{} thru {} = {} {}\n'.format(fr, to, equals, label))

        #tempRulesFile.write('* = NULL')
        tempRulesFile.write('end')

        tempRulesFile.flush()
        tempRulesFile.close()

        reclassification = RunCommand("r.reclass",
                                       input = inputMap,
                                       output = outputMap,
                                       rules = 'Rules.tmp',
                                       overwrite = True)
        os.remove('Rules.tmp')

        if reclassification == 0:
            #succes
            return True
        else:
            return False

    def __okButtonClicked(self, event):
        """
        Makes reclassification and saves new map
        :param event:
        :return: void
        """
        self.app.mainFrame.statustBar.SetStatusText("")
        inputMap = self.app.mainFrame.inputOutputPanel.input.GetValue()
        outputMap = self.app.mainFrame.inputOutputPanel.output.GetValue()


        if self.__reclassify(inputMap, outputMap):
            self.app.mainFrame.statustBar.SetStatusText("Reclassification completed.")
        else:
            self.app.mainFrame.statustBar.SetStatusText("Reclassify Error: Invlaid input or output Map.")

    #-----------------------------------------------------------------------------------------


    def __cancelButtonClicked(self, event):
        """
        If rules file exists it is deleted.
        If preview exists it is removed.
        :param event:
        :return: void
        """
        try:
            os.remove('Rules.tmp')
        except:
            pass

        try:
            self.__removeRaster(rasterName='preview')
        except:
            pass

        self.app.mainFrame.Destroy()
    #-----------------------------------------------------------------------------------------

    def __removeRaster(self, rasterName):
        """
        Removes raster from the specified mapset
        :param rasterName: name of the raster map
        :param mapset: name of the raster mapset
        :return: void
        """
        RunCommand("g.remove",
                    flags = 'f',
                    type = "raster",
                    name = "{}".format(rasterName))
    #-----------------------------------------------------------------------------------------


    def __onInputRasterSelect(self, event, intNum=10):
        """
        Called on input map selection.
        Reclassify table is filled based on the data range in the input Map.
        Categories or data range obtained from r.describe are printed to statusBar.
        :param event:
        :param intNum: number of intervals
        :return: void
        """
        try:
            self.app.mainFrame.statustBar.SetStatusText("")

            rows = self.app.mainFrame.reclassifyPanel.table.GetNumberRows()
            try:
                self.app.mainFrame.reclassifyPanel.table.DeleteRows(0, rows)
            except:
                #no rows to delete
                pass

            intervals = self.__splitToSameIntervals(intNum)
            self.app.mainFrame.leftPanel.Layout()

            i = 0
            for interval in intervals:
                self.app.mainFrame.reclassifyPanel.table.AppendRows(numRows=1)
                rowsNumber = self.app.mainFrame.reclassifyPanel.table.GetNumberRows()
                self.app.mainFrame.reclassifyPanel.table.SetCellEditor(rowsNumber - 1, 3, wx.grid.GridCellTextEditor())
                self.app.mainFrame.reclassifyPanel.table.SetCellValue(i,0,str(interval[0]))
                self.app.mainFrame.reclassifyPanel.table.SetCellValue(i,1,str(interval[1]))
                self.app.mainFrame.reclassifyPanel.table.SetCellValue(i,2,str(i))
                i += 1
        except Exception:
            self.app.mainFrame.statustBar.SetStatusText("Iterval Error: Intervals cannot be counted.")


    #-----------------------------------------------------------------------------------------


    def __previewButtonClicked(self, event):
        """
        Creates a preview.
        New reclassified map is temporary created, drawm into the preview
        and then deleted. Drawn map stays after the deletion.
        :param event:
        :return: void
        """

        self.app.mainFrame.statustBar.SetStatusText("")

        inputMap = self.app.mainFrame.inputOutputPanel.input.GetValue()

        if not self.__reclassify(inputMap, outputMap='preview'):
            self.app.mainFrame.statustBar.SetStatusText("Preview Error: Invalid input Map.")
        else:
            self.app.mainFrame.previewPanel.map.DeleteAllLayers(overlay=True)

            cmdlist = ['d.rast', 'map=preview']
            self.app.mainFrame.previewPanel.map.AddLayer(ltype = 'raster', name = 'preview', command = cmdlist,
                                                         active = True, hidden = False, opacity = 1.0,
                                                         render = False)
            #self.app.mainFrame.previewPanel.map.SetRegion(windres=True, windres3=False)
            self.app.mainFrame.previewPanel.preview.UpdatePreview()
            self.__removeRaster(rasterName='preview')

            self.app.mainFrame.statustBar.SetStatusText("Preview completed.")

    #-----------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------
if __name__ == "__main__":
    pass
