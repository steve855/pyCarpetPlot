#!/usr/local/bin/python
"""

	3_indep_2_dep.py 

Carpet plot of three independant variables against two dependant  

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
f = lambda x1 ,x2, x3: 0.5*x3 * (x1**2+x2**2-2*x1-2*x2+2)

x1 = numpy.linspace(2,5,4)
x2 = numpy.linspace(1,3,3)
x3 = numpy.linspace(1,2,3)

ofst2 = 0
ax1 = plt.subplot(111)
label_points = [(0.25, 0.50), (0.50, 0.70), (0.80,0.90)]
for k in xrange(len(x3)):
	fobj = []
	for i in xrange(len(x1)):
		tmp = []
		for j in xrange(len(x2)):
			tmp.append(f(x1[i], x2[j], x3[k]))
		#end
		fobj.append(tmp)
	#end
	fobj = numpy.array(fobj)
	ax1 = carpet_plot(x1,x2,fobj.T, ofst = 2.5 ,ofst2 = ofst2, axis = ax1, label1 = r'$x_{1}$', label2 = r'$x_{2}$', label2_loc = 'start', dep_title = 'Dependant Variable')
	ax1.annotate(r'$x_{3}$ = %3.2f'%(x3[k]), xy = label_points[k], textcoords = 'axes fraction', bbox = {'facecolor':'white', 'alpha':0.5})
	ofst2 += 10
#end

plt.show()
