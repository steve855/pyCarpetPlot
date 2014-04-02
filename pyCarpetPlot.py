#!/usr/local/bin/python
"""

    pyCarpetPlot.py 

Library of functions to generate carpet plots 

Copyright (c) 2004-2013 by pyACDT Developers
All rights reserved.
Revision: Stephen Andrews - $Date: 02/04/2014$


Developers:
-----------
- Stephen Andrews (SA) 

History
-------
    v. Stephen Andrews  - 
"""

__version__ = '$Revision: $'

"""
To Do:
    - 
"""

# =============================================================================
# Standard Python modules
# =============================================================================
import os, sys
import pdb
from math import radians, sin, cos, ceil

# =============================================================================
# External Python modules
# =============================================================================
import numpy
import matplotlib.pyplot as plt

# =============================================================================
# Extension modules
# =============================================================================
sys.path.append(os.path.abspath('../'))

# =============================================================================
# 
# =============================================================================

def carpet_plot(x1, x2, y, ofst = 1, ofst2 = 0.0, axis = None, x1_skip = 1, x2_skip = 1, label1 = '', label2 = '',  label1_loc = 'end', label2_loc = 'end', dep_title = '', contour_data = None):
    '''

    Generates a carpet plot of the data 

    Plots the data in :math:`y` against the 'cheater axis' 

    _math::

        x_{cheat} = x_1 + \mathrm{ofst} \cdot x_2

    This shows the relationship between x1 and x2 with y but destroys information about how y varries with
    x1 and x2 

    **Inputs** 

    - x1 -> (n x 1) numpy array: Vector of first independant values.
    - x2 -> (m x 1) numpy array: Vector of seccond independant values.
    - y -> (n x m) numpy.array: Matrix of dependant values.
    - ofst -> FLOAT: Offset factor, can be used to change the shape of the plot, *Default 1.0*
                        - ofst = 1 : trend of y with x1 and x2 of similar magnitude
                        - ofst > 1 : trend of y with x2 more pronounced 
                        - ofst < 1 : trend of y with x1 more pronounced
    - ofst2 -> FLOAT: Offset for plotting multiple carpet plots on one axis
    - axis -> matplotlib.pyplot.axis: An axis object to plot on
    - x1_skip -> INT: Value n to read every n values. 
    - x2_skip -> INT: Value n to read every n values.
    - label1 -> STR: Labels to append to the curves of x1. *Default: ''* 
    - label2 -> STR: Labels to append to the curves of x2. *Default: ''* 
    - label1_loc -> STR: Location of x1 labels. *Default: 'end'* 
                    - 'end': at the end of the data 
                    - 'start': at the start of the data 
                    - None: do not show labels
    - label2_loc -> STR: Location of x2 labels. *Default: 'end'* 
                    - 'end': at the end of the data 
                    - 'start': at the start of the data 
                    - None: do not show labels
    - dep_title -> STR: Title to append to the dependant axis
    - contour_data - > (n x m) numpy.array: Matrix of dependant values to plot as a contour. *Default: None*

    '''

    # Input checks and conditioning
    y = numpy.array(y)
    contour_data = numpy.array(contour_data)

    # for var in [y, contour_data]: 
    #     if not (len(x2), len(x1)) == var.shape:
    #         raise Exception('Shape of input does not agree %s != (%d x %d)'%(var.shape, len(x2), len(x1)))
    #     #end
    # #end

    def label_map(label_loc):     
        if label_loc == None : return None
        elif label_loc.lower()[0] == 's': return 0
        elif label_loc.lower()[0] == 'e': return -1
        else: raise Exception('Invalid data label location')
    #end

    def draw_label(text, loc_xy, label_loc, axis):
        if label_loc > 0:
             ha = 'right'
             va = 'bottom'
        else:
             ha = 'left'
             va = 'bottom'
        #end
        axis.annotate(text, xy = loc_xy, xytext = (15, 0), textcoords = 'offset points', ha = ha, va = va)

    
    label1_loc, label2_loc = map(label_map, [label1_loc, label2_loc])

    xx1, xx2 = numpy.meshgrid(x1, x2)

    x_cheat = ofst2 + (xx1 + ofst * xx2)
    
    if axis == None:
        ax1 = plt.subplot(111)
    else:
        ax1 = axis
    #end

    for i in xrange(0,len(x1),x1_skip):
        ax1.plot(x_cheat[:,i], y[:,i], '-k')
        if not label1_loc == None:
            ax1.annotate(r'%s = %3.2f'%(label1, x1[i]), xy = (x_cheat[label1_loc,i], y[label1_loc,i]), xytext = (15, 0), textcoords = 'offset points')
            # draw_label(r'%s = %3.2f'%(label1, x1[i]), (x_cheat[label1_loc,i], y[label1_loc,i]), label1_loc, ax1)
        #end
    #end

    for i in xrange(0,len(x2),x2_skip):
        ax1.plot(x_cheat[i,:], y[i,:], '-k')
        if not label2_loc == None:
            ax1.annotate(r'%s = %3.2f'%(label2, x2[i]), xy = (x_cheat[i,label2_loc], y[i,label2_loc]), xytext = (10, 15), textcoords = 'offset points')
            # draw_label(r'%s = %3.2f'%(label2, x2[i]), (x_cheat[i,label2_loc], y[i,label2_loc]), label2_loc, ax1)
        #end

    if not contour_data == None:
        try:
            CS = ax1.contour(x_cheat, y, contour_data, colors='b')
            ax1.clabel(CS, fontsize=9, inline=1)
        except:
            pass
        #end
    #end

    ax1.set_ylabel(dep_title)
    ax1.axes.get_xaxis().set_visible(False)

    return ax1
