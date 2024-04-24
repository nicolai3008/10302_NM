import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({
#    "text.usetex": True,
    "font.family": "serif",
    "font.sans-serif": ["Computer Modern Roman"],
    "font.size": 14,
    "font.weight": "bold",
    "legend.fontsize": 12,
    "legend.edgecolor": [0.2, 0.2, 0.2],
    "axes.linewidth": 1.75,
    "axes.titlesize": 20,
#    'text.latex.preamble': r'\boldmath',
    "figure.autolayout": True})
import os
d = np.load('NiI2_2D/data.npz')
E = d["energies"]
E = (E - np.min(E))*10**3
q = d["q"]
del d

# def f(x,y):
#     f = x * np.exp(-x**2 - y**2)
#     return f

def rotM(ang):
    M = np.array([[np.cos(ang/180*np.pi), -np.sin(ang/180*np.pi), 0], 
                  [np.sin(ang/180*np.pi), np.cos(ang/180*np.pi), 0],
                  [0, 0, 1]])
    return M

def reflM(m1, m2):
    M = np.array([[m1, 0, 0], 
                  [0, m2, 0],
                  [0, 0, 1]])
    return M


# qx = []; qy = []; E = []
# for i in np.linspace(0, np.cos(ang/180*np.pi), 10):
#     j = 0
#     while j <= np.tan(ang/180*np.pi)*i:
#         qx.append(i)
#         qy.append(j)
#         E.append(np.exp(-i**2-j**2)*np.sin(j)*np.cos(i*10))
#         j += 0.05
# qx = np.array(qx); qy = np.array(qy); E = np.array(E)


ang = 30
c = np.matmul(rotM(2*ang),np.array([1,0,0]))
for i in range(len(q)):
    q[i,0:2] = np.array([1,0])*q[i,0] + np.array([c[0],c[1]])*q[i,1]
qaE = np.stack((q[:,0], q[:,1], E))
del q, i


qaE = np.matmul(rotM(ang), qaE)
qxO = qaE[0,:]
qyO = qaE[1,:]

qaE = np.concatenate((qaE, np.matmul(reflM(1, -1), qaE)), axis = 1)
qaE = np.concatenate((qaE, np.matmul(reflM(-1, 1), qaE)), axis = 1)

Mtot = np.matmul(rotM(-ang), np.matmul(reflM(-1, 1), rotM(ang)))
qaE = np.concatenate((qaE, np.matmul(Mtot, qaE)), axis = 1)

Mtot = np.matmul(rotM(ang), np.matmul(reflM(-1, 1), rotM(-ang)))
qaE = np.concatenate((qaE, np.matmul(Mtot, qaE)), axis = 1)
del Mtot


qx = qaE[0,:]
qy = qaE[1,:]
E = qaE[2,:]


def dv(ang, m1):
    dv = np.array([m1*np.cos(ang/180*np.pi), 
                   np.sin(ang/180*np.pi),
                   0])*1/2*2
    return dv
            
ang = 30
qaE_new = qaE
qaE_new = np.concatenate((qaE_new, 
                          qaE + np.repeat(np.array([dv(ang, 1)]).T, qaE.shape[1], axis=1)), 
                          axis = 1)
qaE_new = np.concatenate((qaE_new, 
                          qaE + np.repeat(np.array([dv(-ang, 1)]).T, qaE.shape[1], axis=1)), 
                          axis = 1)
qaE_new = np.concatenate((qaE_new, 
                          qaE + np.repeat(np.array([dv(ang, -1)]).T, qaE.shape[1], axis=1)), 
                          axis = 1)
qaE_new = np.concatenate((qaE_new, 
                          qaE + np.repeat(np.array([dv(-ang, -1)]).T, qaE.shape[1], axis=1)), 
                          axis = 1)
qaE_new = np.concatenate((qaE_new, 
                          qaE + np.repeat(np.array([[0, 2*1/2, 0]]).T, qaE.shape[1], axis=1)), 
                          axis = 1)
qaE_new = np.concatenate((qaE_new, 
                          qaE + np.repeat(np.array([[0, -2*1/2, 0]]).T, qaE.shape[1], axis=1)), 
                          axis = 1)
qx_new = qaE_new[0,:]
qy_new = qaE_new[1,:]
E_new = qaE_new[2,:]


