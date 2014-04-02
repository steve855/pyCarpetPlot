pyCarpetPlot
============

Library of Python functions to generate carpet plots

**Author**: Stephen Andrews
			<www.aircraftdesign.ca>
			
**Acknowledgements**: This library is heavily based on the matlab functions provided by Dr. McDonals in Ref. 1.

Dependencies
------------

* numpy
* matplotlib
* scipy (for hatched lines only)


References
----------

1. McDonald, Rob. "Carpet Plot Toolkit". <http://www.mathworks.com/matlabcentral/fileexchange/40831-carpet-plot-toolkit>

2. Powers, S. A.. "Generation of Carpet Plots". <http://www.dept.aoe.vt.edu/~mason/Mason_f/SD1CarpetsbySAP.pdf>


Carpet Plot Basics
------------------

A carpet plot displays the relationship between two independent variables and one dependant variable. In these plots, the abscissa uses an arbitrary scale which distorts the individual relationships between each independent variable and the dependant variable. The advantage of this plot is that combinations of the two independent variables which yield a desired dependant variable value are easy to identify.

Each line on the carpet plot represents a variation of one independent variable while the other is maintained constant. Each of these iso-lines is labelled with the corresponding value of the independent variable which is held constant.

To Do
-----

- Give user greater control for placement of curve labels
- Allow constraint lines to be added to carpet plot 
- Streamline generation of three DOF plots


Examples
--------

Thee example plots are contained in the examples directory

2_indep_1_dep
-------------

This example shows a carpet plot of two a dependant variable against two independent variables x1 and x2. Two different choices of offset are shown. The choice of offset is difficult to determine *a priori* but can be modified to ensure that the grid is nicely spaced.

![](./examples/images/2i_1d_good_offset.png =250x)
"Two independent against one dependant - good offset choice"

<!-- ![](./examples/images/2i_1d_bad_offset.png "Two independent against one dependant - poor offset choice"  =250x) -->

2_indep_1_dep
-------------

This example shows a carpet plot where two dependant values are plotted against two independent values. The first dependant value is shown on the ordinate axis while a contour of the second dependant variable is superimposed on the grid of iso-lines of x1 and x2. In this plot, the value of x1 and x2 which yeild the desired combinations of the two dependant variables y1 and y2 can be easily identified.


3_indep_1_dep
-------------

The example can be thought of as a series of three 2DOF carpet plots each corresponding to a different constant value of a third independant variable. Since the abissca of the plot is in arbitary units, there is no loss in accuracy by making a arbitrary shift on the abiscca for each plot. However, since the horizontal shift is arbitrary, you cannot interpolate along the third degree of freedome graphically as is possible between the other two independat variables

![](./examples/images/3i_1d.png "Three independent variables against one dependant")

hatched lines
-------------