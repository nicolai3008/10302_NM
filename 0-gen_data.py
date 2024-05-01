import numpy as np
import matplotlib.pyplot as plt
import os

Type = "Band"
Type = "Conv_E"
Type = "Conv_V"
Type = "Conv_K"
Type = "2D"


mol = "MnI2"

xyz = "Materials/1{}-1.xyz".format(mol)
if Type == "2D":
    template = "template_2d.py"
else:
    template = "template.py"
with open(template, "r") as file:
    template = file.readlines()
    file.close()

# Check if folder with molecule name exists
if not os.path.exists(mol):
    os.makedirs(mol)

if Type == "Band":
    k = 6
    ecut = 600
    v = 6
    n = 101
    template_copy = template[:]
    template_copy[6] = template_copy[6].replace("ECUT", str(ecut))
    template_copy[7] = template_copy[7].replace("KDENS", str(k))
    template_copy[8] = template_copy[8].replace("VACUUM", str(v))
    template_copy[9] = template_copy[9].replace("FOLDER", "Band")
    template_copy[10] = template_copy[10].replace("TYPE", "Band")
    template_copy[11] = template_copy[11].replace("NPOINTS", str(n))
    template_copy[13] = template_copy[13].replace("XYZ", xyz)
    
    with open("{}/Band.py".format(mol), "w") as file:
        file.writelines(template_copy)
        file.close()
    with open("{}/Band.sh".format(mol), "w") as file:
        file.write("#!/bin/bash\n")
        file.write("mq submit Band.py -R 12:1d\n")
        file.close()

elif Type == "Conv_E":
    if not os.path.exists("{}/Conv_E".format(mol)):
        os.makedirs("{}/Conv_E".format(mol))
    k = 6
    v = 6
    E = np.linspace(50,1000,20)
    n = 31
    for i in range(len(E)):
        template_copy = template[:]
        template_copy[6] = template_copy[6].replace("ECUT", str(E[i]))
        template_copy[7] = template_copy[7].replace("KDENS", str(k))
        template_copy[8] = template_copy[8].replace("VACUUM", str(v))
        template_copy[9] = template_copy[9].replace("FOLDER", "Conv_E/Conv_E_{}".format(E[i]))
        template_copy[10] = template_copy[10].replace("TYPE", "Conv")
        template_copy[11] = template_copy[11].replace("NPOINTS", str(n))
        template_copy[13] = template_copy[13].replace("XYZ", xyz)
        
        with open("{}/Conv_E/Conv_E_{}.py".format(mol,E[i]), "w") as file:
            file.writelines(template_copy)
            file.close()
        with open("{}/Conv_E.sh".format(mol), "a") as file:
            if i == 0:
                file.write("#!/bin/bash\n")
            file.write("mq submit Conv_E/Conv_E_{}.py -R 12:1d\n".format(E[i]))
            file.close()
        
elif Type == "Conv_V":
    if not os.path.exists("{}/Conv_V".format(mol)):
        os.makedirs("{}/Conv_V".format(mol))
    k = 6
    v = np.linspace(1,7,13)
    ec = 600
    n = 31
    for i in range(len(v)):
        template_copy = template[:]
        template_copy[6] = template_copy[6].replace("ECUT", str(ec))
        template_copy[7] = template_copy[7].replace("KDENS", str(k))
        template_copy[8] = template_copy[8].replace("VACUUM", str(v[i]))
        template_copy[9] = template_copy[9].replace("FOLDER", "Conv_V/Conv_V_{}".format(v[i]))
        template_copy[10] = template_copy[10].replace("TYPE", "Conv")
        template_copy[11] = template_copy[11].replace("NPOINTS", str(n))
        template_copy[13] = template_copy[13].replace("XYZ", xyz)
        
        with open("{}/Conv_V/Conv_V_{}.py".format(mol,v[i]), "w") as file:
            file.writelines(template_copy)
            file.close()
        with open("{}/Conv_V.sh".format(mol), "a") as file:
            if i == 0:
                file.write("#!/bin/bash\n")
            file.write("mq submit Conv_V/Conv_V_{}.py -R 12:1d\n".format(v[i]))
            file.close()

elif Type == "Conv_K":
    if not os.path.exists("{}/Conv_K".format(mol)):
        os.makedirs("{}/Conv_K".format(mol))
    k = np.linspace(2,8,13)
    v = 6
    ec = 600
    n = 31
    for i in range(len(k)):
        template_copy = template[:]
        template_copy[6] = template_copy[6].replace("ECUT", str(ec))
        template_copy[7] = template_copy[7].replace("KDENS", str(k[i]))
        template_copy[8] = template_copy[8].replace("VACUUM", str(v))
        template_copy[9] = template_copy[9].replace("FOLDER", "Conv_K/Conv_K_{}".format(k[i]))
        template_copy[10] = template_copy[10].replace("TYPE", "Conv")
        template_copy[11] = template_copy[11].replace("NPOINTS", str(n))
        template_copy[13] = template_copy[13].replace("XYZ", xyz)
        
        with open("{}/Conv_K/Conv_K_{}.py".format(mol,k[i]), "w") as file:
            file.writelines(template_copy)
            file.close()
        with open("{}/Conv_K.sh".format(mol), "a") as file:
            if i == 0:
                file.write("#!/bin/bash\n")
            file.write("mq submit Conv_K/Conv_K_{}.py -R 12:1d\n".format(k[i]))
            file.close()    

elif Type == "2D":
    if not os.path.exists("{}_2D".format(mol)):
        os.makedirs("{}_2D".format(mol))
    k = 6
    v = 6
    E = 600
    n = 31
    h = np.linspace(0,40,41)
    for i in range(len(h)):
        template_copy = template[:]
        template_copy[6] = template_copy[6].replace("ECUT", str(E))
        template_copy[7] = template_copy[7].replace("KDENS", str(k))
        template_copy[8] = template_copy[8].replace("VACUUM", str(v))
        template_copy[9] = template_copy[9].replace("FOLDER", "H_{}".format(h[i]))
        template_copy[10] = template_copy[10].replace("TYPE", "2D")
        template_copy[11] = template_copy[11].replace("NPOINTS", str(n))
        template_copy[13] = template_copy[13].replace("XYZ", xyz)
        template_copy[22] = template_copy[22].replace("HEIGHT", str(h[i]))
        
        with open("{}_2D/H_{}.py".format(mol,h[i]), "w") as file:
            file.writelines(template_copy)
            file.close()
        with open("{}_2D/2D.sh".format(mol), "a") as file:
            if i == 0:
                file.write("#!/bin/bash\n")
            file.write("mq submit H_{}.py -R 12:3d\n".format(h[i]))
            file.close()