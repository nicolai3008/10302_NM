import numpy as np

folders = ["NiI2", "MnI2", "VBr2"]

for folder in folders:
    energies = np.load(f'{folder}/data_800.0_8.0_6.0.npz')['energies']
    minimum = np.argmin(energies)
    
    print((energies[0]-energies[minimum])*1000)