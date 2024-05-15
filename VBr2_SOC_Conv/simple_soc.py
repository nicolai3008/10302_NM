import numpy as np
from gpaw.occupations import create_occ_calc
from gpaw.spinorbit import soc_eigenstates
from gpaw.new.ase_interface import GPAW


calc = GPAW('gs_nc_nosoc_xy_n126.gpw')
occcalc = create_occ_calc({'name': 'fermi-dirac', 'width': 0.001})

for n2 in range(84, 252, 2):

    Es = []
    for theta, phi in zip([0, 90, 90], [0, 0, 90]):
        soc = soc_eigenstates(calc=calc, projected=True, theta=theta, phi=phi, n2=n2,
                              occcalc=occcalc).calculate_band_energy()
        Es.append(soc)

    Es = np.array(Es) * 1000
    fd = open('soc_energies.dat', 'a')
    print(n2, Es[0], Es[1], Es[2], file=fd)
    fd.close()
    #print('Projected: (z,x,y)')
    #print(Es - np.min(Es))
    #print()

#Es = []
#for theta, phi in zip([0, 90, 90], [0, 0, 90]):
#    soc = soc_eigenstates(calc=calc, projected=False, theta=theta, phi=phi, n2=n2,
#                             occcalc=occcalc).calculate_band_energy()
#    Es.append(soc)

#Es = np.array(Es) * 1000
#print('Full: (z,x,y)')
#print(Es - np.min(Es))
