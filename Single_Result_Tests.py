from pathlib import Path
import pandas
import numpy as np
import shutil
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

if __name__ == "__main__":
    COLUMNS_WRITE = ['Subject', 'Average Result']
    
    option_test = input('Em qual teste será realizado a análise? \n 1. Teste 1 \n 2. Teste 2 \n 3. Teste 3\n 4. Teste 4\n>>')

    if(option_test == '1'):
        path_tests = Path().absolute() / 'Test-1/Results/'
        print('Pasta de resultados disponíveis no Test-1:')
        for path in path_tests.iterdir():
            if path.is_dir() and (str(path).find('Results\Test')!=-1):
                path_str = str(path)
                print('-', path_str[path_str.index('\Results')+len('\Results/'):], '\n')
        option_folder = input('Qual a pasta de resultados será analisada? (ex: Test1A): ')
        name_folder_read = 'Test-1/Results/' + option_folder
        COLUMNS_READ = ['Image 1', 'Year 1', 'Image 2', 'Year 2', 'Distance Metric', 'Detection Model', 'Recognition Model', 'Distance Result', 'Recognition Result']
        name_folder_write = 'Test-1/Results/SingleResult-' + option_folder
    elif(option_test == '2'):
        path_tests = Path().absolute() / 'Test-2/Results/'
        print('Pasta de resultados disponíveis no Test-2:')
        for path in path_tests.iterdir():
            if path.is_dir() and (str(path).find('Results\Test')!=-1):
                path_str = str(path)
                print('-', path_str[path_str.index('\Results')+len('\Results/'):], '\n')
        option_folder = input('Qual a pasta de resultados será analisada? (ex: Test1A): ')
        name_folder_read = 'Test-2/Results/' + option_folder
        COLUMNS_READ = ['Image 1', 'Year 1', 'Image 2', 'Year 2', 'Distance Metric', 'Detection Model', 'Recognition Model', 'Distance Result', 'Recognition Result']
        name_folder_write = 'Test-2/Results/SingleResult--' + option_folder
    elif(option_test == '3'):
        path_tests = Path().absolute() / 'Test-3/Results/'
        print('Pasta de resultados disponíveis no Test-3:')
        for path in path_tests.iterdir():
            if path.is_dir() and (str(path).find('Results\Test')!=-1):
                path_str = str(path)
                print('-', path_str[path_str.index('\Results')+len('\Results/'):], '\n')
        option_folder = input('Qual a pasta de resultados será analisada? (ex: Test1A): ')
        name_folder_read = 'Test-3/Results/' + option_folder
        COLUMNS_READ = ['Image 1', 'Age 1', 'Image 2', 'Age 2', 'Distance Metric', 'Detection Model', 'Recognition Model', 'Distance Result', 'Recognition Result']
        name_folder_write = 'Test-3/Results/SingleResult--' + option_folder
    elif(option_test == '4'):
        path_tests = Path().absolute() / 'Test-4/Results/'
        print('Pasta de resultados disponíveis no Test-4:')
        for path in path_tests.iterdir():
            if path.is_dir() and (str(path).find('Results\Test')!=-1):
                path_str = str(path)
                print('-', path_str[path_str.index('\Results')+len('\Results/'):], '\n')
        option_folder = input('Qual a pasta de resultados será analisada? (ex: Test1A): ')
        name_folder_read = 'Test-4/Results/' + option_folder
        COLUMNS_READ = ['Image 1', 'Age 1', 'Image 2', 'Age 2', 'Distance Metric', 'Detection Model', 'Recognition Model', 'Distance Result', 'Recognition Result']
        name_folder_write = 'Test-4/Results/SingleResult--' + option_folder

    else:
        print('Opçao inválida.')
        exit()
    
    PATH_DIRECTORY_READ = Path().absolute() / name_folder_read
    PATH_DIRECTORY_WRITE = Path().absolute() / name_folder_write

    if(PATH_DIRECTORY_READ.exists()):
        files_read = PATH_DIRECTORY_READ.glob('*.csv')
    else:
        print('Pasta de resultado não existe.')
        exit()
    if(PATH_DIRECTORY_WRITE.exists()):
        shutil.rmtree(PATH_DIRECTORY_WRITE)
    os.mkdir(PATH_DIRECTORY_WRITE)
   
    path_files = []
    for file in files_read:
        path_files.append(str(file))

    for recognizer in models_recognition:
        results = pandas.DataFrame(columns=COLUMNS_WRITE)
        k = 0
        for file in path_files:
            average = 0
            results_recognizer = []

            csv_file = pandas.read_csv(file)
            subject = csv_file[COLUMNS_READ[0]][0][0:4]
            for i in range(len(csv_file)):
                if csv_file[COLUMNS_READ[6]][i] == recognizer:
                    results_recognizer.append(csv_file[COLUMNS_READ[7]][i])

            average = sum(results_recognizer)/len(results_recognizer)
            
            results.loc[k] = [subject, average]
            k = k + 1
        name_csv = 'SingleResult_' + recognizer +'.csv'
        path_csv = PATH_DIRECTORY_WRITE / name_csv
        results.to_csv(path_csv)

    if(PATH_DIRECTORY_WRITE.exists()):
        files_read = PATH_DIRECTORY_WRITE.glob('*.csv')
    else:
        print('Deu erro para ler os csv que foram gerados agora.')
        exit()

    COLUMNS_READ = ['Subject', 'Average Result']
    COLUMNS_WRITE = ['Recognition Model', 'Average Result']
    path_files = []
    for file in files_read:
        path_files.append(str(file))
        results = pandas.DataFrame(columns=COLUMNS_WRITE)
        k = 0
        for file in path_files:
            average = 0
            results_recognizer = []

            csv_file = pandas.read_csv(file)
            for i in range(len(csv_file)):
                results_recognizer.append(csv_file[COLUMNS_READ[1]][i])

            average = sum(results_recognizer)/len(results_recognizer)
            
            file = (file.split('SingleResult_'))[1].split('.csv')[0]
            results.loc[k] = [file, average]
            k = k + 1
        name_csv = 'SingleResult-Final.csv'
        path_csv = PATH_DIRECTORY_WRITE / name_csv
        results.to_csv(path_csv)
