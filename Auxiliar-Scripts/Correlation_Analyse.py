from pathlib import Path
import pandas
import statistics
from scipy.stats.stats import pearsonr  

PATH_DIRECTORY_READ = Path().absolute() / 'Test-1/Results/Analyser/Analyser_ArcFace.csv'
COLUMNS = ['Subject', 'Ages', 'Ages GAP', 'Age Before GAP', 'Age After GAP', 'Recognized', 'Total Comparisons', 'Average (3)', 'Difference Average (3)', 'Average (4)', 'Difference Average (4)', 'Average (5)', 'Difference Average (5)']

correlations_average_bd = []
correlations_max_bd = []

csv_file = pandas.read_csv(PATH_DIRECTORY_READ)

for i in range(len(csv_file)):
    data = [int(item) for item in csv_file[COLUMNS[2]][i][csv_file[COLUMNS[2]][i].index('[') + 1:csv_file[COLUMNS[2]][i].index(']')].strip().split(", ")]
    average = statistics.mean(data)
    maximum = max(data)
    correlations_average_bd.append(average)
    correlations_max_bd.append(maximum)

print('Average GAP - Test 1: ', sorted(correlations_average_bd), '\n')
print('Maximum GAP - Test 1: ', sorted(correlations_max_bd), '\n')
        

PATH_DIRECTORY_READ = Path().absolute() / 'Test-3/Results/Analyser/Analyser_ArcFace.csv'

correlations_average_fgnet = []
correlations_max_fgnet = []

csv_file = pandas.read_csv(PATH_DIRECTORY_READ)

for i in range(len(csv_file)):
    data = [int(item) for item in csv_file[COLUMNS[2]][i][csv_file[COLUMNS[2]][i].index('[') + 1:csv_file[COLUMNS[2]][i].index(']')].strip().split(", ")]
    average = statistics.mean(data)
    maximum = max(data)
    correlations_average_fgnet.append(average)
    correlations_max_fgnet.append(maximum)

print('Average GAP - Test 3: ', sorted(correlations_average_fgnet), '\n')
print('Maximum GAP - Test 3: ', sorted(correlations_max_fgnet), '\n')

print('Correlation - Average')
print(pearsonr(correlations_average_bd[:80], correlations_average_fgnet))
#print(np.correlate(correlations_average_bd, correlations_average_fgnet))

print('Correlation - Maximum')
print(pearsonr(correlations_max_bd[:80], correlations_max_fgnet))