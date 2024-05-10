import numpy as np
import matplotlib.pyplot as plt

# Take all numpy data files and combine them into a single file

folder = "NiI2_2D"
n = 41

energies = []
q = []
magmoms = []

for i in range(n):
    data = np.load(f'{folder}/data_{i}.npz')
    en = data['energies']
    qn = data['q']
    mn = data['magmoms']
    # Concat the data from each file, flatten the arrays
    energies.extend(en)
    q.extend(qn)
    magmoms.extend(mn)

# Save the data to a single file
np.savez(f'{folder}/data.npz', energies=energies, q=q, magmoms=magmoms)