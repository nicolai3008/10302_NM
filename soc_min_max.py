import numpy as np

mat = "VBr2"

folder = mat+"_Supercell_Ferro"
data = np.load("{}/pso_data.npz".format(folder))
energies = data["soc"]
phi = data["phi"]
theta = data["theta"]

minimum = np.argmin(energies)
maximum = np.argmax(energies)
e_min = energies[minimum]
e_max = energies[maximum]
phi_min = phi[minimum]
theta_min = theta[minimum]
phi_max = phi[maximum]
theta_max = theta[maximum]

print("Energy Difference for {}:".format(mat))
print("Minimum Energy: {} at theta = {} and phi = {}".format(e_min, theta_min, phi_min))
print("Maximum Energy: {} at theta = {} and phi = {}".format(e_max, theta_max, phi_max))
print("Energy Difference: {:.4}meV".format((e_max - e_min)*1000))
