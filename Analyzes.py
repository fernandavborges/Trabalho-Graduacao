from pathlib import Path
import pandas
import numpy as np
import os
# Shapiro-Wilk Test
from scipy.stats import shapiro
# D'Agostino and Pearson's Test
from scipy.stats import normaltest
# Anderson-Darling Test
from scipy.stats import anderson

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

normality_test = 2  # 1 - Shapiro-Wilk Test
                    # 2 - D'Agostino and Pearson's Test
                    # 3 - 

if __name__ == "__main__":
    option_test = input('Em qual teste será realizado a análise? \n 1. Teste 1 \n 2. Teste 2 \n 3. Teste 3 \n 4. Teste 4 \n>>')

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
    else:
        print('Opção inválida.')
        exit()
    
    # Checks if the results folder to be analyzed exists.
    PATH_DIRECTORY_READ = Path().absolute() / name_folder_read
    if(PATH_DIRECTORY_READ.exists()):
        files_read = PATH_DIRECTORY_READ.glob('*.csv')
    else:
        print('Pasta de resultado não existe.')
        exit()

    # Checks if you already have a folder for analysis, if not, one is created.
    PATH_ANALYZES = path_tests.parent / 'Analyzes'
    if(not PATH_ANALYZES.exists()):
        os.mkdir(PATH_ANALYZES)


    # General analysis
    COLUMNS_ANALYSIS = ['Subject', 'Ages', 'Ages GAP', 'Age Before GAP', 'Age After GAP', 'Results', 'Average Result', 'Recognized', 'Total Comparisons', 'Average (3)', 'Difference Average (3)', 'Average (4)', 'Difference Average (4)', 'Average (5)', 'Difference Average (5)', 'Years']
    PATH_GENERAL_ANALYSIS = PATH_ANALYZES / 'GeneralAnalysis'
    if(not PATH_GENERAL_ANALYSIS.exists()):
        os.mkdir(PATH_GENERAL_ANALYSIS)
        os.mkdir(PATH_GENERAL_ANALYSIS / option_folder)
    else:
        if(not (PATH_GENERAL_ANALYSIS / option_folder).exists()):
            os.mkdir(PATH_GENERAL_ANALYSIS / option_folder)
    
    PATH_WRITE_ANALYSIS = PATH_GENERAL_ANALYSIS / option_folder

    path_files = []
    for file in files_read:
        path_files.append(str(file))

    for recognizer in models_recognition:
        results = pandas.DataFrame(columns=COLUMNS_ANALYSIS)
        k = 0
        for file in path_files:
            recognized = 0
            first_age = True
            results_recognizer = []
            ages, ages_gap= [], []
            years = []
            dif_3, dif_4, dif_5 = [], [], []
            age_before, age_after = 0, 0
            average_3, average_4, average_5 = [], [], []

            csv_file = pandas.read_csv(file)

            if(option_test == '1' or option_test == '2'):
                born_year = int(csv_file[COLUMNS_READ[0]][0][5:9])
                subject = csv_file[COLUMNS_READ[0]][0][0:4]
                for i in range(len(csv_file)):
                    age = csv_file[COLUMNS_READ[1]][i] - born_year
                    if age not in ages:
                        ages.append(age)
                    age = csv_file[COLUMNS_READ[3]][i] - born_year
                    if age not in ages:
                        ages.append(age)

                    year = csv_file[COLUMNS_READ[1]][i]
                    if year not in years:
                        years.append(year)
                    year = csv_file[COLUMNS_READ[3]][i]
                    if year not in years:
                        years.append(year)

                    if csv_file[COLUMNS_READ[6]][i] == recognizer:
                        results_recognizer.append(csv_file[COLUMNS_READ[7]][i])
                        if(csv_file[COLUMNS_READ[8]][i] == True):
                            recognized = recognized + 1
            else:
                subject = csv_file[COLUMNS_READ[0]][0][0:3]
                for i in range(len(csv_file)):
                    if csv_file[COLUMNS_READ[1]][i] not in ages:
                        ages.append(csv_file[COLUMNS_READ[1]][i])
                    if csv_file[COLUMNS_READ[3]][i] not in ages:
                        ages.append(csv_file[COLUMNS_READ[3]][i])
                    if csv_file[COLUMNS_READ[6]][i] == recognizer:
                        results_recognizer.append(csv_file[COLUMNS_READ[7]][i])
                        if(csv_file[COLUMNS_READ[8]][i] == True):
                            recognized = recognized + 1
                years = ages

            for i in range(len(results_recognizer)-2):
                average_3.append(sum(results_recognizer[i:i+3])/len(results_recognizer[i:i+3]))
                if(i > 0):
                    dif_3.append(average_3[i]-average_3[i-1])
            for i in range(len(results_recognizer)-3):
                average_4.append(sum(results_recognizer[i:i+4])/len(results_recognizer[i:i+4]))
                if(i > 0):
                    dif_4.append(average_4[i]-average_4[i-1])
            for i in range(len(results_recognizer)-4):
                average_5.append(sum(results_recognizer[i:i+5])/len(results_recognizer[i:i+5]))
                if(i > 0):
                    dif_5.append(average_5[i]-average_5[i-1])

            for i in range(1, len(ages)):
                if len(ages_gap) != 0:
                    if(ages[i]-ages[i-1] >= max(ages_gap)):
                        age_before = ages[i-1]
                        age_after = ages[i]
                else:
                    age_before = ages[i-1]
                    age_after = ages[i]
                ages_gap.append(ages[i]-ages[i-1])
            
            results.loc[k] = [subject, ages, ages_gap, age_before, age_after, results_recognizer, np.mean(np.asarray(results_recognizer)), recognized, len(results_recognizer), average_3, dif_3, average_4, dif_4, average_5, dif_5, years]
            k = k + 1
        name_csv = recognizer +'.csv'
        path_csv = PATH_WRITE_ANALYSIS / name_csv
        results.to_csv(path_csv)


    # Clusters
    PATH_CLUSTERS = PATH_ANALYZES / 'Clusters'
    if(not PATH_CLUSTERS.exists()):
        os.mkdir(PATH_CLUSTERS)
        os.mkdir(PATH_CLUSTERS / option_folder)
    else:
        if(not (PATH_CLUSTERS / option_folder).exists()):
            os.mkdir(PATH_CLUSTERS / option_folder)
    
    PATH_WRITE_CLUSTERS = PATH_CLUSTERS / option_folder
    files_read_analysis = PATH_WRITE_ANALYSIS.glob('*.csv')

    for file in files_read_analysis:
        cluster_1 = pandas.DataFrame(columns=COLUMNS_ANALYSIS)
        cluster_2 = pandas.DataFrame(columns=COLUMNS_ANALYSIS)
        cluster_3 = pandas.DataFrame(columns=COLUMNS_ANALYSIS)
        cluster_4 = pandas.DataFrame(columns=COLUMNS_ANALYSIS)

        csv_file = pandas.read_csv(file)

        for i in range(len(csv_file)):
            data = [int(item) for item in csv_file[COLUMNS_ANALYSIS[2]][i][csv_file[COLUMNS_ANALYSIS[2]][i].index('[') + 1:csv_file[COLUMNS_ANALYSIS[2]][i].index(']')].strip().split(", ")]
            line = [csv_file[COLUMNS_ANALYSIS[0]][i], csv_file[COLUMNS_ANALYSIS[1]][i], csv_file[COLUMNS_ANALYSIS[2]][i], csv_file[COLUMNS_ANALYSIS[3]][i], csv_file[COLUMNS_ANALYSIS[4]][i], csv_file[COLUMNS_ANALYSIS[5]][i], csv_file[COLUMNS_ANALYSIS[6]][i], csv_file[COLUMNS_ANALYSIS[7]][i], csv_file[COLUMNS_ANALYSIS[8]][i], csv_file[COLUMNS_ANALYSIS[9]][i], csv_file[COLUMNS_ANALYSIS[10]][i], csv_file[COLUMNS_ANALYSIS[11]][i], csv_file[COLUMNS_ANALYSIS[12]][i], csv_file[COLUMNS_ANALYSIS[13]][i], csv_file[COLUMNS_ANALYSIS[14]][i], csv_file[COLUMNS_ANALYSIS[15]][i]]
            if(max(data) <= 15):
                cluster_1.loc[len(cluster_1)] = line
            elif(max(data) <= 30):
                cluster_2.loc[len(cluster_2)] = line
            elif(max(data) <= 45):
                cluster_3.loc[len(cluster_3)] = line
            else:
                cluster_4.loc[len(cluster_4)] = line

        name_file = str(file)
        for models in models_recognition:
            if models in name_file:
                model = models
        name_csv_1 = '00_15_' + model + '.csv'
        cluster_1.to_csv(PATH_WRITE_CLUSTERS / name_csv_1)
        name_csv_2 = '16_30_' + model + '.csv'
        cluster_2.to_csv(PATH_WRITE_CLUSTERS / name_csv_2)
        name_csv_3 = '31_45_' + model + '.csv'
        cluster_3.to_csv(PATH_WRITE_CLUSTERS / name_csv_3)
        name_csv_4 = '46_--_' + model + '.csv'
        cluster_4.to_csv(PATH_WRITE_CLUSTERS / name_csv_4)

    
    # Residue Analysis
    COLUMNS_RESIDUE = ['Subject', 'Recognition Model', 'Results', 'Residue', 'Absolute Residue']
    PATH_RESIDUE = PATH_ANALYZES / 'Residues'
    if(not PATH_RESIDUE.exists()):
        os.mkdir(PATH_RESIDUE)

    results = pandas.DataFrame(columns=COLUMNS_RESIDUE)
    k = 0
    for file in path_files:
        for recognizer in models_recognition:
            results_recognizer = []

            csv_file = pandas.read_csv(file)

            if(option_test == '1' or option_test == '2'):
                subject = csv_file[COLUMNS_READ[0]][0][0:4]
            else:
                subject = csv_file[COLUMNS_READ[0]][0][0:3]
            for i in range(len(csv_file)):
                if csv_file[COLUMNS_READ[6]][i] == recognizer:
                    results_recognizer.append(csv_file[COLUMNS_READ[7]][i])
            
            difference = np.diff(np.asarray(results_recognizer))
            residue = np.sum(difference)
            abs_residue = np.sum(np.absolute(difference))

            results.loc[k] = [subject, recognizer, results_recognizer, residue, abs_residue]
            k = k + 1
    name_csv = option_folder + '.csv'
    path_csv = PATH_RESIDUE / name_csv
    results.to_csv(path_csv)


    # Single Result
    PATH_SINGLE_RESULT = PATH_ANALYZES / 'SingleResult'
    if(not PATH_SINGLE_RESULT.exists()):
        os.mkdir(PATH_SINGLE_RESULT)
    COLUMNS_WRITE_SINGLE_RESULT = ['Recognition Model', 'Average Result', 'Average Recognition']
    
    files_read_single_result = PATH_WRITE_ANALYSIS.glob('*.csv')

    path_files = []
    for file in files_read_single_result:
        path_files.append(str(file))
    
    k = 0
    results = pandas.DataFrame(columns=COLUMNS_WRITE_SINGLE_RESULT)
    for file in path_files:
        average = 0
        results_recognizer = []
        correct_recognitions = []
        total_recognitions = []

        csv_file = pandas.read_csv(file)
        for i in range(len(csv_file)):
            results_recognizer.append(csv_file[COLUMNS_ANALYSIS[6]][i])
            correct_recognitions.append(csv_file[COLUMNS_ANALYSIS[7]][i])
            total_recognitions.append(csv_file[COLUMNS_ANALYSIS[8]][i])

        name_file = str(file)
        for models in models_recognition:
            if models in name_file:
                model = models
        results.loc[k] = [model, np.mean(np.asarray(results_recognizer)), sum(correct_recognitions)/sum(total_recognitions)]
        k = k + 1
    name_csv = option_folder + '.csv'
    path_csv = PATH_SINGLE_RESULT / name_csv
    results.to_csv(path_csv)

    # Normality Tests
    PATH_NORMALITY = PATH_ANALYZES / 'Normality'
    if(not PATH_NORMALITY.exists()):
        os.mkdir(PATH_NORMALITY)
    
    files_read_normality = PATH_WRITE_ANALYSIS.glob('*.csv')

    final_vector = {}
    path_files = []
    for file in files_read_normality:
        path_files.append(str(file))

    for file in path_files:
        average_result = []

        csv_file = pandas.read_csv(file)
        for i in range(len(csv_file)):
            average_result.append(csv_file[COLUMNS_ANALYSIS[6]][i])

        name_file = str(file)
        for models in models_recognition:
            if models in name_file:
                model = models

        if(normality_test == 1):
            # Shapiro-Wilk Test
            # normality test
            stat, p = shapiro(average_result)
            print('Statistics=%.3f, p=%.3f' % (stat, p))
            # interpret
            alpha = 0.05
            if p > alpha:
                print('Sample looks Gaussian (fail to reject H0)')
                print(model)
                final_vector[model] = True
            else:
                print('Sample does not look Gaussian (reject H0)')
                print(model)
                final_vector[model] = False

        elif(normality_test == 2):
            # D'Agostino and Pearson's Test
            # normality test
            stat, p = normaltest(average_result)
            print('Statistics=%.3f, p=%.3f' % (stat, p))
            # interpret
            alpha = 0.05
            if p > alpha:
                print('Sample looks Gaussian (fail to reject H0)')
                print(model)
                final_vector[model] = True
            else:
                print('Sample does not look Gaussian (reject H0)')
                print(model)
                final_vector[model] = False

        else:
            # Anderson-Darling Test
            # normality test
            result = anderson(average_result)
            print('Statistic: %.3f' % result.statistic)
            p = 0
            for i in range(len(result.critical_values)):
                sl, cv = result.significance_level[i], result.critical_values[i]
                if result.statistic < result.critical_values[i]:
                    print('%.3f: %.3f, data looks normal (fail to reject H0)' % (sl, cv))
                    print(model)
                    final_vector[model] = True
                else:
                    print('%.3f: %.3f, data does not look normal (reject H0)' % (sl, cv))
                    print(model)
                    final_vector[model] = False

    name_txt = option_folder + '-NormalityTest.txt'
    path_txt = PATH_NORMALITY / name_txt
    with open(path_txt, 'w') as txt_file:
        txt_file.write(str(final_vector))
    