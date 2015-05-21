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
    from Controler import Controler

except ImportError as err:
    print(u"ImportError: {}".format(err))
    sys.exit("-1")
#-----------------------------------------------------------------------------------------

def main():
    """
    Entry point.
    """
    app = OurApp(redirect=True)    #redirect=False -> error output goes to command line
    control = Controler(app)
    app.MainLoop()

    return 0
#-----------------------------------------------------------------------------------------
if __name__ == "__main__":
    sys.exit(main())
