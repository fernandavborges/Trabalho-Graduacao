"""
    Script that performs the recognition tests (the recognition is always done between two images).
"""

from deepface import DeepFace
import os
from pathlib import Path
from pandas import DataFrame
import threading


distance_metrics = [
  "cosine", 
  "euclidean", 
  "euclidean_l2"
]

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

def recognition_thread(subjects, files, bd_folder, results_folder, file_logs_path, columns, test):
    first_subject = True
    previous_image = ''
    subject = ''
 
    for file in files: 
        if(file != '.gitignore' and file[0:4] in subjects):
            if(file[0:4] != subject and first_subject == False): # Changed subject - save csv with previous subject information
                name_csv = previous_image[0:4] + '.csv'
                path_csv = results_folder / name_csv
                results.to_csv(path_csv)
                file_logs.close()
                results = DataFrame(columns=columns)
                file_logs_name =  file[0:4] + '.txt'
                file_logs = open(file_logs_path / file_logs_name, "w")
                previous_image = ''
            subject = file[0:4]

            if(first_subject):
                results = DataFrame(columns=columns)
                first_subject = False
                file_logs_name =  file[0:4] + '.txt'
                file_logs = open(file_logs_path / file_logs_name, "w")

            for recognizer in models_recognition:
                print('Detector: ' + models_detection[3] + '\n' + 'Recognizer: ' + recognizer + '\n')
                if previous_image != '':
                    img1_path = str(bd_folder / previous_image)
                    img2_path = str(bd_folder / file)
                    try:
                        result = DeepFace.verify(img1_path = img1_path, img2_path = img2_path, model_name=recognizer, distance_metric = "cosine", detector_backend = models_detection[3])
                        if(test == '1' or test == '2'):
                            line = [previous_image, previous_image[10:14], file, file[10:14], distance_metrics[0], models_detection[3], recognizer, result.get('distance'), result.get('verified')]
                        else:
                            line = [previous_image, previous_image[4:6], file, file[4:6], distance_metrics[0], models_detection[3], recognizer, result.get('distance'), result.get('verified')]
                        results.loc[len(results)] = line
                    except Exception as exception:
                        print('Exception:' + str(exception))
                        file_logs.write('Detector: ' + models_detection[3]  + '. Recognizer: ' + recognizer + '.\n') 
                        file_logs.write('Imagem ' + previous_image + ' e ' + file + '\n') 
                        file_logs.write('Exception:' + str(exception) + '\n\n')
            previous_image = file

    name_csv = subject + '.csv'
    path_csv = results_folder / name_csv
    results.to_csv(path_csv)
    file_logs.close()

if __name__ == "__main__":
    option_test = input('Qual teste será rodado? \n 1. Teste 1 \n 2. Teste 2 \n 3. Teste 3 \n 4. Teste 4\n >>')
    
    if(option_test == '1'):
        PATH_DIRECTORY = Path().absolute() / 'Test-1'
        COLUMNS = ['Image 1', 'Year 1', 'Image 2', 'Year 2', 'Distance Metric', 'Detection Model', 'Recognition Model', 'Distance Result', 'Recognition Result']
        PATH_LOGS = Path().absolute() / 'Test-1/Logs/'
        PATH_BD = PATH_DIRECTORY / 'BD'
    elif(option_test == '2'):
        PATH_DIRECTORY = Path().absolute() / 'Test-2'
        COLUMNS = ['Image 1', 'Year 1', 'Image 2', 'Year 2', 'Distance Metric', 'Detection Model', 'Recognition Model', 'Distance Result', 'Recognition Result']
        PATH_LOGS = Path().absolute() / 'Test-2/Logs/'
        PATH_BD = PATH_DIRECTORY / 'BD'
    elif(option_test == '3'):
        PATH_DIRECTORY = Path().absolute() / 'Test-3'
        COLUMNS = ['Image 1', 'Age 1', 'Image 2', 'Age 2', 'Distance Metric', 'Detection Model', 'Recognition Model', 'Distance Result', 'Recognition Result']
        PATH_LOGS = Path().absolute() / 'Test-3/Logs/'
        PATH_BD = PATH_DIRECTORY / 'BD-FGNET'
    elif(option_test == '4'):
        PATH_DIRECTORY = Path().absolute() / 'Test-4'
        COLUMNS = ['Image 1', 'Age 1', 'Image 2', 'Age 2', 'Distance Metric', 'Detection Model', 'Recognition Model', 'Distance Result', 'Recognition Result']
        PATH_LOGS = Path().absolute() / 'Test-4/Logs/'
        PATH_BD = PATH_DIRECTORY / 'BD-FGNET'
    else:
        print('Opção inválida.')
        exit()

    option_mode = input('\nQual o modo de teste?\n 1. Normal \n 2. Aleatório \n 3. Quartis\n>>')

    if(option_mode == '1'): 
        results_folder = PATH_DIRECTORY / 'Results/Test1A/'
    elif(option_mode == '2'):
        number_test = input('\nNúmero do teste a ser realizado (é esperado um número inteiro que será adicionado ao nome da pasta): ')
        name = 'Results/Test' + number_test + 'B/'
        results_folder = PATH_DIRECTORY / name
    elif(option_mode == '3'):
        number_test = input('\nNúmero do teste a ser realizado (é esperado um número inteiro que será adicionado ao nome da pasta): ')
        name = 'Results/Test' + number_test + 'C/'
        results_folder = PATH_DIRECTORY / name
    else:
        print('Opção inválida.')
        exit()

    files = os.listdir(PATH_BD)
    files.sort()
    subjects = []
    thread_subjects = []
    n_threads = int(input("Número de threads a serem criadas: "))

    if(results_folder.exists()):
        csv = os.listdir(results_folder)
        for c in csv:  
            subjects.append(c[0:4])
    else:
        os.mkdir(results_folder)
    for file in files:
        if(file[0:4] not in thread_subjects and file[0:4] not in subjects):
            thread_subjects.append(file[0:4])
    n_subjects = int(len(thread_subjects)/n_threads)
    for i in range(n_threads):
        if(i == n_threads - 1):
            threading.Thread(target=recognition_thread, args=(thread_subjects[i*n_subjects:], files, PATH_BD, results_folder, PATH_LOGS, COLUMNS, option_test, )).start() 
            print('Thread criada! - Sujeitos:', thread_subjects[i*n_subjects:])
        else:
            threading.Thread(target=recognition_thread, args=(thread_subjects[i*n_subjects:(i+1)*n_subjects], files, PATH_BD, results_folder, PATH_LOGS, COLUMNS, option_test, )).start()
            print('Thread criada! - Sujeitos:', thread_subjects[i*n_subjects:(i+1)*n_subjects])
        
