import numpy as np
import matplotlib.pyplot as plt

folder = "NiI2"
data = np.load(f'{folder}/data.npz')
energies = data['energies']*1000
energies = energies - energies[0]
q = data['q']
print(q[0])

q = q[:,0:2]
magmoms = data['magmoms']

# 2D plot of points
plt.figure(1)
plt.scatter(q[:,0], q[:,1], c=energies, cmap='viridis')
plt.colorbar(label='Energy - $E_F$ [meV]')
plt.xlabel('q1')
plt.ylabel('q2')
plt.savefig(f'2D.png')

q_n = q

folder = "NiI2_2D"
data = np.load(f'{folder}/data.npz')
energies = data['energies']*1000
energies = energies - energies[0]
q = data['q']
q = q[:,0:2]
magmoms = data['magmoms']

# 2D plot of points
plt.figure(2)
plt.scatter(q[:,0], q[:,1], c=energies, cmap='viridis')
plt.scatter(q_n[:,0], q_n[:,1], c='k')
plt.colorbar(label='Energy - $E_F$ [meV]')
plt.xlabel('q1')
plt.ylabel('q2')

plt.savefig(f'2D_2.png')