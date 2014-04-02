#!/usr/local/bin/python
"""

    hatched_line_test.py 

Example script for adding a hatched line 

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

# =============================================================================
# External Python modules
# =============================================================================
import numpy

# =============================================================================
# Extension modules
# =============================================================================
sys.path.append(os.path.abspath('../'))

from pyCarpetPlot import *

# =============================================================================
# 
# =============================================================================
       
xx = numpy.linspace(0,10,11)
yy1 = xx**2
yy2 = 2 * yy1
yy3 = 0.5 * yy1
# yy2 = 2 * xx

ax1 = plt.subplot(111)
ax1.plot(xx,yy1, 'ok')
ax1.set_xlabel('X Values')
ax1.set_ylabel('Y Values')

ax1 = hatched_line(xx, yy2, ax1, flip = True)
ax1 = hatched_line(xx, yy3, ax1, flip = False)
ax1 = hatched_line([0,10], [20]*2, ax1, flip = True)
ax1 = hatched_line([0,10], [40]*2, ax1, flip = False)

plt.show()
