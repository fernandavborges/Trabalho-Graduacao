"""
    Script that performs the recognition tests for Test 3 (FGNET Database), and the recognition is always done between two images.
"""

from deepface import DeepFace
import os
from pathlib import Path
from pandas import DataFrame

# Chosing the database
PATH_DIRECTORY = Path().absolute() / 'BD-FGNET'
files = os.listdir(PATH_DIRECTORY)

previous_image = ''
subject = ''
first_subject = True

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
file_logs_name = Path().absolute() / 'Logs_Test_3.txt'

file_logs = open(file_logs_name, "w")

for file in files: 
    if(file[0:4] != subject and first_subject == False): # Changed subject - save csv with previous subject information
        name_csv = previous_image[0:4] + '.csv'
        path_csv = results_folder / name_csv
        save = results.to_csv(path_csv)
        results = DataFrame(columns=COLUMNS)
        previous_image = ''
    subject = file[0:4]
    if first_subject:
        results = DataFrame(columns=COLUMNS)
        first_subject = False
    for detector in models_detection:
        for recognizer in models_recognition:
            print('Detector: ' + detector + '\n' + 'Recognizer: ' + recognizer + '\n')
            if previous_image != '':
                img1_path = str(Path().absolute() / 'BD-FGNET' / previous_image)
                img2_path = str(Path().absolute()/ 'BD-FGNET' / file)
                try:
                    result = DeepFace.verify(img1_path = img1_path, img2_path = img2_path, model_name=recognizer, distance_metric = "cosine", detector_backend = detector)
                    results = results.append({'Image 1':previous_image, 'Age 1':previous_image[4:6], 'Image 2':file, 'Age 2':file[4:6], 'Distance Metric':distance_metrics[0], 'Detection Model':detector, 'Recognition Model':recognizer, 'Distance Result':result.get('distance'), 'Recognition Result':result.get('verified')}, ignore_index=True)
                except Exception as exception:
                    print('Exception:' + str(exception))
                    file_logs.write('Detector: ' + detector + '. Recognizer: ' + recognizer + '.\n') 
                    file_logs.write('Imagem ' + previous_image + ' e ' + file + '\n') 
                    file_logs.write('Exception:' + str(exception) + '\n\n')
    previous_image = file

name_csv = previous_image[0:4] + '.csv'
path_csv = results_folder / name_csv
save = results.to_csv(path_csv)
file_logs.close()
    


# fig, ax = plt.subplots()

# ax.bar(anos, distancias, width=1, edgecolor="white", linewidth=0.7)

# ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
#        ylim=(0, 8), yticks=np.arange(1, 8))

# plt.show()