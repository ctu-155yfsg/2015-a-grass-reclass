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

except ImportError as err:
    print(u"ImportError: {}".format(err))
    sys.exit()
#-----------------------------------------------------------------------------------------

class OurFrame(wx.Frame):

    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size = (750, 800))


        """
        panel = wx.Panel(self)
        statusBar = self.CreateStatusBar()

        button = wx.Button(panel, label = u"Hello", pos = (300, 200), size = (100, 30))
        self.Bind(wx.EVT_BUTTON, self.OnHelloClicked, button)
        """


    def OnHelloClicked(self, event):
        print(u"button clicked\n")

#-----------------------------------------------------------------------------------------
if __name__ == "__main__":
    pass