import os

dataset_path = 'E:\\TESI\\TESI_LAMBONI_VIVIANA\\DATASET'

emotions = [
    'BOREDOM',
    'CONFUSION',
    'ENTHUSIASM',
    'FRUSTRATION',
    'INTEREST',
    'NEUTRAL',
    'SURPRISE'
    ]

yale = 'YALE'

for em in emotions:
    print(dataset_path + '\\' + em + '\\' + yale + '\\')
    if os.path.isdir(dataset_path + '\\' + em + '\\' + yale + '\\'):
        entries = os.scandir(dataset_path + '\\' + em + '\\' + yale + '\\')
        for en in entries:
            if en.is_file():
                my_file = en.name
                print("FILE NAME: " + my_file)
                base = os.path.splitext(my_file)[0]
                print("BASE: " + base)
                complete_path_from = dataset_path + '\\' + em + '\\' + yale + '\\' + my_file
                complete_path_to = dataset_path + '\\' + em + '\\' + yale + '\\' + base + '.jpeg'
                os.rename(complete_path_from, complete_path_to)