import numpy as np
import pylab as plt

a = np.loadtxt('../spiral/soc_energies.dat')
plt.plot(a[:, 0], a[:, 3] - a[:, 1], '-', label='spiral - proj')
plt.plot([a[0, 0], a[-1, 0]], 2 * [0.0], '--', c='0.5')

a = np.loadtxt('../spiral/soc_energies_full.dat')
plt.plot(a[:, 0], a[:, 3] - a[:, 1], '-', label='spiral - full')
plt.plot([a[0, 0], a[-1, 0]], 2 * [0.0], '--', c='0.5')

a = np.loadtxt('soc_energies.dat')
plt.plot(a[:, 0] / 3, (a[:, 3] - a[:, 1]) / 3, '-', label='SC - proj')

a = np.loadtxt('soc_energies_full.dat')
plt.plot(a[:, 0] / 3, (a[:, 3] - a[:, 1]) / 3, '-', label='SC - full')

plt.legend()
plt.xlabel('Number of bands per formula unit')
plt.ylabel('E_z - E_x [meV per formula unit]')
plt.show()