G = np.array([1,0])*0 + np.array([c[0],c[1]])*0
M = np.array([1,0,0])*1/2 + np.array([c[0],c[1],0])*0
M = np.matmul(rotM(30), M); M = M[0:2]
K = np.array([1,0,0])*1/3 + np.array([c[0],c[1],0])*1/3
K = np.matmul(rotM(30), K)
del c
HV = np.zeros((3,7))
for i in range(7):
    HV[:,i] = np.matmul(rotM(2*ang*i), K)
K = K[0:2]; HV = HV[0:2,:]

# fig = plt.figure()
# ax = fig.add_subplot()
# ax.plot(qxO, qyO, 'bo', ms=3, zorder = 100, label=r'\textbf{Original data}')
# ax.set_aspect('equal', adjustable='box')
# ax.tricontour(qx, qy, E, levels=60, linewidths=0.1, colors='k')
# cntr2 = ax.tricontourf(qx, qy, E, levels=60, cmap="RdBu_r")
# fig.colorbar(cntr2, ax=ax, fraction=0.0385, pad=0.07)
# #ax.plot(qx, qy, 'ko', ms=3, label=r'\textbf{Symmetry data}', alpha=0.1)
# ax.legend(bbox_to_anchor=(1.05, -0.25), fancybox=False, ncols=2)
# ax.set_title(r'\textbf{Contour plot (First BZ)}', pad=15)
# ax.set_xlabel(r'\unboldmath $q_x$ \textbf{[Å}\boldmath $^{-1}$\textbf{]}', fontsize=18, labelpad=10)
# ax.set_ylabel(r'\unboldmath $q_y$ \textbf{[Å}\boldmath $^{-1}$\textbf{]}', fontsize=18, labelpad=10)
# ax.set_xlim(-0.8,0.8)
# ax.set_ylim(-0.8,0.8)
# fig.set_size_inches(6, 5, forward=True)
# plt.xticks(weight = 'bold')
# plt.show()

fig = plt.figure()
ax = fig.add_subplot()
ax.plot(HV[0,:], HV[1,:], 'k--', linewidth=2)
ax.plot(qxO, qyO, 'go', ms=1, zorder = 99, label=r'\textbf{Original data}')
ax.plot(G[0], G[1], 'ko', ms=8, zorder = 100)
ax.annotate(r'$\Gamma$', (G[0]-0.08, G[1]+0.08), va='top', color='black')
ax.plot(M[0], M[1], 'ko', ms=8, zorder = 100)
ax.annotate(r'$\mathrm{M}$', (M[0]+0.04, M[1]+0.08), va='top', color='black')
ax.plot(K[0], K[1], 'ko', ms=8, zorder = 100)
ax.annotate(r'$\mathrm{K}$', (K[0]+0.04, K[1]+0.08), va='top', color='black')
ax.set_aspect('equal', adjustable='box')
lvls = np.linspace(0, 45, 45*2 + 1)
ax.tricontour(qx_new, qy_new, E_new, extend='max', levels=lvls, linewidths=0.1, colors='k')
cntr2 = ax.tricontourf(qx_new, qy_new, E_new, extend='max', levels=lvls, cmap="seismic")
cb = plt.colorbar(cntr2, ax=ax, fraction=0.0385, pad=0.07, extend='max')
cb.set_label(label=r'\textbf{Energy [meV]}', labelpad=15)
# ax.plot(qx, qy, 'ko', ms=3, label=r'\textbf{Symmetry data}', alpha=0.1)
ax.legend(bbox_to_anchor=(1.25, -0.08), fancybox=False, ncols=2)
# ax.set_title(r'\textbf{Contour plot}', pad=15)
ax.set_xlabel(r'\unboldmath $\tilde{q}_x$ \textbf{[–}\boldmath \textbf{]}', fontsize=18, labelpad=10)
ax.set_ylabel(r'\unboldmath $\tilde{q}_y$ \textbf{[–}\boldmath \textbf{]}', fontsize=18, labelpad=10)
ax.set_xlim(-0.8,0.8)
ax.set_ylim(-0.8,0.8)
fig.set_size_inches(6, 5.5, forward=True)
plt.xticks(weight = 'bold')
plt.show()













#%%

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_trisurf(qx, qy, E, cmap="seismic", linewidth=0)
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()





























