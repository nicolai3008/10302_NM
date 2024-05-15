import matplotlib.pyplot as plt 
import numpy as np

# Hexagonal grid of points
nx = 3
ny = 3
d = 1

# Plot the hexagons
fig, ax = plt.subplots()
for i in range(-nx,nx):
    for j in range(-ny,ny):
        plt.plot(i*d-j*d/2,j*d*np.sqrt(3)/2,'o',color='purple',markersize=30, zorder=0)

plt.arrow(0,0,d,0,width=0.05, head_width=0.3, head_length=4.5*0.05, length_includes_head=True, fc='k', ec='k',zorder=1)
plt.arrow(0,0,-d/2,d*np.sqrt(3)/2,width=0.05,  head_width=0.3, head_length=4.5*0.05,length_includes_head=True, fc='k', ec='k',zorder=1)
plt.text(d/2-0.1,0.1,'$\mathbf{a}_1$',fontsize=20)
plt.text(-d/5,d*np.sqrt(3)/2-0.3,'$\mathbf{a}_2$',fontsize=20)
plt.xlim(-1.2,1.2)
plt.ylim(-1,1)
ax.set_aspect('equal')
ax.axis('off')
plt.savefig("Hexagon.png")


# Hexagonal grid of points
nx = 3
ny = 3
d = 1

# Plot the hexagons
fig, ax = plt.subplots()
for i in range(-nx,nx):
    for j in range(-ny,ny):
        plt.plot(np.sqrt(3)/2*d*i,j*d+1/2*d*i,'o',color='red',markersize=30, zorder=0)
epsilon=10**-6
v = np.sqrt(3/36+0.5**2)
x1 = np.linspace(-v,-np.sqrt(3)/6,100)
l1 = (x1+v)*np.sqrt(3)
x2 = np.linspace(np.sqrt(3)/6,v,100)
l2 = -(x2-v)*np.sqrt(3)

plt.arrow(0,0,0,d,width=0.05, head_width=0.3, head_length=4.5*0.05, length_includes_head=True, fc='k', ec='k',zorder=1)
plt.arrow(0,0,d*np.sqrt(3)/2,d/2,width=0.05,  head_width=0.3, head_length=4.5*0.05,length_includes_head=True, fc='k', ec='k',zorder=1)
plt.text(np.sqrt(3)/2-0.2,0,'$\mathbf{b}_1$',fontsize=20)
plt.text(-d/4-0.15,0.85,'$\mathbf{b}_2$',fontsize=20)
plt.plot((-np.sqrt(3)/6,np.sqrt(3)/6),(0.5,0.5),color='k',linewidth=2)
plt.plot((-np.sqrt(3)/6,np.sqrt(3)/6),(-0.5,-0.5),color='k',linewidth=2)
plt.fill_between((-np.sqrt(3)/6,np.sqrt(3)/6),0.5,-0.5,color='red',alpha=0.1,edgecolor="none")
plt.plot((-v,-np.sqrt(3)/6),(0,0.5),color='k',linewidth=2)
plt.plot((-v,-np.sqrt(3)/6),(0,-0.5),color='k',linewidth=2)
plt.fill_between(x1,0,l1,color='red',alpha=0.1,edgecolor="none")
plt.fill_between(x1,0,-l1,color='red',alpha=0.1,edgecolor="none")
plt.plot((np.sqrt(3)/6,v),(0.5,0),color='k',linewidth=2)
plt.plot((np.sqrt(3)/6,v),(-0.5,0),color='k',linewidth=2)
plt.fill_between(x2,0,l2,color='red',alpha=0.1,edgecolor="none")
plt.fill_between(x2,0,-l2,color='red',alpha=0.1,edgecolor="none")
plt.ylim(-1.2,1.2)
plt.xlim(-1,1)
ax.set_aspect('equal')
ax.axis('off')
plt.savefig("Hexagon_BZ.png")


fig, ax = plt.subplots()
for i in range(-nx,nx):
    for j in range(-ny,ny):
        plt.plot(np.sqrt(3)/2*d*i,j*d+1/2*d*i,'o',color='red',markersize=30, zorder=0)
epsilon=10**-6
plt.plot((-np.sqrt(3)/6,np.sqrt(3)/6),(0.5,0.5),color='k',linewidth=2)
plt.plot((-np.sqrt(3)/6,np.sqrt(3)/6),(-0.5,-0.5),color='k',linewidth=2)
plt.fill_between((-np.sqrt(3)/6,np.sqrt(3)/6),0.5,-0.5,color='red',alpha=0.1,edgecolor="none")
plt.plot((-v,-np.sqrt(3)/6),(0,0.5),color='k',linewidth=2)
plt.plot((-v,-np.sqrt(3)/6),(0,-0.5),color='k',linewidth=2)
plt.fill_between(x1,0,l1,color='red',alpha=0.1,edgecolor="none")
plt.fill_between(x1,0,-l1,color='red',alpha=0.1,edgecolor="none")
plt.plot((np.sqrt(3)/6,v),(0.5,0),color='k',linewidth=2)
plt.plot((np.sqrt(3)/6,v),(-0.5,0),color='k',linewidth=2)
plt.fill_between(x2,0,l2,color='red',alpha=0.1,edgecolor="none")
plt.fill_between(x2,0,-l2,color='red',alpha=0.1,edgecolor="none")
plt.plot(d*np.sqrt(3)/4,d/4,'o',color='k',markersize=15, zorder=3)
plt.text(d*np.sqrt(3)/4+0.1,d/4-0.1,'$M$',fontsize=20)
plt.plot(0,0,'o',color='k',markersize=15, zorder=3)
plt.text(-0.1,-0.1,'$\Gamma$',fontsize=20)
plt.plot(np.sqrt(3)/6,0.5,'o',color='k',markersize=15, zorder=3)
plt.text(np.sqrt(3)/6+0.1,0.5+0.1,'$K$',fontsize=20)
plt.ylim(-1.2,1.2)
plt.xlim(-1,1)
ax.set_aspect('equal')
ax.axis('off')
plt.savefig("Hexagon_BZ_High.png")