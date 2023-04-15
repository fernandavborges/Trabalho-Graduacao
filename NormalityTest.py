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

normality_test = 2  # 1 - Shapiro-Wilk Test
                    # 2 - D'Agostino and Pearson's Test
                    # 3 - 

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
        path_tests = Path().absolute() / 'Test-1/Results/'
        print('Pasta de resultados disponíveis no Test-1:')
        for path in path_tests.iterdir():
            if path.is_dir() and (str(path).find('Results\SingleResult-Test')!=-1):
                path_str = str(path)
                print('-', path_str[path_str.index('\Results')+len('\Results/'):], '\n')
        option_folder = input('Qual a pasta de resultados será analisada? (ex: SingleResult-Test1A): ')
        name_folder = 'Test-1/Results/' + option_folder
    elif(option_test == '2'):
        path_tests = Path().absolute() / 'Test-2/Results/'
        print('Pasta de resultados disponíveis no Test-2:')
        for path in path_tests.iterdir():
            if path.is_dir() and (str(path).find('Results\SingleResult-Test')!=-1):
                path_str = str(path)
                print('-', path_str[path_str.index('\Results')+len('\Results/'):], '\n')
        option_folder = input('Qual a pasta de resultados será analisada? (ex: SingleResult-Test1A): ')
        name_folder = 'Test-2/Results/' + option_folder
    elif(option_test == '3'):
        path_tests = Path().absolute() / 'Test-3/Results/'
        print('Pasta de resultados disponíveis no Test-3:')
        for path in path_tests.iterdir():
            if path.is_dir() and (str(path).find('Results\SingleResult-Test')!=-1):
                path_str = str(path)
                print('-', path_str[path_str.index('\Results')+len('\Results/'):], '\n')
        option_folder = input('Qual a pasta de resultados será analisada? (ex: SingleResult-Test1A): ')
        name_folder = 'Test-3/Results/' + option_folder
    elif(option_test == '4'):
        path_tests = Path().absolute() / 'Test-4/Results/'
        print('Pasta de resultados disponíveis no Test-4:')
        for path in path_tests.iterdir():
            if path.is_dir() and (str(path).find('Results\SingleResult-Test')!=-1):
                path_str = str(path)
                print('-', path_str[path_str.index('\Results')+len('\Results/'):], '\n')
        option_folder = input('Qual a pasta de resultados será analisada? (ex: SingleResult-Test1A): ')
        name_folder = 'Test-4/Results/' + option_folder

    else:
        print('Opçao inválida.')
        exit()
    
    PATH_DIRECTORY = Path().absolute() / name_folder

    if(PATH_DIRECTORY.exists()):
        files_read = PATH_DIRECTORY.glob('*.csv')
    else:
        print('Pasta de resultado não existe.')
        exit()

    COLUMNS_READ = ['Subject', 'Average Result']
    vetor_final = {}

    path_files = []
    for file in files_read:
        if not ('Final' in str(file)):
            average_result = []

            csv_file = pandas.read_csv(file)
            for i in range(len(csv_file)):
                average_result.append(csv_file[COLUMNS_READ[1]][i])

            file = (str(file).split('SingleResult_'))[1].split('.csv')[0]

            if(normality_test == 1):
                # Shapiro-Wilk Test
                # normality test
                stat, p = shapiro(average_result)
                print('Statistics=%.3f, p=%.3f' % (stat, p))
                # interpret
                alpha = 0.05
                if p > alpha:
                    print('Sample looks Gaussian (fail to reject H0)')
                    print(file)
                    vetor_final[file] = True
                else:
                    print('Sample does not look Gaussian (reject H0)')
                    print(file)
                    vetor_final[file] = False

            elif(normality_test == 2):
                # D'Agostino and Pearson's Test
                # normality test
                stat, p = normaltest(average_result)
                print('Statistics=%.3f, p=%.3f' % (stat, p))
                # interpret
                alpha = 0.05
                if p > alpha:
                    print('Sample looks Gaussian (fail to reject H0)')
                    print(file)
                    vetor_final[file] = True
                else:
                    print('Sample does not look Gaussian (reject H0)')
                    print(file)
                    vetor_final[file] = False

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
                        print(file)
                        vetor_final[file] = True
                    else:
                        print('%.3f: %.3f, data does not look normal (reject H0)' % (sl, cv))
                        print(file)
                        vetor_final[file] = False

    name_txt = 'NormalityTest.txt'
    path_txt = PATH_DIRECTORY / name_txt
    with open(path_txt, 'w') as txt_file:
        txt_file.write(str(vetor_final))
