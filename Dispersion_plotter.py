import matplotlib.pyplot as plt
import numpy as np

# Plot the energy bands from E and q

folder = 'MnI2'
data = np.load(f'{folder}/data.npz')
energies = data['energies']*1000
energies = energies - energies[0]
q = data['q']
magmoms = data['magmoms']

normal_ticks = [0]
g = 1

for i, q_c in enumerate(q):
    if i == 0:
        continue
    if q_c[1] - q[i-1][1] > 1e-6 and g ==1:
        normal_ticks.append(i-1)
        g = 2
    if q_c[1] - q[i-1][1] < 1e-6 and g == 2:
        normal_ticks.append(i-1)
        g = 3

normal_ticks.append(len(q)-1)
label_ticks = ['$\Gamma$', 'M', 'K', '$\Gamma$']

plt.axhline(y=0, ls='--', color='k')
plt.plot(energies, 'r-')
plt.xlim(normal_ticks[0], normal_ticks[-1])
plt.xticks(normal_ticks, label_ticks)
plt.grid(axis='x')
plt.ylabel("Energy - $E_F$ [meV]")
plt.savefig(f'{folder}-bands.png')
plt.show()
# Plot the energy bands along high symmetry lines
