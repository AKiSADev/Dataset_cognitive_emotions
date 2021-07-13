import os
from shutil import copyfile

dataset_path = 'E:\\TESI\\TESI_LAMBONI_VIVIANA\\DATASET'
dataset_final_path = 'E:\\TESI\\TESI_LAMBONI_VIVIANA\\DATASET_FINALE'

emotions = [
    'BOREDOM',
    'CONFUSION',
    'ENTHUSIASM',
    'FRUSTRATION',
    'INTEREST',
    'NEUTRAL',
    'SURPRISE'
    ]


for em in emotions:
    print(em)
    print("DIRECTORIES:")
    if not os.path.isdir(dataset_final_path + '\\' + em):
        os.makedirs(dataset_final_path + '\\' + em)
    for root, dirs, files in os.walk(dataset_path + '\\' + em, topdown=False):
        for f in files:
            if f != ".directory":
                print('ROOT: ' + root)
                print ("FILE: " + f)
                dataset = root.split("\\")[5]
                print("DATASET: " + dataset)
                source = os.path.join(root, f)
                dst = dataset_final_path + '\\' + em + '\\' + dataset + '_' + f
                copyfile(source, dst)
            



