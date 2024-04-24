from ase.build import mx2
from gpaw.new.ase_interface import GPAW
import numpy as np
from ase.io import read, write

atoms = read('NiI2.xyz')
MM = atoms.get_magnetic_moments()
atoms.set_initial_magnetic_moments([(MM[0]), (MM[1]), (MM[2])])
MM = atoms.get_initial_magnetic_moments()

# Align the magnetic moment in the xy-plane
magmoms = [[MM[0], 0, 0], [MM[1], 0, 0], [MM[2], 0, 0]]
print(magmoms)

#cell = atoms.get_cell()
#atoms.set_cell([cell[0], cell[1], [0, 0, 10]])
#atoms.set_pbc((True, True, True))
#atoms.center(vacuum=3, axis=2)
#m = atoms.get_magnetic_moments()







