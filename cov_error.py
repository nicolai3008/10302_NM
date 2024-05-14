import numpy as np
import os

folder = "VBr2"
subs = ["Conv_E","Conv_K", "Conv_V"]
maxes = [[800.0,1000],[7.5,8],[6.5,7]]

print(f"Results for {folder}")
for i, sub in enumerate(subs):
    print(f"Results for {sub}")
    sub_folder = os.path.join(folder,sub)
    files = os.listdir(sub_folder)
    # remove .py files
    files = [f for f in files if ".py" not in f]
    # sort files by number
    a = [f for f in files if str(maxes[i][0]) in f][0].strip()
    b = [f for f in files if str(maxes[i][1]) in f][0].strip()
    a = np.load(os.path.join(sub_folder,a))
    b = np.load(os.path.join(sub_folder,b))
    avg_er = (np.sum(b["energies"] - a["energies"])/len(a["energies"]))*1000
    m_er = (b["energies"][10] - a["energies"][10])*1000
    k_er = (b["energies"][16] - a["energies"][16])*1000
    print(f"Average Energy Error: {avg_er}")
    print(f"Energy Error at M: {m_er}")
    print(f"Energy Error at K: {k_er}")