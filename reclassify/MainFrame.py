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
    from Layout.InputOutputPanel import InputOutputPanel
    from Layout.ControlPanel import ControlPanel
    from Layout.PreviewPanel import PreviewPanel
    from Layout.ReclassifyPanel import ReclassifyPanel

except ImportError as err:
    print(u"ImportError: {}".format(err))
    sys.exit("-1")
#-----------------------------------------------------------------------------------------

class MainFrame(wx.Frame):
    """
    Subclass of wx.Frame.
    Top level frame.
    Represents main window.
    """
    def __init__(self, parent, id, title):

        wx.Frame.__init__(self, parent, id, title, size = (1000, 600))

        self.statustBar = self.CreateStatusBar()
        self.SetMinSize( (1000, 600) )

        self.topPanel = wx.Panel(self, wx.NewId())
        self.leftPanel = wx.Panel(self.topPanel, wx.NewId())

        self.inputOutputPanel = InputOutputPanel(self.leftPanel, wx.NewId())
        self.reclassifyPanel = ReclassifyPanel(self.leftPanel, wx.NewId())
        self.previewPanel = PreviewPanel(self.topPanel, wx.NewId())
        self.controlPanel = ControlPanel(self, wx.NewId())

        leftPanelvBox = wx.BoxSizer(wx.VERTICAL)
        leftPanelvBox.Add(self.inputOutputPanel, 0, 0)
        leftPanelvBox.Add(self.reclassifyPanel, wx.EXPAND, 0)
        self.leftPanel.SetSizer(leftPanelvBox)

        topPanelhBox = wx.BoxSizer(wx.HORIZONTAL)
        topPanelhBox.Add(self.leftPanel, 0, wx.EXPAND)
        topPanelhBox.Add(self.previewPanel, wx.EXPAND, wx.EXPAND)
        self.topPanel.SetSizer(topPanelhBox)

        vBox = wx.BoxSizer(wx.VERTICAL)
        vBox.Add(self.topPanel, wx.EXPAND, wx.EXPAND)
        vBox.Add(self.controlPanel, 0, wx.EXPAND)

        self.SetSizer(vBox)


#-----------------------------------------------------------------------------------------
if __name__ == "__main__":
    pass