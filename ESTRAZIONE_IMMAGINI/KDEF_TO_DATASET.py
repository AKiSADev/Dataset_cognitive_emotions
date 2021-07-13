import os
from shutil import copyfile


dataset_path = 'E:\\TESI\\TESI_LAMBONI_VIVIANA\\DATASET\\INTEREST\\KDEF'
base_path = 'E:\\TESI\\TESI_LAMBONI_VIVIANA\\RISORSE_ESTERNE\\DATASET_ESTERNI\\KDEF\\KDEF'

entries = os.scandir(base_path)
for en in entries:
    files = os.scandir(base_path + '\\' + en.name)
    for f in files:
        if f.is_file() and ("NES.JPG" in f.name):
            src = base_path + '\\' + en.name + '\\' + f.name
            copyfile(src, dataset_path + '\\' + f.name)

