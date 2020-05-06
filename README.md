# martini_vesicle
A quick and dirty script to generate a Martini Lipids vesicle.

Example:
vesicle.py 50 800 1000 > 50nm_vesicle.pdb

This will write a PDB containing 800 lipids in the inner leaflet
and 1000 lipids in the outer leaflet. The vesicle will have a 
radius of 50 nm. The specific lipid can be changed by altering
the marked section in the script. In general it looks very much
like insane. By default POPC is used.

Original author: T.A. Wassenaar (2019)
Adapted by: B.M.H. Bruininks (2020)
