import os
from shutil import copyfile

dataset_balanced = 'E:\\TESI\\TESI_LAMBONI_VIVIANA\\DATASET_FINALE_BALANCED'
dataset_balanced_divided = 'E:\\TESI\\TESI_LAMBONI_VIVIANA\\DATASET_FINALE_BALANCED_SPLITTED'

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


print(directs)
for em in emotions:
    print(em)
    for d in directs:
        if not os.path.isdir(dataset_balanced_divided + '\\' + em + '\\' + d):
            os.makedirs(dataset_balanced_divided + '\\' + em + '\\' + d)
    for root, dirs, files in os.walk(dataset_balanced + '\\' + em, topdown=False):
        file_number = len(files)
        base = file_number *  0.2
        test = file_number * 0.2
        valid = base * 0.2
        base = base - valid
        count = 0
        dst = ''
        for f in files:
            print(directs)
            source = os.path.join(root, f)
            if count <= test:
                dst = dataset_balanced_divided + '\\' + em + '\\'  + directs[1] + '\\' + f
            elif count > test and count <= (test + valid):
                dst = dataset_balanced_divided + '\\' + em + '\\'  + directs[2] + '\\' + f
            elif count > (test + valid) and count <= file_number:
                dst = dataset_balanced_divided + '\\' + em + '\\' + directs[0] + '\\' + f
            print('SOURCE: ' + source)
            print('DEST: ' + dst)
            copyfile(source, dst)
            count += 1