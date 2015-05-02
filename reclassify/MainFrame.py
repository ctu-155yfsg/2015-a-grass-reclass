#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Subclass of wx.Frame"""

#-----------------------------------------------------------------------------------------
#Import
try:
    #wxPython
    import wx
    #python std library
    import sys
    #our modules and packages
    from Panels.InputOutputPanel import InputOutputPanel
    from Panels.ControlPanel import ControlPanel
    from Panels.PreviewPanel import PreviewPanel
    from Panels.ReclassifyPanel import ReclassifyPanel

except ImportError as err:
    print(u"ImportError: {}".format(err))
    sys.exit()
#-----------------------------------------------------------------------------------------

class MainFrame(wx.Frame):
    """
    Subclass of wx.Frame
    Represents main window
    """
    def __init__(self, parent, id, title):

        wx.Frame.__init__(self, parent, id, title, size = (750, 800))

        self.topPanel = wx.Panel(self, wx.NewId())
        self.CreateStatusBar()

        self.inputOutputPanel = InputOutputPanel(self.topPanel, wx.NewId())
        self.reclassifyPanel = ReclassifyPanel(self.topPanel, wx.NewId())
        self.previewPanel = PreviewPanel(self, wx.NewId())
        self.controlPanel = ControlPanel(self, wx.NewId())

        hBox = wx.BoxSizer(wx.HORIZONTAL)
        hBox.Add(self.inputOutputPanel, wx.EXPAND, 0)
        hBox.Add(self.reclassifyPanel, wx.EXPAND, 0)
        self.topPanel.SetSizer(hBox)

        vBox = wx.BoxSizer(wx.VERTICAL)
        vBox.Add(self.topPanel, 0, wx.EXPAND)
        vBox.Add(self.previewPanel, wx.EXPAND, wx.EXPAND)
        vBox.Add(self.controlPanel, 0, wx.EXPAND)

        self.SetSizer(vBox)

#-----------------------------------------------------------------------------------------
if __name__ == "__main__":
    pass