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
os.chdir('VBr2_SOC_Conv')

# Plot the energy bands from E and q
# Plot the energy bands along high symmetry lines

names = ["", "_ss", "_full"]
act_names = ["SC PSO", "GBT PSO", "SC FSOC"]
order = [1, 0, 2]
factor = [3, 1, 3]
fig = plt.figure()
ax = fig.add_subplot()
e_min = 0
e_max = 0

for i in order:
    data = np.loadtxt("soc_energies{}.dat".format(names[i]),delimiter=" ")
    n = data[:,0]/factor[i]
    e_z = data[:,1]
    e_x = data[:,2]
    e_y = data[:,3]
    e = (e_x-e_z)/factor[i]
    if max(e) > e_max:
        e_max = max(e)
    if min(e) < e_min:
        e_min = min(e)
    ax.plot(n,e, label=act_names[i])

ax.set_title(r"\textbf{SOC band convergence:} $\mathrm{VBr_2}$", pad=15)
ax.set_xlabel("Number of bands per formula unit", labelpad=10)
ax.set_ylabel(r"\unboldmath $E_{x}^\mathrm{SOC}-E_{z}^\mathrm{SOC}$ \textbf{[meV]}")
ax.vlines([35,41],e_min,e_max,linestyles='dashed',colors='k')
ax.set_xticks(range(25,225,25))
ax.set_yticks(np.arange(-0.2,0.6,0.1))
ax.legend()
ax.grid()
fig.set_size_inches(6, 5.0, forward=True)
plt.savefig("soc_energies.svg", dpi=1200)

