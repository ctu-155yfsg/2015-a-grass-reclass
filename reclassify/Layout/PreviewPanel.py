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
    #GRASS modules and packages
    from modules.colorrules import BufferedWindow
    from core.render import Map
    #our modules and packages

except ImportError as err:
    print(u"ImportError: {}".format(err))
    sys.exit("-1")
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
        #self.previewPanel.Hide() #hidden when no preview active
    #-----------------------------------------------------------------------------------------


    def __buildPreviewPanel(self):
        """
        Creates preview panel.
        :return: void
        """

        try:
            #Output preview
            self.map = Map()
            self.width = self.map.width = 400
            self.height = self.map.height = 300
            self.map.geom = self.width, self.height

            self.preview = BufferedWindow(parent=self,
                                          id=wx.NewId(),
                                          size = (400, 300),
                                          Map=self.map)
            self.preview.EraseMap()

        except Exception as err:
            print(err)


    #-----------------------------------------------------------------------------------------


    def __layout(self):
        """
        Specifies final layout for PreviewPanel.
        :return: void
        """

        sBox = wx.StaticBox(self, wx.NewId(), "Preview")
        vBox = wx.StaticBoxSizer(sBox, wx.VERTICAL)
        vBox.Add(self.preview, wx.ALIGN_CENTER, wx.ALIGN_CENTER)
        self.SetSizer(vBox)
    #-----------------------------------------------------------------------------------------


if __name__ == "__main__":
    pass