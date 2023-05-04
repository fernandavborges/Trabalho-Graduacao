from pathlib import Path
import pandas
import numpy as np
import os

models_recognition = [
  "VGG-Face", 
  "Facenet", 
  "Facenet512", 
  "OpenFace", 
  "DeepFace", 
  "DeepID", 
  "ArcFace", 
  "Dlib", 
  "SFace"
]

COLUMNS_WRITE = ['Recognition Model', 'Subject', 'Average Result', 'Average Recognition']

if __name__ == "__main__":
    option_test = input('Em qual teste será realizado a análise? \n 1. Teste 1 \n 3. Teste 3 \n >>')

    if(option_test == '1'):
        path_tests = Path().absolute() / 'Test-1/Results/'
        COLUMNS_READ = ['Image 1', 'Year 1', 'Image 2', 'Year 2', 'Distance Metric', 'Detection Model', 'Recognition Model', 'Distance Result', 'Recognition Result']
    elif(option_test == '3'):
        path_tests = Path().absolute() / 'Test-3/Results/'
        COLUMNS_READ = ['Image 1', 'Age 1', 'Image 2', 'Age 2', 'Distance Metric', 'Detection Model', 'Recognition Model', 'Distance Result', 'Recognition Result']
    else:
        print('Opção inválida.')
        exit()
    
    PATH_DIRECTORY_READ = path_tests
    option_test = input('Qual tipo de teste? (ex: C): ')

    tests_read = []
    if(option_test == 'C'):
        with os.scandir(path_tests) as itr:
            for entry in itr :
                if entry.is_dir() and 'C' in entry.name:
                    tests_read.append(entry.path)
    elif(option_test == 'B'):
        with os.scandir(path_tests) as itr:
            for entry in itr :
                if entry.is_dir() and 'B' in entry.name:
                    tests_read.append(entry.path)
    else:
        print('Tipo de teste inválido.')
        exit()
    
    if(tests_read == None):
        print('Pasta de resultados desse tipo não existe.')
        exit()

results = pandas.DataFrame(columns=COLUMNS_WRITE)
k = 0
for recognizer in models_recognition:
    average_result = []
    average_recognition = []
    for test in tests_read:
        avg_file = []
        avg_rec_file = []
        subjects = []

        files_read = Path(test).glob('*.csv')
        path_files = []
        for file in files_read:
            path_files.append(str(file))
        

        for file in path_files:
            csv_file = pandas.read_csv(file)
            subjects.append(csv_file[COLUMNS_READ[0]][0][:4])
            recognized = 0
            total = 0
            results_recognizer = []
            for i in range(len(csv_file)):
                if(csv_file[COLUMNS_READ[6]][i] == recognizer):
                    results_recognizer.append(csv_file[COLUMNS_READ[7]][i])
                    total = total + 1
                    if(csv_file[COLUMNS_READ[8]][i] == True):
                        recognized = recognized + 1
            avg_file.append(np.mean(np.asarray(results_recognizer)))
            avg_rec_file.append(recognized/total) 
        average_result.append(avg_file)
        average_recognition.append(avg_rec_file)

    
    for result, recognition, subject in zip(np.mean(np.asarray(average_result), axis=0), np.mean(np.asarray(average_recognition), axis=0), np.asarray(subjects)):
        results.loc[k] = [recognizer, subject, result, recognition]
        k = k + 1

name_csv = 'Test' + option_test +'-Final.csv'
path_csv = PATH_DIRECTORY_READ / name_csv
results.to_csv(path_csv)
