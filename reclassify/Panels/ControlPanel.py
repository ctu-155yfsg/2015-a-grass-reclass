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
class ControlPanel(wx.Panel):
    """
    Subclass of wx.Panel.
    Represents bottom part of the window.
    Contains progress bar (reclassification),
    reclassify button and cancel button.
    """

    def __init__(self, parent, id):

        wx.Panel.__init__(self, parent, id)

        self.SetBackgroundColour('Yellow')