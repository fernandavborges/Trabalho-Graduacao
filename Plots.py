from pathlib import Path
import pandas
import numpy as np
import matplotlib.pyplot as plt
import shutil
import os

thresholds = {
    'VGG-Face':0.4, 
    'Facenet':0.4, 
    'Facenet512':0.3, 
    'OpenFace':0.1, 
    'DeepFace':0.23, 
    'DeepID':0.015, 
    'ArcFace':0.68, 
    'Dlib':0.7, 
    'SFace':0.5932763306134152
}

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

    option_test = input('Em qual teste será realizado o plot? \n 1. Teste 1 \n 2. Teste 2 \n 3. Teste 3 \n 4. Teste 4 \n>>')
    
    if(option_test == '1'):
        PATH_ANALYZES = Path().absolute() / 'Test-1/Analyzes/'
        print('Pasta de resultados disponíveis no Test-1:')
        for path in (PATH_ANALYZES / 'Residues').iterdir():
            if path.is_file() and (str(path).find('Analyzes\Residues')!=-1):
                path_str = str(path)
                print('-', path_str[path_str.index('Residues')+len('Residues/'):-4], '\n')
        option_folder = input('Qual a pasta de resultados será analisada? (ex: Test1A): ')
    elif(option_test == '2'):
        PATH_ANALYZES = Path().absolute() / 'Test-2/Analyzes/'
        print('Pasta de resultados disponíveis no Test-2:')
        for path in (PATH_ANALYZES / 'Residues').iterdir():
            if path.is_file() and (str(path).find('Analyzes\Residues')!=-1):
                path_str = str(path)
                print('-', path_str[path_str.index('Residues')+len('Residues/'):-4], '\n')
        option_folder = input('Qual a pasta de resultados será analisada? (ex: Test1A): ')
    elif(option_test == '3'):
        PATH_ANALYZES = Path().absolute() / 'Test-3/Analyzes/'
        print('Pasta de resultados disponíveis no Test-3:')
        for path in (PATH_ANALYZES / 'Residues').iterdir():
            if path.is_file() and (str(path).find('Analyzes\Residues')!=-1):
                path_str = str(path)
                print('-', path_str[path_str.index('Residues')+len('Residues/'):-4], '\n')
        option_folder = input('Qual a pasta de resultados será analisada? (ex: Test1A): ')
    elif(option_test == '4'):
        PATH_ANALYZES = Path().absolute() / 'Test-4/Analyzes/'
        print('Pasta de resultados disponíveis no Test-4:')
        for path in (PATH_ANALYZES / 'Residues').iterdir():
            if path.is_file() and (str(path).find('Analyzes\Residues')!=-1):
                path_str = str(path)
                print('-', path_str[path_str.index('Residues')+len('Residues/'):-4], '\n')
        option_folder = input('Qual a pasta de resultados será analisada?(ex: Test1A): ')
    else:
        print('Opçao inválida.')
        exit()

    if(not (PATH_ANALYZES/'Residues'/(option_folder+'.csv')).exists()):
        print('Pasta de resultado não existe.')
        exit()

    PATH_PLOT = PATH_ANALYZES / 'Plots'
    if(not PATH_PLOT.exists()):
        os.mkdir(PATH_PLOT)

    option_plot = input('Qual plotagem será realizada? \n 1. Plot de resultados por sujeito/modelo.\n 2. Plot de médias de resultados por modelo. \n 3. Plot de Clusters. \n 4. Plot de Resíduos. \n>>')

    if(option_plot == '1'):
        COLUMNS_ANALYSIS = ['Subject', 'Ages', 'Ages GAP', 'Age Before GAP', 'Age After GAP', 'Results', 'Average Result', 'Recognized', 'Total Comparisons', 'Average (3)', 'Difference Average (3)', 'Average (4)', 'Difference Average (4)', 'Average (5)', 'Difference Average (5)', 'Years']
        PATH_READ = PATH_ANALYZES / 'GeneralAnalysis' / option_folder
        if(PATH_READ.exists()):
            files_read = PATH_READ.glob('*.csv')
        else:
            print('Pasta de resultado não existe.')
            exit()

        PATH_RESULTS = PATH_PLOT / 'Results'
        if(not PATH_RESULTS.exists()):
            os.mkdir(PATH_RESULTS)

        PATH_WRITE = PATH_RESULTS / option_folder
        if(PATH_WRITE.exists()):
            shutil.rmtree(PATH_WRITE)
        os.mkdir(PATH_WRITE)

        for file in files_read:
            name_file = str(file)
            for model in models_recognition:
                if model in name_file:
                    name_model = model
            csv_file = pandas.read_csv(file)
            for i in range(len(csv_file)):
                results_recognizer = [float(item) for item in csv_file[COLUMNS_ANALYSIS[5]][i][csv_file[COLUMNS_ANALYSIS[5]][i].index('[') + 1:csv_file[COLUMNS_ANALYSIS[5]][i].index(']')].strip().split(", ")]
                year = [int(item) for item in csv_file[COLUMNS_ANALYSIS[15]][i][csv_file[COLUMNS_ANALYSIS[15]][i].index('[') + 1:csv_file[COLUMNS_ANALYSIS[15]][i].index(']')].strip().split(", ")]
                subject = csv_file[COLUMNS_ANALYSIS[0]][i]

                plt.figure()
                plt.xlabel("Anos")
                plt.ylabel("Distâncias")
                plt.title("Sujeito: "+ subject + ". Modelo: " + name_model + ".")
                plt.bar(year[:-1], results_recognizer)
                plt.plot([year[0], year[-1]], [thresholds[name_model], thresholds[name_model]], "-", color='b', label='Limite')
                name_plot = PATH_WRITE /  (subject + '-' + name_model)
                plt.savefig(name_plot)
                #plt.show()
                plt.close()

    elif(option_plot == '2'):
        COLUMNS_READ = ['Subject', 'Ages', 'Ages GAP', 'Age Before GAP', 'Age After GAP', 'Results', 'Average Result', 'Recognized', 'Total Comparisons', 'Average (3)', 'Difference Average (3)', 'Average (4)', 'Difference Average (4)', 'Average (5)', 'Difference Average (5)', 'Years']
        PATH_READ = PATH_ANALYZES / 'GeneralAnalysis' / option_folder
        if(PATH_READ.exists()):
            files_read = PATH_READ.glob('*.csv')
        else:
            print('Pasta de resultado não existe.')
            exit()
        
        PATH_AVERAGE = PATH_PLOT / 'Averages'
        if(not PATH_AVERAGE.exists()):
            os.mkdir(PATH_AVERAGE)

        PATH_WRITE = PATH_AVERAGE / option_folder
        if(PATH_WRITE.exists()):
            shutil.rmtree(PATH_WRITE)
        os.mkdir(PATH_WRITE)

        option = input('\nComo plotar os gráficos?\n 1. Evidenciando a média\n 2. Evidenciando os sujeitos \n>>')
        if(option != '1' and option != '2'):
            print('Opção inválida.')
            exit()
        for file in files_read:
            name_file = str(file)
            for model in models_recognition:
                if model in name_file:
                    name_model = model
            average_3, average_4, average_5 = [], [], []
            csv_file = pandas.read_csv(file)
            if(len(csv_file) != 0):
                figure, axs = plt.subplots(3, 1, sharex=False, sharey=False)
                plt.rcParams.update({'font.size': 15})
                plt.rcParams['xtick.labelsize'] = 15
                plt.rcParams['ytick.labelsize'] = 15
                if(option == '2'):
                    if(len(csv_file) <= 10): 
                        figure.set_figwidth(15)
                        figure.set_figheight(25)
                    elif(len(csv_file) < 20): 
                        figure.set_figwidth(25)
                        figure.set_figheight(30)
                    else:
                        figure.set_figwidth(35)
                        figure.set_figheight(40)
                else:
                    figure.set_figwidth(15)
                    figure.set_figheight(25)
                axs[0].set_title(option_folder + ' - '+ name_model + ' - Average 3')
                axs[1].set_title(option_folder + ' - '+ name_model + ' - Average 4')
                axs[2].set_title(option_folder + ' - '+ name_model + ' - Average 5')
                axs[0].set_xlabel('Média nº')
                axs[1].set_xlabel('Média nº')
                axs[2].set_xlabel('Média nº')
                axs[0].set_ylabel("Distâncias")
                axs[1].set_ylabel("Distâncias")
                axs[2].set_ylabel("Distâncias")

                for i in range(len(csv_file)):
                    subject = csv_file[COLUMNS_READ[0]][i]
                    plot_3 = [float(item) for item in csv_file[COLUMNS_READ[9]][i][csv_file[COLUMNS_READ[9]][i].index('[') + 1:csv_file[COLUMNS_READ[9]][i].index(']')].strip().split(", ")]
                    plot_4 = [float(item) for item in csv_file[COLUMNS_READ[11]][i][csv_file[COLUMNS_READ[11]][i].index('[') + 1:csv_file[COLUMNS_READ[11]][i].index(']')].strip().split(", ")]
                    plot_5 = [float(item) for item in csv_file[COLUMNS_READ[13]][i][csv_file[COLUMNS_READ[13]][i].index('[') + 1:csv_file[COLUMNS_READ[13]][i].index(']')].strip().split(", ")]

                    if(option == '1'):
                        axs[0].plot(range(len(plot_3)), plot_3, color='grey', linewidth=1.0)
                        axs[1].plot(range(len(plot_4)), plot_4, color='grey', linewidth=1.0)
                        axs[2].plot(range(len(plot_5)), plot_5, color='grey', linewidth=1.0)
                    else:
                        axs[0].plot(range(len(plot_3)), plot_3, label=subject)
                        axs[1].plot(range(len(plot_4)), plot_4, label=subject)
                        axs[2].plot(range(len(plot_5)), plot_5, label=subject)

                    average_3.append(plot_3)
                    average_4.append(plot_4)
                    average_5.append(plot_5)
                
                if(option == '1'):
                    plot_av_3 = np.sum(average_3, axis=0)/len(average_3)
                    plot_av_4 = np.sum(average_4, axis=0)/len(average_4)
                    plot_av_5 = np.sum(average_5, axis=0)/len(average_5)

                    axs[0].plot(range(len(plot_av_3)), plot_av_3, label='Média', color='black', linewidth=3.0)
                    axs[1].plot(range(len(plot_av_4)), plot_av_4, label='Média', color='black', linewidth=3.0)
                    axs[2].plot(range(len(plot_av_5)), plot_av_5, label='Média', color='black', linewidth=3.0)

                axs[0].legend()
                axs[1].legend()
                axs[2].legend()
                if(option == '1'):
                    name_fig = option_folder + ' - '+ name_model + '-Average'
                else:       
                    name_fig = option_folder + ' - '+ name_model
                name_plot = PATH_WRITE / name_fig
                figure.savefig(name_plot)
                figure.clear()


    elif(option_plot == '3'):
        COLUMNS_READ = ['Subject', 'Ages', 'Ages GAP', 'Age Before GAP', 'Age After GAP', 'Results', 'Average Result', 'Recognized', 'Total Comparisons', 'Average (3)', 'Difference Average (3)', 'Average (4)', 'Difference Average (4)', 'Average (5)', 'Difference Average (5)', 'Years']
        PATH_READ = PATH_ANALYZES / 'Clusters' / option_folder
        if(PATH_READ.exists()):
            files_read = PATH_READ.glob('*.csv')
        else:
            print('Pasta de resultado clusters não existe.')
            exit()

        option = input('\nComo plotar os gráficos?\n 1. Evidenciando a média\n 2. Evidenciando os sujeitos \n>>')
        if(option != '1' and option != '2'):
            print('Opção inválida.')
            exit()
        for file in files_read:
            name_file = str(file)
            average_3, average_4, average_5 = [], [], []
            csv_file = pandas.read_csv(file)

            for model in models_recognition:
                if model in name_file:
                    name_model = model

            if(len(csv_file) != 0):
                figure, axs = plt.subplots(3, 1, sharex=False, sharey=False)
                plt.rcParams.update({'font.size': 15})
                plt.rcParams['xtick.labelsize'] = 15
                plt.rcParams['ytick.labelsize'] = 15
                if(option == '2'):
                    if(len(csv_file) <= 10): 
                        figure.set_figwidth(15)
                        figure.set_figheight(25)
                    elif(len(csv_file) < 20): 
                        figure.set_figwidth(25)
                        figure.set_figheight(30)
                    else:
                        figure.set_figwidth(35)
                        figure.set_figheight(40)
                else:
                    figure.set_figwidth(15)
                    figure.set_figheight(25)
                axs[0].set_title('Cluster ' + name_file[name_file.index(name_model)-6:-4] + ' - Average 3')
                axs[1].set_title('Cluster ' + name_file[name_file.index(name_model)-6:-4] + ' - Average 4')
                axs[2].set_title('Cluster ' + name_file[name_file.index(name_model)-6:-4] + ' - Average 5')
                axs[0].set_xlabel('Média nº')
                axs[1].set_xlabel('Média nº')
                axs[2].set_xlabel('Média nº')
                axs[0].set_ylabel("Distâncias (% do Threshold)")
                axs[1].set_ylabel("Distâncias (% do Threshold)")
                axs[2].set_ylabel("Distâncias (% do Threshold)")

                for i in range(len(csv_file)):
                    subject = csv_file[COLUMNS_READ[0]][i]
                    plot_3 = [float(item) for item in csv_file[COLUMNS_READ[9]][i][csv_file[COLUMNS_READ[9]][i].index('[') + 1:csv_file[COLUMNS_READ[9]][i].index(']')].strip().split(", ")]
                    plot_3 = [x * 100/ thresholds[name_model] for x in plot_3]
                    plot_4 = [float(item) for item in csv_file[COLUMNS_READ[11]][i][csv_file[COLUMNS_READ[11]][i].index('[') + 1:csv_file[COLUMNS_READ[11]][i].index(']')].strip().split(", ")]
                    plot_4 = [x * 100/ thresholds[name_model] for x in plot_4]
                    plot_5 = [float(item) for item in csv_file[COLUMNS_READ[13]][i][csv_file[COLUMNS_READ[13]][i].index('[') + 1:csv_file[COLUMNS_READ[13]][i].index(']')].strip().split(", ")]
                    plot_5 = [x * 100/ thresholds[name_model] for x in plot_5]

                    if(option == '1'):
                        axs[0].plot(range(len(plot_3)), plot_3, color='grey', linewidth=1.0)
                        axs[1].plot(range(len(plot_4)), plot_4, color='grey', linewidth=1.0)
                        axs[2].plot(range(len(plot_5)), plot_5, color='grey', linewidth=1.0)
                    else:
                        axs[0].plot(range(len(plot_3)), plot_3, label=subject)
                        axs[1].plot(range(len(plot_4)), plot_4, label=subject)
                        axs[2].plot(range(len(plot_5)), plot_5, label=subject)

                    average_3.append(plot_3)
                    average_4.append(plot_4)
                    average_5.append(plot_5)
                
                if(option == '1'):
                    plot_av_3 = np.sum(average_3, axis=0)/len(average_3)
                    plot_av_4 = np.sum(average_4, axis=0)/len(average_4)
                    plot_av_5 = np.sum(average_5, axis=0)/len(average_5)

                    axs[0].plot(range(len(plot_av_3)), plot_av_3, label='Média', color='black', linewidth=3.0)
                    axs[1].plot(range(len(plot_av_4)), plot_av_4, label='Média', color='black', linewidth=3.0)
                    axs[2].plot(range(len(plot_av_5)), plot_av_5, label='Média', color='black', linewidth=3.0)

                axs[0].legend()
                axs[1].legend()
                axs[2].legend()
                if(option == '1'):
                    name_fig = name_file[name_file.index(name_model)-6:-4] + '-Average'
                else:       
                    name_fig = name_file[name_file.index(name_model)-6:-4]
                name_plot = PATH_READ / name_fig
                figure.savefig(name_plot)
                figure.clear()

    elif(option_plot == '4'):
        COLUMNS_READ = ['Subject', 'Recognition Model', 'Results', 'Residue', 'Absolute Residue']
        file = option_folder + '.csv'
        PATH_READ = PATH_ANALYZES / 'Residues' / file 
        PATH_WRITE = PATH_READ.parent / 'Plots'

        if(not PATH_WRITE.exists()):
            os.mkdir(PATH_WRITE)
        
        csv_file = pandas.read_csv(PATH_READ)
        if(len(csv_file) != 0):
            for model in models_recognition:
                residues = []
                abs_residues = []
                for i in range(len(csv_file)):
                    if(csv_file[COLUMNS_READ[1]][i] == model):
                        residues.append(csv_file[COLUMNS_READ[3]][i]) 
                        abs_residues.append(csv_file[COLUMNS_READ[4]][i])       
                plt.figure(figsize=(20,15))
                plt.rcParams.update({'font.size': 15})
                plt.rcParams['xtick.labelsize'] = 15
                plt.rcParams['ytick.labelsize'] = 15
                plt.title('Histograma - ' + file[:-4] +'. Modelo: ' + model)
                plt.xlabel('Resíduo')
                plt.ylabel("Frequência")
                plt.hist(residues, 10, rwidth=0.9)
                name_fig = file[:-4] + '-' + model
                name_plot = PATH_WRITE / name_fig
                plt.savefig(name_plot)
                plt.clf()
                plt.title('Histograma - ' + file[:-4] +'. Modelo: ' + model + '- Absoluto')
                plt.hist(abs_residues, 10, rwidth=0.9)
                name_fig = file[:-4] + '-' + model + '-Absolute'
                name_plot = PATH_WRITE / name_fig
                plt.savefig(name_plot)

    else:
        print('Opçao inválida.')
        exit()