from pathlib import Path
import pandas
import numpy as np
import matplotlib.pyplot as plt


COLUMNS = ['Subject', 'Ages', 'Ages GAP', 'Age Before GAP', 'Age After GAP', 'Recognized', 'Total Comparisons', 'Average (3)', 'Difference Average (3)', 'Average (4)', 'Difference Average (4)', 'Average (5)', 'Difference Average (5)']

if __name__ == "__main__":

    option_test = input('Em qual teste será realizado o plot? \n 1. Teste 1 \n 2. Teste 2 \n 3. Teste 3 \n>>')
    
    if(option_test == '1'):
        path_tests = Path().absolute() / 'Test-1/Results/'
        print('Pasta de resultados disoníveis no Test-1:')
        for path in path_tests.iterdir():
            if path.is_dir() and (str(path).find('Results\Analyser')!=-1):
                path_str = str(path)
                print('-', path_str[path_str.index('Analyser-')+len('Analyser-'):], '\n')
        
        option_folder = input('Qual a pasta de resultados será analisada? (É preciso que esteja gerado a pasta de Analyser desses resultados)(ex: Test1A): ')
        name_folder = 'Test-1/Results/Analyser-' + option_folder
        PATH_DIRECTORY = Path().absolute() / name_folder

    elif(option_test == '2'):
        path_tests = Path().absolute() / 'Test-2/Results/'
        print('Pasta de resultados disoníveis no Test-2:')
        for path in path_tests.iterdir():
            if path.is_dir() and (str(path).find('Results\Analyser')!=-1):
                path_str = str(path)
                print('-', path_str[path_str.index('Analyser-')+len('Analyser-'):], '\n')
        option_folder = input('Qual a pasta de resultados será analisada? (É preciso que esteja gerado a pasta de Analyser desses resultados)(ex: Test1A): ')
        name_folder = 'Test-2/Results/Analyser-' + option_folder
        PATH_DIRECTORY = Path().absolute() / name_folder

    elif(option_test == '3'):
        path_tests = Path().absolute() / 'Test-3/Results/'
        print('Pasta de resultados disoníveis no Test-3:')
        for path in path_tests.iterdir():
            if path.is_dir() and (str(path).find('Results\Analyser')!=-1):
                path_str = str(path)
                print('-', path_str[path_str.index('Analyser-')+len('Analyser-'):], '\n')
        option_folder = input('Qual a pasta de resultados será analisada? (É preciso que esteja gerado a pasta de Analyser desses resultados)(ex: Test1A): ')
        name_folder = 'Test-3/Results/Analyser-' + option_folder
        PATH_DIRECTORY = Path().absolute() / name_folder
    else:
        print('Opçao inválida.')
        exit()

    if(PATH_DIRECTORY.exists()):
        files_read = PATH_DIRECTORY.glob('*.csv')
    else:
        print('Pasta de resultado analyser não existe.')
        exit()

    option = input('\nComo plotar os gráficos?\n 1. Evidenciando a média\n 2. Evidenciando os sujeitos \n>>')
    if(option != '1' and option != '2'):
        print('Opção inválida.')
        exit()
    for file in files_read:
        name_file = str(file)
        if name_file != 'Final.csv':
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
                axs[0].set_title(name_file[name_file.index('Analyser_'):-4] + ' - Average 3')
                axs[1].set_title(name_file[name_file.index('Analyser_'):-4] + ' - Average 4')
                axs[2].set_title(name_file[name_file.index('Analyser_'):-4] + ' - Average 5')
                axs[0].set_xlabel('Média nº')
                axs[1].set_xlabel('Média nº')
                axs[2].set_xlabel('Média nº')
                axs[0].set_ylabel("Distâncias")
                axs[1].set_ylabel("Distâncias")
                axs[2].set_ylabel("Distâncias")

                for i in range(len(csv_file)):
                    subject = csv_file[COLUMNS[0]][i]
                    plot_3 = [float(item) for item in csv_file[COLUMNS[7]][i][csv_file[COLUMNS[7]][i].index('[') + 1:csv_file[COLUMNS[7]][i].index(']')].strip().split(", ")]
                    plot_4 = [float(item) for item in csv_file[COLUMNS[9]][i][csv_file[COLUMNS[9]][i].index('[') + 1:csv_file[COLUMNS[9]][i].index(']')].strip().split(", ")]
                    plot_5 = [float(item) for item in csv_file[COLUMNS[11]][i][csv_file[COLUMNS[11]][i].index('[') + 1:csv_file[COLUMNS[11]][i].index(']')].strip().split(", ")]

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
                    name_fig = name_file[name_file.index('Analyser'):-4] + '-Average'
                else:       
                    name_fig = name_file[name_file.index('Analyser'):-4]
                name_plot = PATH_DIRECTORY.parent / name_fig
                figure.savefig(name_plot)
                figure.clear()
