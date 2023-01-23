import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
import os
import pandas
import numpy as np

PATH_DIRECTORY = Path(__file__).parents[0] / 'Results/CSVs'
files = PATH_DIRECTORY.glob('*.csv')

COLUMNS = ['Surgery', 'Image 1', 'Image 2', 'Distance Metric', 'Detection Model', 'Recognition Model', 'Distance Result', 'Recognition Result']

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

# Configurations for ploters
vector = np.vectorize(np.int_)
n_models = len(models_recognition)

def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height), xy=(rect.get_x() + rect.get_width() / 2, height), xytext=(0, 3), textcoords="offset points", ha='center', va='bottom')

for file in files:
  csv_file = pandas.read_csv(file)
  total_comparactions = (len(csv_file)/len(models_detection))/len(models_recognition)
  for detector in models_detection:
    results_recognizer = []
    results_correct = []
    results_incorrect = []
    for recognizer in models_recognition:
      correct = 0
      for i in range(len(csv_file)):
        if csv_file[COLUMNS[7]][i] == True and csv_file[COLUMNS[5]][i] == recognizer and csv_file[COLUMNS[4]][i] == detector:
          correct += 1
      total = 0
      for i in range(len(csv_file)):
        if csv_file[COLUMNS[5]][i] == recognizer and csv_file[COLUMNS[4]][i] == detector:
          total += 1
      results_recognizer.append(recognizer)
      results_correct.append(correct)
      results_incorrect.append(total-correct)

    correct = vector(np.array(results_correct))
    incorrect = vector(np.array(results_incorrect))

    # create plot
    fig, ax = plt.subplots()
    index = np.arange(n_models)
    bar_width = 0.35

    rects1 = plt.bar(index, correct, bar_width, color='g', label='Correto')
    rects2 = plt.bar(index + bar_width, incorrect, bar_width, color='r', label='Incorreto')

    ax.plot([0., index[-1]+bar_width], [total_comparactions*6, total_comparactions*6], "-", color='b')

    plt.xlabel('Modelos de Reconhecimento')
    plt.ylabel('Quantidade de Imagens')
    plt.title('Deteceção com ' + detector)
    plt.xticks(index + bar_width, np.asarray(results_recognizer))
    plt.legend()
    autolabel(rects1)
    autolabel(rects2)
    plt.tight_layout()
    name_plot = str(Path(__file__).parents[0] / 'Results/Images') + '/' + detector
    print(name_plot)
    plt.savefig(name_plot)
    plt.show()
