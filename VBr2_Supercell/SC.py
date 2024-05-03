from ase.build import mx2
from ase.build.supercells import make_supercell
from ase.io import read
from ase.visualize import view
from gpaw.new.ase_interface import GPAW
import numpy as np
import os
import ast


ecut = float("600")
k = float("6")
v = float("6")
folder = "SC"
type = "Band"
n = int("101")

atoms = read("../"+"Materials/1VBr2-1.xyz")
M = [[2,1,0],[1,2,0],[0,0,1]]
# Create supercell for MnI2
sc = make_supercell(atoms,M)
sc.center(vacuum=v, axis=2)


energies = np.load('../VBr2/data_600_6.0_6.0.npz')['energies']
minimum = np.argmin(energies)
calc = GPAW(f'../VBr2/Band/gsq-{minimum:02}.gpw')
with open(f'../VBr2/Band/gsq-{minimum:02}.txt') as f:
    lines = f.readlines()
    f.close()
for i, line in enumerate(lines):
    if "total magnetic moment" in line:
        m = line.split(":")[-1].strip(" []\n").split(", ")
        m = [float(x) for x in m]
    if "local magnetic moment" in line:
        m = lines[i+1][:-10].strip()
        MAG = ast.literal_eval(m)
print(MAG)
MM = [MAG[0], 0, 0,MAG[0], 0, 0,MAG[0], 0, 0]
sc.set_initial_magnetic_moments(MM)

# Align the magnetic moment in the xy-plane
magmoms = [MAG, [0, 0, 0], [0, 0, 0],[MAG[0]*np.cos(np.deg2rad(120)),MAG[0]*np.sin(np.deg2rad(120)),0], [0, 0, 0], [0, 0, 0],[MAG[0]*np.cos(np.deg2rad(120)),-MAG[0]*np.sin(np.deg2rad(120)),0], [0, 0, 0], [0, 0, 0]]


os.makedirs(folder, exist_ok=True)
calc = GPAW(mode={'name': 'pw',
        'ecut': ecut},
        xc='LDA',
        mixer={'backend': 'pulay',
            'beta': 0.05,
            'method': 'sum',
            'nmaxold': 5,
            'weight': 100},
        symmetry='off',
        parallel={'domain': 1, 'band': 1},
        magmoms=magmoms,
        kpts={'density': k, 'gamma': True},
        txt=f'{folder}/gsq-sc.txt')
sc.calc = calc
energy = sc.get_potential_energy()
calc.write(f'{folder}/gsq-sc.gpw')
magmom = sc.calc.get_magnetic_moment()
print(f'Energy: {energy} eV')
print(f'Magnetic moment: {magmom} Bohr magnetons')

energies_q = np.array(energy)
magmoms_q = np.array(magmom)
q = np.array([1/3,1/3,0])
np.savez('data_{}_{}_{}.npz'.format(ecut,k,v), energies=energies_q, magmoms=magmoms_q, q=q)
