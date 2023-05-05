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

if __name__ == "__main__":    
    option_test = input('Em qual teste será realizado a análise? \n 1. Teste 1 \n 2. Teste 2 \n 3. Teste 3\n 4. Teste 4\n>>')

    if(option_test == '1'):
        file_positive = 'Test-2/Results/Test-Accuracy/Accuracy-positive.csv'
        file_negative = 'Test-2/Results/Test-Accuracy/Accuracy-negative.csv'
        csv_file_positive = pandas.read_csv(file_positive)
        csv_file_negative = pandas.read_csv(file_negative)
        COLUMNS = ['Image 1', 'Year 1', 'Image 2', 'Year 2', 'Distance Metric', 'Detection Model', 'Recognition Model', 'Distance Result', 'Recognition Result']
        
        for recognizer in models_recognition:
            recognized_pos = 0
            results_recognizer_pos = []
            for i in range(len(csv_file_positive)):
                if csv_file_positive[COLUMNS[6]][i] == recognizer:
                    results_recognizer_pos.append(csv_file_positive[COLUMNS[7]][i])
                    if(csv_file_positive[COLUMNS[8]][i] == True):
                        recognized_pos = recognized_pos + 1
            print("Casos - Modelo " + str(recognizer))
            print("Reconheceu corretamente (= True): " + str(recognized_pos))
            print("Porcentagem: " + str(recognized_pos/len(results_recognizer_pos)))

            recognized_neg = 0
            results_recognizer_neg = []
            for i in range(len(csv_file_negative)):
                if csv_file_negative[COLUMNS[6]][i] == recognizer:
                    results_recognizer_neg.append(csv_file_negative[COLUMNS[7]][i])
                    if(csv_file_negative[COLUMNS[8]][i] == "FALSE"):
                        recognized_neg = recognized_neg + 1
            print("Reconheceu corretamente (= False): " + str(recognized_neg))
            print("Porcentagem: " + str(recognized_neg/len(results_recognizer_neg)))

            final = (recognized_pos + recognized_neg)/(len(results_recognizer_neg)+len(results_recognizer_neg))
            print("Porcentage final - Modelo " + str(recognizer) + ": " + str(final)+"\n")
    elif(option_test == '3'):
        file = 'Test-3/Results/Test-Accuracy/Accuracy.csv'
        csv = pandas.read_csv(file)
        COLUMNS = ['Image 1', 'Age 1', 'Image 2', 'Age 2', 'Distance Metric', 'Detection Model', 'Recognition Model', 'Distance Result', 'Recognition Result']
        
        for recognizer in models_recognition:
            recognized_pos = 0
            results_recognizer_pos = []

            #print('len(file): '+str(len(csv)))
            #print('len(file)/2+ 2: '+str(round(len(csv)/2)+2))
                        
            for i in range((round(len(csv)/2) +2)):
                if csv[COLUMNS[6]][i] == recognizer:
                    results_recognizer_pos.append(csv[COLUMNS[7]][i])
                    if(str(csv[COLUMNS[8]][i]) == 'True'):
                        recognized_pos = recognized_pos + 1
            print("Casos - Modelo " + str(recognizer))
            print("Reconheceu corretamente (= True): " + str(recognized_pos))
            print("Porcentagem: " + str(recognized_pos/len(results_recognizer_pos)))

            recognized_neg = 0
            results_recognizer_neg = []
            for i in range(((round(len(csv)/2))+2), len(csv)):
                if csv[COLUMNS[6]][i] == recognizer:
                    results_recognizer_neg.append(csv[COLUMNS[7]][i])
                    if(str(csv[COLUMNS[8]][i]) == 'False'):
                        recognized_neg = recognized_neg + 1
            print("Reconheceu corretamente (= False): " + str(recognized_neg))
            print("Porcentagem: " + str(recognized_neg/len(results_recognizer_neg)))

            final = (recognized_pos + recognized_neg)/(len(results_recognizer_neg)+len(results_recognizer_neg))
            print("Porcentage final - Modelo " + str(recognizer) + ": " + str(final)+"\n")
    else:
        print('Opçao inválida.')
        exit()

    

    


