import os
from shutil import copyfile
import random
from os.path import isfile, join

dataset_balanced = 'E:\\TESI\\TESI_LAMBONI_VIVIANA\\DATASET_FINALE_BALANCED'
dataset_balanced_divided = 'E:\\TESI\\TESI_LAMBONI_VIVIANA\\DATASET_FINALE_BALANCED_SPLITTED_RANDOM_CORRECTED'

emotions = [
    'BOREDOM',
    'CONFUSION',
    'ENTHUSIASM',
    'FRUSTRATION',
    'INTEREST',
    'NEUTRAL',
    'SURPRISE'
    ]

directs = [
    'TRAIN',
    'TEST',
    'VALIDATION'
]


for d in directs:
    for em in emotions:
        dir = dataset_balanced_divided + '\\' + d + '\\'+ em + '\\'
        if not os.path.isdir(dir):
            os.makedirs(dir)

for em in emotions:
    files = os.listdir(dataset_balanced + '\\' + em)

    tot_files = len(files)
    n_test = int(tot_files * 0.2)
    n_val = int((tot_files - n_test) * 0.2)

    print(tot_files)
    print(n_test)
    print(n_val)

    count = 0
    while count <= n_test:
        file = random.randint(0, len(files) - 1)
        source = dataset_balanced + '\\' + em + "\\" + files[file]
        dst = dataset_balanced_divided + '\\' + directs[1] + '\\' + em + '\\' + files[file]
        copyfile(source, dst)
        del files[file]
        count += 1
    
    count = 0
    while count <= n_val:
        file = random.randint(0, len(files)- 1)
        source = dataset_balanced + '\\' + em + "\\" + files[file]
        dst = dataset_balanced_divided + '\\' + directs[2] + '\\' + em + '\\' + files[file]
        copyfile(source, dst)
        del files[file]
        count += 1
    
    for f in files:
        source = dataset_balanced + '\\' + em + "\\" + f
        dst = dataset_balanced_divided + '\\' + directs[0] + '\\' + em + '\\' + f
        copyfile(source, dst)
    
