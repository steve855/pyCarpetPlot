#!/usr/local/bin/python
"""

	2_indep_1_dep.py 

Carpet plot of two independant variables against one dependant  

Copyright (c) 2004-2013 by pyACDT Developers
All rights reserved.
Revision: 1.0 - $Date: 02/04/2014$


Developers:
-----------
- Stephen Andrews (SA) 

History
-------
    v. 1
   .0  - 
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
f = lambda x1 ,x2: x1**2+x2**2-2*x1-2*x2+2
f2 = lambda x1 ,x2: (x1*x2)**0.5

x1 = numpy.linspace(2,5,4)
x2 = numpy.linspace(1,3,3)

fobj = []
contour = []
for i in xrange(len(x1)):
	tmp = []
	tmp2 = []
	for j in xrange(len(x2)):
		tmp.append(f(x1[i], x2[j]))
		tmp2.append(f2(x1[i], x2[j]))
	#end
	fobj.append(tmp)
	contour.append(tmp2)
#end

fobj = numpy.array(fobj)
contour = numpy.array(contour)

# pdb.set_trace()
ax1 = carpet_plot(x1,x2,fobj.T, ofst = 3, label1 = r'$x_{1}$', label2 = r'$x_{2}$', label1_loc = 'end', label1_ofst = (10,0), label2_ofst = (0,15), dep_title = 'Dependant Variable', contour_data = contour.T)
plt.show()
