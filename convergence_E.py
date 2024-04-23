import numpy as np
import matplotlib.pyplot as plt

# Check for convergence when changing parameter

folder = "MnI2/E_con"
var = [100,200,300,400,500,600,700,800,900,1000]
e = []

for i in var:
    print(i)
    data = np.load(f'{folder}/data.{i}.npz')
    energies = data['energies']*1000
    energies = energies - energies[0]
    q = data['q']
    magmoms = data['magmoms']
    e.append(energies)
    plt.plot(energies, label=f'E-cut off = {i}')

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
plt.xlim(normal_ticks[0], normal_ticks[-1])
plt.xticks(normal_ticks, label_ticks)
plt.grid(axis='x')
plt.ylabel("Energy - $E_F$ [meV]")
plt.legend()
plt.savefig(f'Convergence-kpoints_E.png')

e = np.array(e)
e = e - e[4]
plt.figure(2)
plt.plot(var, e[:,normal_ticks[0]], label='$\Gamma$')
plt.plot(var, e[:,normal_ticks[1]], label='M')
plt.plot(var, e[:,normal_ticks[2]], label='K')
plt.plot(var, e[:,normal_ticks[3]], label='$\Gamma$')
plt.xlabel('E-cut off [eV]')
plt.ylabel('Energy - $E_F$ [meV]')
plt.legend()
plt.grid()
plt.title('Convergence with k-points compared to $k=6$')
plt.savefig('Convergence-kpoints-2_E.png')
