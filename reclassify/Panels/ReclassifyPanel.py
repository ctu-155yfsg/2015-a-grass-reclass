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
    sys.exit()
#-----------------------------------------------------------------------------------------
class ReclassifyPanel(wx.Panel):

    def __init__(self, parent, id):
        wx.Panel.__init__(self, parent, id)
        self.SetBackgroundColour('Red')