#end

def hatched_line(x, y, axis, spc = 0.03, theta = 45, len_tick = 0.015, flip = False, linestyle = None):
    try:
        from scipy.interpolate import interp1d 
    except:
        raise Exception('scipy required to plot hatched lines')
    #end

    x = numpy.array(x)
    y = numpy.array(y)
    
    # Calculate the aspect ratio of the plot
    aspect_ratio = axis.axis()
    aspect_ratio = (aspect_ratio[1] - aspect_ratio[0]) / (aspect_ratio[3] - aspect_ratio[2])

    if flip:
        flip = -1
    else:
        flip = 1
    #end

    # Calcualte the distance along the curve
    ds = numpy.sqrt((x[1:] - x[:-1])**2 + ((y[1:] - y[:-1])*aspect_ratio)**2)
    s_tot = sum(ds)
    ds = numpy.concatenate(([0.0], numpy.cumsum(ds)))

    # Determine the x and y corrdinates of the tick root
    s_tick = numpy.linspace(0, s_tot, ceil(1 / spc))
    x_tick = interp1d(ds, x, bounds_error = False)(s_tick)
    y_tick = interp1d(ds, y, bounds_error = False)(s_tick)

    # Calcualte the normal to the curve at the tick root
    delta_s = spc * s_tot
    v_tick = (x_tick - interp1d(ds, x, bounds_error = False)(s_tick + delta_s)) / delta_s
    u_tick = (y_tick - interp1d(ds, y, bounds_error = False)(s_tick + delta_s)) / (delta_s * aspect_ratio)
    n = numpy.sqrt(u_tick **2 + v_tick **2)
    
    # Calcualte the offset in x and y for the tick
    theta = radians(theta)
    trans_matrix = numpy.array([[cos(theta), -sin(theta)],[sin(theta), cos(theta)]])
    dxy = numpy.dot(numpy.array([u_tick / n , v_tick / n]).T, trans_matrix) * len_tick * s_tot 

    # Draw the base line
    base_line = plt.Line2D(x_tick, y_tick)
    axis.add_line(base_line)

    # Draw each tick
    for i in xrange(len(x_tick)):
        axis.add_line(plt.Line2D([x_tick[i], x_tick[i] - flip * dxy[i,0]], [y_tick[i], (y_tick[i] - flip * dxy[i,1] / aspect_ratio)]))
    #end

    return axis
#end