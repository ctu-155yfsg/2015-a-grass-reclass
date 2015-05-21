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
    #from modules.colorrules import BufferedWindow
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

        #BINDING
        self.app.mainFrame.controlPanel.reclassifyButton.Bind(wx.EVT_BUTTON, self.__reclassifyButtonClicked)
        self.app.mainFrame.controlPanel.cancelButton.Bind(wx.EVT_BUTTON, self.__cancelButtonClicked)

        self.app.mainFrame.reclassifyPanel.addButton.Bind(wx.EVT_BUTTON, self.__addButtonClicked)
        self.app.mainFrame.reclassifyPanel.deleteButton.Bind(wx.EVT_BUTTON, self.__deleteButtonClicked)
        self.app.mainFrame.reclassifyPanel.previewButton.Bind(wx.EVT_BUTTON, self.__previewButtonClicked)

        self.app.mainFrame.controlPanel.reclassifyButton.Bind(wx.EVT_BUTTON, self.__reclassifyButtonClicked)

    #-----------------------------------------------------------------------------------------


    def __addButtonClicked(self, event):
        """
        Append one row to the reclassify table.
        :param event:
        :return: void
        """
        self.app.mainFrame.reclassifyPanel.table.AppendRows(numRows=1)
        self.app.mainFrame.leftPanel.Layout()
    #-----------------------------------------------------------------------------------------


    def __deleteButtonClicked(self, event):
        """
        Removes selected rows from the reclassify table.
        :param event:
        :return: void
        """
        selectedRow = self.app.mainFrame.reclassifyPanel.table.GetSelectedRows()

        for I in range(len(selectedRow), 0, -1):
            self.app.mainFrame.reclassifyPanel.table.DeleteRows(pos=I, numRows=1)

        self.app.mainFrame.leftPanel.Layout()
    #-----------------------------------------------------------------------------------------


    def __getRasterMinMax(self):
        """
        Find out MIN and MAX value in the raster using r.describe.
        :return: list containing min and max values in the raster: [MIN, MAX]
        """
        inputMap = self.app.mainFrame.inputOutputPanel.input.GetValue()

        rasterInfo = RunCommand('r.describe', map=inputMap, read=True)
        rasterMinMax = re.split('-', rasterInfo)

        return rasterMinMax
    #-----------------------------------------------------------------------------------------


    def __splitToSameIntervals(self, numberOfIntervals):
        """
        Calculates intervals based on numberOfIntervals that can be used to describe raster map
        :param numberOfIntervals:
        :return: list of intervals [ilist1, ilist2, ...], intervals are also lists - ilist = [left, right]
        """
        intervals = []

        Min, Max = self.__getRasterMinMax()
        Min = int(float(Min))
        Max = int(float(Max))
        length = Max - Min

        try:
            step = int(length/numberOfIntervals)
        except ZeroDivisionError:
            intervals.append([Min, Max])
            return intervals

        print('Min: {}\nMax: {}\nStep: {}'.format(Min, Max, step))

        if(step < 1):
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

        return intervals


    def __previewButtonClicked(self, event):
        #pass
        intervals = self.__splitToSameIntervals(2)

        self.app.mainFrame.reclassifyPanel.table.AppendRows(numRows=2)
        self.app.mainFrame.leftPanel.Layout()

        i = 0
        for interval in intervals:
            self.app.mainFrame.reclassifyPanel.table.SetCellValue(i,0,str(interval[0]))
            self.app.mainFrame.reclassifyPanel.table.SetCellValue(i,1,str(interval[1]))
            self.app.mainFrame.reclassifyPanel.table.SetCellValue(i,2,str((interval[0]+interval[1])/2))
            i += 1
    #-----------------------------------------------------------------------------------------


    def __reclassifyButtonClicked(self, event):
        """
        Create rules file based on data in the table.
        Calls r.reclass with given input and output map.
        Deletes rules file in the end.
        Data intervals which are not covered by the table are set to NULL.
        :param event:
        :return: void
        """
        rowNum = self.app.mainFrame.reclassifyPanel.table.GetNumberRows()
        inputMap = self.app.mainFrame.inputOutputPanel.input.GetValue()
        outputMap = self.app.mainFrame.inputOutputPanel.output.GetValue()

        print(inputMap)

        tempRulesFile = open('Rules.tmp', 'w')

        for row in range(0, rowNum, 1):
            fr = self.app.mainFrame.reclassifyPanel.table.GetCellValue(row, 0)
            to = self.app.mainFrame.reclassifyPanel.table.GetCellValue(row, 1)
            equals = self.app.mainFrame.reclassifyPanel.table.GetCellValue(row, 2)

            tempRulesFile.write('{} thru {} = {}\n'.format(fr, to, equals))

        tempRulesFile.write('* = NULL')

        tempRulesFile.flush()
        tempRulesFile.close()

        RunCommand("r.reclass",
                    input = inputMap,
                    output = outputMap,
                    rules = 'Rules.tmp',
                    overwrite = True)

        os.remove('Rules.tmp')
    #-----------------------------------------------------------------------------------------


    def __cancelButtonClicked(self, event):
        """
        If rules file exists it is deleted.
        :param event:
        :return: void
        """
        try:
            os.remove('Rules.tmp')
        except:
            pass
    #-----------------------------------------------------------------------------------------

    def __removeRaster(self, rasterName, mapset):
        """
        Removes raster from the specified mapset
        :param rasterName: name of the raster map
        :param mapset: name of the raster mapset
        :return: void
        """
        RunCommand("g.remove",
                    flags = 'f',
                    type = "raster",
                    name = "{}@{}".format(rasterName, mapset))
    #-----------------------------------------------------------------------------------------

    def __initializeReclassTable(self):
        pass

#-----------------------------------------------------------------------------------------
if __name__ == "__main__":
    pass
