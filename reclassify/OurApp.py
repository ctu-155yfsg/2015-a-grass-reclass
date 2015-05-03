#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Subclass of wx.App"""

#-----------------------------------------------------------------------------------------
#Import
try:
    #wxPython
    import wx
    #python std library
    import sys
    #our modules and packages
    from MainFrame import MainFrame

except ImportError as err:
    print(u"ImportError: {}".format(err))
    sys.exit()
#-----------------------------------------------------------------------------------------
class OurApp(wx.App):
    """
    Subclass of wx.App
    Has only one frame which is also a top level frame.
    """
    def OnInit(self):
        self.mainFrame = MainFrame(parent = None, id = wx.NewId(), title = u"Reclass")
        self.SetTopWindow(self.mainFrame)
        self.mainFrame.Show()
        return True

#-----------------------------------------------------------------------------------------
if __name__ == "__main__":
    pass