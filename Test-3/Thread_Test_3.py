"""
    Script that performs the recognition tests for Test 3 (FGNET Database), and the recognition is always done between two images.
"""

from deepface import DeepFace
import os
from pathlib import Path
from pandas import DataFrame
import threading

# Chosing the database
PATH_DIRECTORY = Path().absolute() / 'BD-FGNET'

COLUMNS = ['Image 1', 'Age 1', 'Image 2', 'Age 2', 'Distance Metric', 'Detection Model', 'Recognition Model', 'Distance Result', 'Recognition Result']

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

results_folder = Path().absolute() / 'Results/CSVs/'
file_logs_path = Path().absolute() / 'Logs/'

def recognition_thread(subjects, files):
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
                results = DataFrame(columns=COLUMNS)
                file_logs_name =  file[0:4] + '.txt'
                file_logs = open(file_logs_path / file_logs_name, "w")
                previous_image = ''
            subject = file[0:4]

            if(first_subject):
                results = DataFrame(columns=COLUMNS)
                first_subject = False
                file_logs_name =  file[0:4] + '.txt'
                file_logs = open(file_logs_path / file_logs_name, "w")

            for recognizer in models_recognition:
                print('Detector: ' + models_detection[3] + '\n' + 'Recognizer: ' + recognizer + '\n')
                if previous_image != '':
                    img1_path = str(Path().absolute() / 'BD-FGNET' / previous_image)
                    img2_path = str(Path().absolute() / 'BD-FGNET' / file)
                    try:
                        result = DeepFace.verify(img1_path = img1_path, img2_path = img2_path, model_name=recognizer, distance_metric = "cosine", detector_backend = models_detection[3])
                        results = results.append({'Image 1':previous_image, 'Age 1':previous_image[4:6], 'Image 2':file, 'Age 2':file[4:6], 'Distance Metric':distance_metrics[0], 'Detection Model':models_detection[3], 'Recognition Model':recognizer, 'Distance Result':result.get('distance'), 'Recognition Result':result.get('verified')}, ignore_index=True)
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
    files = os.listdir(PATH_DIRECTORY)
    files.sort()
    subjects = []
    thread_subjects = []
    n_threads = int(input("Number of threads you want to create: "))

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
            threading.Thread(target=recognition_thread, args=(thread_subjects[i*n_subjects:], files,)).start() 
            print('Thread created! - Subjects:', thread_subjects[i*n_subjects:])
        else:
            threading.Thread(target=recognition_thread, args=(thread_subjects[i*n_subjects:(i+1)*n_subjects], files,)).start()
            print('Thread created! - Subjects:', thread_subjects[i*n_subjects:(i+1)*n_subjects])
        
