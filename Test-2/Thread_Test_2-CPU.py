"""
    Script that performs the recognition tests for Test 3 (FGNET Database), and the recognition is always done between two images.
"""

from deepface import DeepFace
import os
from pathlib import Path
from pandas import DataFrame
import threading

# Chosing the database
PATH_DIRECTORY = Path().absolute() / 'BD'

COLUMNS = ['Image 1', 'Year 1', 'Image 2', 'Year 2', 'Distance Metric', 'Detection Model', 'Recognition Model', 'Distance Result', 'Recognition Result']

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

def recognition_thread(subject):
    files = os.listdir(PATH_DIRECTORY)
    files.sort()
    print(files)
    first_subject = True
    previous_image = ''
    file_logs_name =  subject + '.txt'
    file_logs = open(file_logs_path / file_logs_name, "w")
 
    for file in files: 
        print('File: ',file)
        if(file != '.gitignore'):
            if file[0:4] == subject:
                if (first_subject):
                    results = DataFrame(columns=COLUMNS)
                    first_subject = False
                    previous_image = file
                else:
                    for recognizer in models_recognition:
                        print('Detector: ' + models_detection[3] + '\n' + 'Recognizer: ' + recognizer + '\n')
                        if previous_image != '':
                            img1_path = str(Path().absolute() / 'BD' / previous_image)
                            img2_path = str(Path().absolute() / 'BD' / file)
                            try:
                                result = DeepFace.verify(img1_path = img1_path, img2_path = img2_path, model_name=recognizer, distance_metric = "cosine", detector_backend = models_detection[3])
                                results = results.append({'Image 1':previous_image, 'Year 1':previous_image[10:14], 'Image 2':file, 'Year 2':file[10:14], 'Distance Metric':distance_metrics[0], 'Detection Model':models_detection[3], 'Recognition Model':recognizer, 'Distance Result':result.get('distance'), 'Recognition Result':result.get('verified')}, ignore_index=True)
                            except Exception as exception:
                                print('Exception:' + str(exception))
                                file_logs.write('Detector: ' + models_detection[3]  + '. Recognizer: ' + recognizer + '.\n') 
                                file_logs.write('Imagem ' + previous_image + ' e ' + file + '\n') 
                                file_logs.write('Exception:' + str(exception) + '\n\n')
                    previous_image = file

            if (int(file[1:4]) > int(subject[1:4])):
                break

    name_csv = subject + '.csv'
    path_csv = results_folder / name_csv
    results.to_csv(path_csv)
    file_logs.close()

if __name__ == "__main__":
    files = os.listdir(PATH_DIRECTORY)
    subjects = []

    for file in files:
        if file[0:4] not in subjects:
            threading.Thread(target=recognition_thread, args=(file[0:4],)).start()
            print('Thread lancada!')
            subjects.append(file[0:4])