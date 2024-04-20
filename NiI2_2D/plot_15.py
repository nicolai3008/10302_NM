from ase.build import mx2
from gpaw.new.ase_interface import GPAW
import numpy as np

atoms = mx2('NiI2', kind='1T', a=4.166,
            thickness=3.027146598949815, vacuum=4)

# Align the magnetic moment in the xy-plane
magmoms = [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
ecut = 600
k = 6

# Construct list of q-vectors
h = 15
path1 = np.linspace(0,1/3,21)
path2 = np.linspace(1/3,0.5,11)
path2 = path2[1:]
path = np.concatenate((path1,path2))
diagonal1 = np.linspace(0,1/3,21)
diagonal2 = np.linspace(1/3,0,11)
diagonal2 = diagonal2[1:]
diagonal = np.concatenate((diagonal1,diagonal2))
idx =[]
for i in range(len(diagonal)):
    if diagonal[h] <= diagonal[i]:
        idx.append(i)
       
p = []
for i in range(len(idx)):
    p.append([path[idx[i]],diagonal[h],0]) 

path = p
energies_q = []
magmoms_q = []
q = []

print('Calculating ground state')
print(len(path), "q-points in the path")
print("=====================================")

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
                kpts={'density': 6.0, 'gamma': True},
                txt=f'gsq-{h}-{i:02}.txt')
    atoms.calc = calc
    energy = atoms.get_potential_energy()
    calc.write(f'gsq-{h}-{i:02}.gpw')
    magmom = atoms.calc.get_magnetic_moment()
    energies_q.append(energy)
    magmoms_q.append(magmom)
    print(f'Energy: {energy} eV')
    print(f'Magnetic moment: {magmom} Bohr magnetons')

energies_q = np.array(energies_q)
magmoms_q = np.array(magmoms_q)
q = np.array(q)
np.savez(f'data_{h}.npz', energies=energies_q, magmoms=magmoms_q, q=q)
