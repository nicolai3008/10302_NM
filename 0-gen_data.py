import numpy as np
import matplotlib.pyplot as plt
import os

mol = "VBr2"

xyz = "Materials/1{}-1.xyz".format(mol)
template = "template.py"
with open(template, "r") as file:
    template = file.readlines()
    file.close()

# Check if folder with molecule name exists
if not os.path.exists(mol):
    os.makedirs(mol)

Type = "Band"
# Type = "Conv_E"
# Type = "Conv_V"
# Type = "Conv_K"
# Type = "2D"

if Type == "Band":
    k = 6
    ecut = 600
    v = 6
    
    

