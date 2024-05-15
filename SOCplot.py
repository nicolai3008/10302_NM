import numpy as np
import matplotlib as mpl
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
os.chdir('NiI2_Supercell_Ferro')
d = np.load('pso_data.npz')
e = d["soc"]
e = (e - np.min(e))*10**3
theta = d["theta"]
phi =d["phi"]
del d

material = r'$\mathrm{NiI_2}$'

cvals  = [-2, -1.65, 0, 1.65, 2.0]
colors = ["darkred", "red", "white", "blue", "darkblue"]
norm=plt.Normalize(min(cvals),max(cvals))
tuples = list(zip(map(norm,cvals), colors))
cmap = mpl.colors.LinearSegmentedColormap.from_list("", tuples)


fig = plt.figure()
ax = fig.add_subplot()
lvls = np.linspace(0, np.max(e), 50)
ax.tricontour(theta, phi, e, levels=lvls, linewidths=0.1, colors='white')
cntr2 = ax.tricontourf(theta, phi, e, levels=lvls, cmap=cmap)
#cb = plt.colorbar(cntr2, ax=ax, fraction=0.0385, pad=0.07, format='%.3f')
#cb.set_label(label=r'\unboldmath $E_{\mathrm{PSO}}$ \textbf{[meV]}', labelpad=15)
ax.scatter(theta[np.argmax(e)]-180, phi[np.argmax(e)], color='white', s=50)
# ax.scatter(theta[e <= 1*10**(-3)], phi[e <= 1*10**(-3)], color='gray', s=50)
ax.scatter(theta[np.argmin(e)]-180, phi[np.argmin(e)], color='k', s=50)
ax.set_xlabel(r'\unboldmath $\theta$ \textbf{[deg.]}', fontsize=18, labelpad=10)
ax.set_ylabel(r'\unboldmath $\phi$ \textbf{[deg.]}', fontsize=18, labelpad=10)
ax.set_title(r'\textbf{PSO \unboldmath $(\theta,\phi)$-space:} '+material, pad=15)
ax.set_xlim(0, 90)
ax.set_ylim(0, 360)
fig.set_size_inches(6*0.8, 5.5*0.8, forward=True)
plt.savefig('PSO_2D.png', dpi=300, bbox_inches='tight')
plt.close(fig)

def sph2cart(r, theta, phi):
    return [
         r * np.sin(theta) * np.cos(phi),
         r * np.sin(theta) * np.sin(phi),
         r * np.cos(theta)
    ]
r = sph2cart(1, theta/180*np.pi, phi/180*np.pi)
x = r[0]; y = r[1]; z = r[2]
#x = np.concatenate((x, -x)); y = np.concatenate((y, -y)); z = np.concatenate((z, -z)); e = np.concatenate((e, e))
del r



fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
norm = mpl.colors.BoundaryNorm(lvls, cmap.N)
sc = ax.scatter(x, y, z, c=e, cmap=cmap, norm=norm)
cb = fig.colorbar(sc, ax=ax, fraction=0.0405, pad=0.15, format='%.3f')
cb.set_label(label=r'\unboldmath $E_{\mathrm{PSO}}$ \textbf{[meV]}', labelpad=15)
ax.set_aspect('equal', adjustable='box')
ax.set_xlabel(r'\unboldmath $\hat{n}_x$ \textbf{[–]}', fontsize=18, labelpad=10)
ax.set_ylabel(r'\unboldmath $\hat{n}_y$ \textbf{[–]}', fontsize=18, labelpad=10)
ax.set_zlabel(r'\unboldmath $\hat{n}_z$ \textbf{[–]}', fontsize=18, labelpad=10)
ax.set_title(r'\textbf{PSO 3D:} '+material, pad=15)
ax.set_xlim(-1.1, 1.1)
ax.set_ylim(-1.1, 1.1)
ax.set_zlim(-1.1, 1.1)
fig.set_size_inches(6, 5.5, forward=True)
plt.savefig('PSO_3D.png', dpi=300, bbox_inches='tight')






#%%


print(np.max(e)/3)

print(theta[np.argmin(e)]-180, phi[np.argmin(e)])
print(theta[np.argmin(e)], phi[np.argmin(e)])

print(theta[np.argmax(e)]-180, phi[np.argmax(e)])
print(theta[np.argmax(e)], phi[np.argmax(e)])













