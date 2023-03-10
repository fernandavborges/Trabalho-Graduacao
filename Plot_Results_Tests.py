import matplotlib.pyplot as plt
from pathlib import Path
import pandas
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
models_detection = [
  "opencv", 
  "ssd", 
  "dlib", 
  "mtcnn", 
  "retinaface", 
  "mediapipe"
]

thresholds = [
    0.4,
    0.4,
    0.3,
    0.1,
    0.23,
    0.015,
    0.68,
    0.07,
    0.5932763306134152
]

if __name__ == "__main__":

    option_test = input('Para qual teste será realizado o plot? \n 1. Teste 1 \n 2. Teste 2 \n 3. Teste 3 \n>>')

    if(option_test == '1'):
        path_tests = Path().absolute() / 'Test-1/Results/'
        print('Pasta de resultados disponíveis no Test-1:')
        for path in path_tests.iterdir():
            if path.is_dir() and (str(path).find('Results\Test')!=-1):
                path_str = str(path)
                print('-', path_str[path_str.index('\Results')+len('\Results/'):], '\n')
        option_folder = input('Qual a pasta de resultados será analisada? (ex: Test1A): ')
        name_folder = 'Test-1/Results/' + option_folder
        COLUMNS = ['Image 1', 'Year 1', 'Image 2', 'Year 2', 'Distance Metric', 'Detection Model', 'Recognition Model', 'Distance Result', 'Recognition Result']
        name_folder_write = 'Test-1/Results/' + 'Images-' + option_folder
    elif(option_test == '2'):
        path_tests = Path().absolute() / 'Test-2/Results/'
        print('Pasta de resultados disponíveis no Test-2:')
        for path in path_tests.iterdir():
            if path.is_dir() and (str(path).find('Results\Test')!=-1):
                path_str = str(path)
                print('-', path_str[path_str.index('\Results')+len('\Results/'):], '\n')
        option_folder = input('Qual a pasta de resultados será analisada? (ex: Test1A): ')
        name_folder = 'Test-2/Results/' + option_folder
        COLUMNS = ['Image 1', 'Year 1', 'Image 2', 'Year 2', 'Distance Metric', 'Detection Model', 'Recognition Model', 'Distance Result', 'Recognition Result']
        name_folder_write = 'Test-2/Results/' + 'Images-' + option_folder
    elif(option_test == '3'):
        path_tests = Path().absolute() / 'Test-3/Results/'
        print('Pasta de resultados disponíveis no Test-3:')
        for path in path_tests.iterdir():
            if path.is_dir() and (str(path).find('Results\Test')!=-1):
                path_str = str(path)
                print('-', path_str[path_str.index('\Results')+len('\Results/'):], '\n')
        option_folder = input('Qual a pasta de resultados será analisada? (ex: Test1A): ')
        name_folder = 'Test-3/Results/' + option_folder
        COLUMNS = ['Image 1', 'Age 1', 'Image 2', 'Age 2', 'Distance Metric', 'Detection Model', 'Recognition Model', 'Distance Result', 'Recognition Result']
        name_folder_write = 'Test-3/Results/' + 'Images-' + option_folder
    else:
        print('Opçao inválida.')
        exit()
        
    PATH_DIRECTORY = Path().absolute() / name_folder
    PATH_DIRECTORY_WRITE = Path().absolute() / name_folder_write

    if(PATH_DIRECTORY.exists()):
        files = PATH_DIRECTORY.glob('*.csv')
    else:
        print('Pasta de resultado não existe.')
        exit()
    
    if(PATH_DIRECTORY_WRITE.exists()):
        shutil.rmtree(PATH_DIRECTORY_WRITE)
    os.mkdir(PATH_DIRECTORY_WRITE)

    subject = ''
    for file in files:
        csv_file = pandas.read_csv(file)
        subject = csv_file[COLUMNS[0]][0][0:4]
        for iterator in zip(models_recognition, thresholds):
            results_recognizer = []
            year = []
            for i in range(len(csv_file)):
                if csv_file[COLUMNS[6]][i] == iterator[0]:
                    results_recognizer.append(csv_file[COLUMNS[7]][i])
                    year.append(csv_file[COLUMNS[1]][i])

            plt.figure()
            plt.xlabel("Anos")
            plt.ylabel("Distâncias")
            plt.title("Sujeito: "+ subject + ". Modelo: " + iterator[0] + ".")
            plt.bar(year, results_recognizer)
            plt.plot([year[0], year[-1]], [iterator[1], iterator[1]], "-", color='b', label='Limite')
            name_plot = str(PATH_DIRECTORY_WRITE) +  '/' + subject + '-' + iterator[0]
            plt.savefig(name_plot)
            #plt.show()
            plt.close()