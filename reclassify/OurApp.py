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
    from OurFrame import OurFrame

except ImportError as err:
    print(u"ImportError: {}".format(err))
    sys.exit()
#-----------------------------------------------------------------------------------------
class OurApp(wx.App):

    def OnInit(self):
        self.mainFrame = OurFrame(parent = None, id = wx.NewId(), title = u"Reclass")
        self.SetTopWindow(self.mainFrame)
        self.mainFrame.Show()
        return True

#-----------------------------------------------------------------------------------------
if __name__ == "__main__":
    pass