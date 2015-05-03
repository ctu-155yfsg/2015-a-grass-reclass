#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Subclass of wx.Panel"""

#-----------------------------------------------------------------------------------------
#Import
try:
    #wxPython
    import wx
    import wx.grid
    #python std library
    import sys
    #our modules and packages

except ImportError as err:
    print(u"ImportError: {}".format(err))
    sys.exit()
#-----------------------------------------------------------------------------------------
class ReclassifyPanel(wx.Panel):
    """
    Subclass of wx.Panel.
    Represents top-right part of the window.
    Contains reclassification table, delete entry
    button and add entry button.
    """

    def __init__(self, parent, id):

        wx.Panel.__init__(self, parent, id)
        #TABLE
        self.nCol = 2
        self.__buildTable()
        #BUTTONS
        self.__buildButtonPanel()
        #LAYOUT
        self.__layout()
        #self.SetMinSize((400, -1))
    #-----------------------------------------------------------------------------------------


    def __buildTable(self):
        """
        Creates table for displaying mapset classification.
        Table is made using wx.grid.Grid.
        :return: void
        """
        self.tablePanel = wx.Panel(self, wx.NewId())
        self.table = wx.grid.Grid(self.tablePanel)
        self.table.CreateGrid(10, self.nCol)

        self.table.SetColLabelValue(0, "Range")
        self.table.SetColLabelValue(1, "Value")

        for row in range(10):
            for col in range(self.nCol):
                self.table.SetCellValue(row, col, "({}, {})".format(row, col))

        box = wx.BoxSizer(wx.HORIZONTAL)
        box.Add(self.table, wx.EXPAND, wx.EXPAND)
        self.tablePanel.SetSizer(box)
    #-----------------------------------------------------------------------------------------


    def __buildButtonPanel(self):
        """
        Creates delete entry button and add entry button.
        :return: void
        """
        self.buttonPanel = wx.Panel(self, wx.NewId())
        self.addButton = wx.Button(self.buttonPanel, wx.NewId(), "Add", size=(100, -1))
        self.deleteButton = wx.Button(self.buttonPanel, wx.NewId(), "Delete", size=(100, -1))

        vBox = wx.BoxSizer(wx.VERTICAL)
        vBox.Add(self.addButton, 0, wx.ALIGN_CENTER)
        vBox.Add(self.deleteButton, 0, wx.ALIGN_CENTER)
        self.buttonPanel.SetSizer(vBox)
    #-----------------------------------------------------------------------------------------


    def __layout(self):
        """
        Specifies final layout in Reclassify Panel
        :return: void
        """
        margin = 5
        sBox = wx.StaticBox(self, wx.NewId(), "Reclassification Table")
        hBox = wx.StaticBoxSizer(sBox, wx.HORIZONTAL)
        hBox.Add(self.tablePanel, 0, wx.ALL | wx.CENTER | wx.EXPAND, margin)
        hBox.Add(self.buttonPanel, 0, wx.ALL | wx.ALIGN_TOP, margin)
        self.SetSizer(hBox)
    #-----------------------------------------------------------------------------------------