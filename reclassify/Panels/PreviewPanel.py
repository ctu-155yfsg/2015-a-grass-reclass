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
class PreviewPanel(wx.Panel):
    """
    Subclass of wx.Panel.
    Represents center part of the window.
    Contains preview of the reclassified mapset.
    """

    def __init__(self, parent, id):

        wx.Panel.__init__(self, parent, id)

        #PREVIEW
        self.__buildPreviewPanel()
        #LAYOUT
        self.__layout()

        #self.SetBackgroundColour('Blue')
    #-----------------------------------------------------------------------------------------


    def __buildPreviewPanel(self):
        """
        Creates preview panel.
        Preview is displayed using wx.StaticBitmap
        :return: void
        """
        self.previewPanel = wx.Panel(self, wx.NewId())
        image = wx.Image("D:/GRASS_RECLAS/test.jpg", wx.BITMAP_TYPE_JPEG)
        temp = image.ConvertToBitmap()
        self.preview = wx.StaticBitmap(self.previewPanel, bitmap=temp)

        Box = wx.BoxSizer(wx.HORIZONTAL)
        Box.Add(self.preview, 0, wx.ALIGN_CENTER)
        self.previewPanel.SetSizer(Box)


    #-----------------------------------------------------------------------------------------


    def __layout(self):
        """
        Specifies final layout for PreviewPanel.
        :return: void
        """
        sBox = wx.StaticBox(self, wx.NewId(), "Preview")
        vBox = wx.StaticBoxSizer(sBox, wx.VERTICAL)
        vBox.Add(self.previewPanel, wx.ALIGN_CENTER, wx.ALIGN_CENTER)
        self.SetSizer(vBox)
    #-----------------------------------------------------------------------------------------