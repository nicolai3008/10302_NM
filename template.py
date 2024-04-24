from ase.build import mx2
from ase.io import read
from ase.visualize import view
from gpaw.new.ase_interface import GPAW
import numpy as np
import os
ecut = float("ECUT")
k = float("KDENS")
v = float("VACUUM")
folder = "FOLDER"
type = "TYPE"
n = int("NPOINTS")

atoms = read("../"+"XYZ")
MM = atoms.get_magnetic_moments()
atoms.set_initial_magnetic_moments(MM)
atoms.center(vacuum=v, axis=2)

# Align the magnetic moment in the xy-plane
magmoms = [[MM[0], 0, 0], [MM[1], 0, 0], [MM[2], 0, 0]]
energies_q = []
magmoms_q = []
q = []
# Construct list of q-vectors
path = atoms.cell.bandpath('GMKG', npoints=n).kpts
print('Calculating ground state')
print(len(path), "q-points in the path")
print("=====================================")

if type == "Band":
    os.makedirs(folder, exist_ok=True)
    for i, q_c in enumerate(path):
        print(f'Calculating q={q_c}')
        q.append(q_c)
        # Spin-spiral calculations require non-collinear calculations
        # without symmetry or spin-orbit coupling
        calc = GPAW(mode={'name': 'pw',
                        'ecut': ecut,
                        'qspiral': q_c},
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
                    txt=f'{folder}/gsq-{i:02}.txt')
        atoms.calc = calc
        energy = atoms.get_potential_energy()
        calc.write(f'{folder}/gsq-{i:02}.gpw')
        magmom = atoms.calc.get_magnetic_moment()
        energies_q.append(energy)
        magmoms_q.append(magmom)
        print(f'Energy: {energy} eV')
        print(f'Magnetic moment: {magmom} Bohr magnetons')

    energies_q = np.array(energies_q)
    magmoms_q = np.array(magmoms_q)
    q = np.array(q)
    np.savez('data_{}_{}_{}.npz'.format(ecut,k,v), energies=energies_q, magmoms=magmoms_q, q=q)

elif type == "Conv":
    p = folder.split('/')
    os.chdir(p[0])
    os.makedirs(p[1], exist_ok=True)
    os.chdir("..")
    for i, q_c in enumerate(path):
        print(f'Calculating q={q_c}')
        q.append(q_c)
        # Spin-spiral calculations require non-collinear calculations
        # without symmetry or spin-orbit coupling
        calc = GPAW(mode={'name': 'pw',
                        'ecut': ecut,
                        'qspiral': q_c},
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
                    txt=f'{folder}/gsq-{i:02}.txt')
        atoms.calc = calc
        energy = atoms.get_potential_energy()
        calc.write(f'{folder}/gsq-{i:02}.gpw')
        magmom = atoms.calc.get_magnetic_moment()
        energies_q.append(energy)
        magmoms_q.append(magmom)
        print(f'Energy: {energy} eV')
        print(f'Magnetic moment: {magmom} Bohr magnetons')

    energies_q = np.array(energies_q)
    magmoms_q = np.array(magmoms_q)
    q = np.array(q)
    np.savez('{}/data_{}_{}_{}.npz'.format(p[0],ecut,k,v), energies=energies_q, magmoms=magmoms_q, q=q)
