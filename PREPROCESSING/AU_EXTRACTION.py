import os
import csv
import shutil

dataset_path = 'E:\\TESI\\TESI_LAMBONI_VIVIANA\\DATASET_FINALE'
command = 'E:\\TESI\\TESI_LAMBONI_VIVIANA\\RISORSE_ESTERNE\\OPENFACE\\OpenFace_2.2.0_win_x64\\OpenFace_2.2.0_win_x64\\FaceLandmarkImg.exe -fdir '
out_dir_command = " -out_dir "
result_path = 'E:\\TESI\\TESI_LAMBONI_VIVIANA\\CSV\\PROCESSED'
csv_path = 'E:\\TESI\\TESI_LAMBONI_VIVIANA\\CSV\\'
completed_file_name = 'COMPLETE_DATASET_AU.csv'

emotions = [
    'BOREDOM',
    'CONFUSION',
    'ENTHUSIASM',
    'FRUSTRATION',
    'INTEREST',
    'NEUTRAL',
    'SURPRISE'
    ]

for f in os.scandir(csv_path):
    if f.is_file():
        os.remove(csv_path + '\\' + f.name)
for em in emotions:
    column_titles = False
    #pulizia directory risultati
    print("Inizio pulizia...")
    for f in os.scandir(result_path):
        if f.is_file():
            os.remove(result_path + '\\' + f.name)
        elif f.is_dir():
            shutil.rmtree(result_path + '\\' + f.name, ignore_errors=True)
    print("Fine pulizia...")
    #analizzo le directories
    directory_path = dataset_path + '\\' + em
    print(directory_path)
    print("Inizio analisi...")
    os.system(command + '"' + directory_path + '"' + out_dir_command + result_path)
    print("Fine analisi...")
    #ripulisci directory risultati da jpg e txt
    with open(csv_path + em + '.csv', 'w', newline='') as file_in:
        writer = csv.writer(file_in)
        processed = os.scandir(result_path)
        print("PROCESSED: " + str(processed))
        for p in processed:
            #print("PROCESSED: " + p.name)
            extension = os.path.splitext(result_path + '\\' + p.name)[1]
            print("EXT: " + str(extension))
            if p.is_file() and (extension != '.csv'):
                os.remove(result_path + '\\' + p.name)
            elif p.is_dir():
                shutil.rmtree(result_path + '\\' + p.name, ignore_errors=True)
            elif p.is_file() and extension == '.csv':
                #unisci csv
                print("CSV: " + p.name)
                with open(result_path + '\\' + p.name, mode='r') as csv_file:
                    csv_reader = csv.reader(csv_file)
                    line_count = 0
                    for row in csv_reader:
                        if line_count == 0 and column_titles == False:
                            row.append("Emotion")
                            row.append("File")
                            column_titles = True
                            writer.writerow(row)
                        elif line_count != 0:
                            row.append(em)
                            row.append(p.name)
                            writer.writerow(row)
                        print(row)
                        line_count += 1
                    csv_file.close()
            elif  p.is_dir():
                shutil.rmtree(os.path.join(result_path, p), ignore_errors=True)
        file_in.close()
with open(csv_path + completed_file_name, 'w', newline='') as file_in:
    writer = csv.writer(file_in)
    column_titles_c = False
    for em in emotions:  
        with open(csv_path + em + '.csv', mode='r') as csv_file:
            csv_reader = csv.reader(csv_file)
            line_count = 0
            for row in csv_reader:
                if line_count == 0 and column_titles_c == False:
                    column_titles_c = True
                    writer.writerow(row)
                elif line_count != 0:
                    writer.writerow(row)
                print(row)
                line_count += 1
            csv_file.close()
    file_in.close()


                