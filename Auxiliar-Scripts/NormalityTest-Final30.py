from pathlib import Path
import pandas
import numpy as np
import shutil
import os
# Shapiro-Wilk Test
from scipy.stats import shapiro
# D'Agostino and Pearson's Test
from scipy.stats import normaltest
# Anderson-Darling Test
from scipy.stats import anderson
import statistics

normality_test = 1  # 1 - Shapiro-Wilk Test
                    # 2 - D'Agostino and Pearson's Test
                    # 3 - Anderson-Darling Test

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
        file_option = Path().absolute().parent /'Test-1/Results/TestC-Final.csv'
        csv_file = pandas.read_csv(file_option)
    elif(option_test == '3'):
        file_option = Path().absolute().parent /'Test-3/Results/TestC-Final.csv'
        csv_file = pandas.read_csv(file_option)
    else:
        print('Opçao inválida.')
        exit()

    COLUMNS_READ = ['Recognition Model', 'Subject', 'Average Result', 'Average Recognition']
    vetor_final = {}

    for recognizer in models_recognition:
        average_result = []

        for i in range(len(csv_file)):
            if recognizer == csv_file[COLUMNS_READ[0]][i]:
                average_result.append(csv_file[COLUMNS_READ[2]][i])

        if(normality_test == 1):
            # Shapiro-Wilk Test
            # normality test
            stat, p = shapiro(average_result)
            print('Statistics=%.3f, p=%.3f' % (stat, p))
            # interpret
            alpha = 0.05
            if p > alpha:
                print('Sample looks Gaussian (fail to reject H0)')
                print(recognizer)
                vetor_final[recognizer] = True
            else:
                print('Sample does not look Gaussian (reject H0)')
                print(recognizer)
                vetor_final[recognizer] = False

        elif(normality_test == 2):
            # D'Agostino and Pearson's Test
            # normality test
            stat, p = normaltest(average_result)
            print('Statistics=%.3f, p=%.3f' % (stat, p))
            # interpret
            alpha = 0.05
            if p > alpha:
                print('Sample looks Gaussian (fail to reject H0)')
                print(recognizer)
                vetor_final[recognizer] = True
            else:
                print('Sample does not look Gaussian (reject H0)')
                print(recognizer)
                vetor_final[recognizer] = False

        else:
            # Anderson-Darling Test
            # normality test
            result = anderson(data)
            print('Statistic: %.3f' % result.statistic)
            p = 0
            for i in range(len(result.critical_values)):
                sl, cv = result.significance_level[i], result.critical_values[i]
                if result.statistic < result.critical_values[i]:
                    print('%.3f: %.3f, data looks normal (fail to reject H0)' % (sl, cv))
                    print(recognizer)
                    vetor_final[recognizer] = True
                else:
                    print('%.3f: %.3f, data does not look normal (reject H0)' % (sl, cv))
                    print(recognizer)
                    vetor_final[recognizer] = False

        variancia = statistics.variance(average_result, xbar=None)

    name_txt = 'NormalityTest-Final30.txt'
    test = 'Test-'+str(option_test)
    path_txt = Path().absolute().parent / test / 'Results' /name_txt
    with open(path_txt, 'w') as txt_file:
        txt_file.write(str(vetor_final) + '\n')
        txt_file.write('Variancia: '+str(variancia))