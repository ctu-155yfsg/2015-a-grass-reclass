#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Subclass of wx.Panel"""

#-----------------------------------------------------------------------------------------
#Import
try:
    #wxPython
    import wx
    import wx.grid
    import wx.lib.scrolledpanel
    #python std library
    import sys
    #our modules and packages

except ImportError as err:
    print(u"ImportError: {}".format(err))
    sys.exit("-1")
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
        self.tableCol = 3
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
        #self.tablePanel = wx.lib.scrolledpanel.ScrolledPanel(self, wx.NewId(), size=(200,300))
        #self.tablePanel.SetupScrolling()
        self.table = wx.grid.Grid(self.tablePanel)
        self.table.CreateGrid(0, self.tableCol)

        self.table.SetColLabelValue(0, "Lower limit")
        self.table.SetColLabelValue(1, "Upper limit")
        self.table.SetColLabelValue(2, "Value")

        self.table.SetDefaultEditor(wx.grid.GridCellNumberEditor(-1, -1))
        #for row in range(10):
        #    for col in range(self.nCol):
        #        self.table.SetCellValue(row, col, "({}, {})".format(row, col))



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
        self.previewButton = wx.Button(self.buttonPanel, wx.NewId(), "Preview", size=(100, -1))

        vBox = wx.BoxSizer(wx.VERTICAL)
        vBox.Add(self.addButton, 0, wx.ALIGN_CENTER)
        vBox.Add(self.deleteButton, 0, wx.ALIGN_CENTER)
        vBox.Add(self.previewButton, 0, wx.ALIGN_CENTER)
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


if __name__ == "__main__":
    pass