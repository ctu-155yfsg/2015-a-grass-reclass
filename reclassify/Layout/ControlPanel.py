#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Subclass of wx.Panel"""

#-----------------------------------------------------------------------------------------
#Import
try:
    #wxPython
    import wx
    #python std library
    import sys
    #our modules and packages

except ImportError as err:
    print(u"ImportError: {}".format(err))
    sys.exit("-1")
#-----------------------------------------------------------------------------------------
class ControlPanel(wx.Panel):
    """
    Subclass of wx.Panel.
    Represents bottom part of the window.
    Contains progress bar (reclassification),
    reclassify button and cancel button.
    """

    def __init__(self, parent, id):

        wx.Panel.__init__(self, parent, id)

        #BUTTONS
        self.__buildButtonsPanel()
        #PROGRESSBAR
        self.__buildProgressBarPanel()
        #LAYOUT
        self.__layout()

        self.progressBar.Hide()
    #-----------------------------------------------------------------------------------------


    def __buildButtonsPanel(self):
        """
        Creates reclassify button and cancel button.
        :return: void
        """
        self.buttonPanel = wx.Panel(self, wx.NewId())
        self.reclassifyButton = wx.Button(self.buttonPanel, wx.NewId(), "Reclassify", size=(100, -1))
        self.cancelButton = wx.Button(self.buttonPanel, wx.NewId(), "Cancel", size=(100, -1))

        hBox = wx.BoxSizer(wx.HORIZONTAL)
        hBox.Add(self.reclassifyButton, 0, wx.ALIGN_CENTER)
        hBox.Add(self.cancelButton, 0, wx.ALIGN_CENTER)
        self.buttonPanel.SetSizer(hBox)

    #-----------------------------------------------------------------------------------------


    def __buildProgressBarPanel(self):
        """
        Creates progress Bar.
        :return: void
        """
        self.progressBarPanel = wx.Panel(self, wx.NewId())
        self.progressBar = wx.Gauge(self.progressBarPanel, wx.NewId(), 100)
        self.progressBar.SetValue(33)

        margin = 5
        hBox = wx.BoxSizer(wx.HORIZONTAL)
        hBox.Add(self.progressBar, wx.EXPAND, wx.CENTER | wx.ALL | margin)
        self.progressBarPanel.SetSizer(hBox)
    #-----------------------------------------------------------------------------------------


    def __layout(self):
        """
        Specifies final layout inside the Control Panel.
        :return: void
        """
        margin = 5
        vBox = wx.BoxSizer(wx.VERTICAL)
        vBox.Add(self.progressBarPanel, 0, wx.ALL | wx.CENTER | wx.EXPAND, margin)
        vBox.Add(self.buttonPanel, 0, wx.ALL | wx.ALIGN_RIGHT, margin)
        self.SetSizer(vBox)
    #-----------------------------------------------------------------------------------------


if __name__ == "__main__":
    pass