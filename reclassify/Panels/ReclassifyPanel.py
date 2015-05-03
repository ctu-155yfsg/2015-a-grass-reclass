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
        self.__buildTable()
        #BUTTONS
        self.__buildButtonPanel()
        #LAYOUT
        self.__layout()
    #-----------------------------------------------------------------------------------------


    def __buildTable(self):
        """
        Creates table for displaying mapset classification.
        Table is made using wx.grid.Grid.
        :return: void
        """
        self.tablePanel = wx.Panel(self, wx.NewId())
        self.table = wx.grid.Grid(self.tablePanel)
        self.table.CreateGrid(10,2)

        for row in range(10):
            for col in range(2):
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

        hBox = wx.BoxSizer(wx.HORIZONTAL)
        hBox.Add(self.addButton, 0, wx.ALIGN_CENTER)
        hBox.Add(self.deleteButton, 0, wx.ALIGN_CENTER)
        self.buttonPanel.SetSizer(hBox)
    #-----------------------------------------------------------------------------------------


    def __layout(self):
        margin = 5
        sBox = wx.StaticBox(self, wx.NewId(), "Reclassification Table")
        vBox = wx.StaticBoxSizer(sBox, wx.VERTICAL)
        vBox.Add(self.tablePanel, 0, wx.ALL | wx.CENTER | wx.EXPAND, margin)
        vBox.Add(self.buttonPanel, 0, wx.ALL | wx.ALIGN_RIGHT, margin)
        self.SetSizer(vBox)
    #-----------------------------------------------------------------------------------------