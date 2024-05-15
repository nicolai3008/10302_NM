import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.sans-serif": ["Computer Modern Roman"],
    "font.size": 14,
    "font.weight": "bold",
    "legend.fontsize": 12,
    "legend.edgecolor": [0.2, 0.2, 0.2],
    "axes.linewidth": 1.75,
    "axes.titlesize": 20,
    'text.latex.preamble': r'\boldmath',
    "figure.autolayout": True})
import os
os.chdir('VBr2')

# Plot the energy bands from E and q
# Plot the energy bands along high symmetry lines

material = r'$\mathrm{NiI_2}$'
data = np.load('data_800.0_8.0_6.0.npz')
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
label_ticks = [r'$\Gamma$', r'$\mathrm{M}$', r'$\mathrm{K}$', r'$\Gamma$']


fig = plt.figure()
ax = fig.add_subplot()
ax.hlines(y=0, xmin=0, xmax=len(q)-1, ls='--', color='k', zorder=120)
ax.hlines(y=np.min(energies), xmin=0, xmax=np.argmin(energies), ls='--', color='blue')
ax.plot(energies, 'k-', linewidth=2, zorder = 99)
ax.grid(axis='y')
#ax.text(0.225, 0.55, r'\unboldmath $\min{{E_{{\mathbf{{q}}}} - E_{{\Gamma}}}} = {Emin}$ meV'.format(Emin=round(np.min(energies),2)), transform=ax.transAxes, fontsize=14, verticalalignment='top')
ax.text(0.420, 0.100, r'\unboldmath ${Emin}$ meV'.format(Emin=round(np.min(energies),3)), transform=ax.transAxes, fontsize=14, verticalalignment='top', color='blue')
ax.set_title(r'\textbf{Spin spiral dispersion:} '+material, pad=15)
ax.set_ylabel(r'\unboldmath $E_{\mathbf{q}} - E_{\Gamma}$ \textbf{[meV]}', fontsize=18, labelpad=10)
ax.set_xlim(normal_ticks[0], normal_ticks[-1])
ax.set_xticks(normal_ticks, label_ticks)
ax.set_ylim(ax.get_ylim())
ax.vlines(x=normal_ticks[1:3], ymin=ax.get_ylim()[0], ymax=ax.get_ylim()[1], color='k', linewidth=2, linestyle='dotted')
#ax.set_ylim(-1, 1)
fig.set_size_inches(6, 5.0, forward=True)
plt.show()



#%%
q[np.argmin(energies)]

import scipy
scipy.signal.find_peaks(-energies)
q[15,0:2]
q[57,0:2]
q[83,0:2]
energies[15]