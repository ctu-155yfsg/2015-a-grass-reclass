#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Reclassification tool for GRASS"""

#-----------------------------------------------------------------------------------------
#Import
try:
    #wxPython

    #python std library
    import sys
    #our modules and packages
    from OurApp import OurApp

except ImportError as err:
    print(u"ImportError: {}".format(err))
    sys.exit()
#-----------------------------------------------------------------------------------------

def main():
    """
    Entry point.
    """
    app = OurApp(redirect=False)    #redirect=False -> error output goes to command line
    app.MainLoop()

#-----------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
