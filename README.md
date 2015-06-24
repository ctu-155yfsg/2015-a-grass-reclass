# Reclassification tool for GRASS GIS

Semester project of 155YFSG class (academic year 2014/2015) CTU Prague Department of Geomatic

* Group A

### Authors

* Rokusek Jaromír
* Svoboda Ondřej

### Task

Create a GUI application which work as a wrapper for GRASS GIS reclassification tool. 
This application should work as a plugin and it should be written in Python 2.x.x with usage of wxPython.
It has to be able to show a preview of reclassification.

# Quick Guide

### Introduction

This tool was made as a school project at the Czech Technical University in Prague - Department of Geomatic. 
It is a GUI wrapper over GRASS reclassification tool. It is not a new implementation of a recllasification tool itself. 
It’s just a GUI application that uses the old recllasification tool and it is ment to be easier to use and also more practical.

### Advantages
* There is no need for reclassification rules file. 
** See [r.reclass](http://grass.osgeo.org/grass71/manuals/r.reclass.html) for more info on rules file.
* There is a preview of a new reclassified map.

### Usage
Program is very simple. You just have to select input map which is the one you want to reclassify and you also have to specify where the output should be saved. 
Output can be an existing map. In this case it is overwritten. But it  can also be a new non existing map. 
In this case you just need to write it’s name into the output raster map field. Map with this name is automatically created into current mapset. 

![image 1](/images/range.jpg)

After the specification of  input and output maps, you can set reclassification rules. To do this there is a table which is easy to understand (see image 1). 
The table is automatically filled with some values when input map is selected. 
The main reason of that is that you can see minimum and maximum values present in a map. 
But that’s not all. There is a statusbar which will help you even more. 
It is displaying either range of values (image 1) or list of categories (image 2) present in the map based on the map type. 
This decision is made by GRASS function [r.describe.](http://grass.osgeo.org/grass71/manuals/r.describe.html)

![image 2](/images/categories.jpg)

Table can be adjusted by Add and Delete buttons, which are used to add or remove rows.
Reclassification rules are set by defining a range and it’s new value. Defining a label is optional. 
Label is just a name for the category. Lower and Upper limits defines the range. It is a closed interval.
Preview button is used for displaying a preview. Ok button confirms everything and performs reclassification. 
Cancel button cancels everything and closes the window.







