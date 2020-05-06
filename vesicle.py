#!/usr/bin/env python3
# This a quick and dirty Insane style vesicle builder for Martini lipid
#  system. This quick adaptation was made by T.A. Wassenaar (2019) Small
#  adapatations mainly regarding readability were made by B.M.H. Bruininks. 

import numpy as np

THICK = 4 # Membrane thickness in nanometers.
CONST = 2.3999632297286531 # Area mismatch inner/outer ratio for spheres. 

############### Changing the lipids is pretty hard coded ##################
# This goes for any ..[PO][PO] lipid... Just change the topology.
# Lipid definition.
POPC = "NC3 PO4 GL1 GL2 C1A D2A C3A C4A C1B C2B C3B C4B".split()
# Z-heights of the individual beads.
Z = np.array([  6,  5,  4,  4,  3,  2,  1,  0,  3,  2,  1,  0]) * 2.0 / 7
# A PDB description line for said lipid
pdbline = "ATOM  {:5}  {:3} POPC {:4}    {:8.3f}{:8.3f}{:8.3f}  1.00  0.00"
###########################################################################

# No changes need to be made in this section.
def _point(y, phi):
    r = np.sqrt(1-y*y)
    return np.cos(phi)*r, y, np.sin(phi)*r


def points_on_sphere(n):
    return np.array([_point((2.*k+1)/n-1, k*CONST) for k in range(n)])


def vesicle(radius, inner, outer):
    # inner 
    pos = radius - 0.1 - Z + np.random.random(12)/10
    lip = list(zip(POPC, pos))

    atom = 1
    res = 1
    for xyz in points_on_sphere(inner):
        for a, r in lip:
            x,y,z = r*xyz
            print(pdbline.format(atom, a, res, x, y, z))
            atom += 1
        res += 1

    # outer 
    pos = radius + 0.1 + Z + np.random.random(12)/10
    lip = list(zip(POPC, pos))

    atom = 1
    res = 1
    for xyz in points_on_sphere(outer):
        for a, r in lip:
            x,y,z = r*xyz
            print(pdbline.format(atom, a, res, x, y, z))
            atom += 1
        res += 1

def main(argv=None):
    """
    Generates a vesicle of given size (float), with the given amount of lipids
    in the inner and outer leaflet (int).
    """
    if len(argv) < 3:
        message = ('\nPlease specify the radius (nm), and the amount of lipids in '
                   'the inner and outer leaflet.\n'
                   'Example: vesicle.py 50 800 1000 > 50nm_vesicle.pdb\n')
        print(message)
        return 1
    radius = float(argv[1])
    inner = int(argv[2])
    outer = int(argv[3])

    vesicle(radius, inner, outer)

    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main(sys.argv))
