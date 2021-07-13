import os
from shutil import copyfile


dataset_path = 'E:\\TESI\\TESI_LAMBONI_VIVIANA\\DATASET\\'
base_path = 'E:\\TESI\\TESI_LAMBONI_VIVIANA\\RISORSE_ESTERNE\\DATASET_ESTERNI\\CFD\\Images'

entries = os.scandir(base_path)
for en in entries:
    if en.is_dir():
        sub = os.scandir(base_path + '\\' + en.name)
        for s in sub:
            if s.is_dir():
                files =  os.scandir(base_path + '\\' + en.name + '\\' + s.name)
                for f in files:
                    src = base_path + '\\' + en.name + '\\' + s.name + '\\' + f.name
                    if f.is_file() and ("-N.jpg" in f.name):
                        copyfile(src, dataset_path + '\\INTEREST\\CFD' + '\\' + f.name)
                    elif f.is_file() and ("-A.jpg" in f.name):
                        copyfile(src, dataset_path + '\\FRUSTRATION\\CFD' + '\\' + f.name)
