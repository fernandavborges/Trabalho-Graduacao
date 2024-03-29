import os
from pathlib import Path
import matplotlib.pyplot as plt
from pprint import pprint

# Databases
PATH_DIRECTORY_BD = Path('.') / '../C2FPW'
files_BD = os.listdir(PATH_DIRECTORY_BD)
PATH_DIRECTORY_FGNET = Path('.') / '../FGNET'
files_FGNET = os.listdir(PATH_DIRECTORY_FGNET)

# 'C2FPW' DataBase
amount_BD = []
first_subject = True
count = 0
for file in files_BD:
    if file != '.gitignore':
        if first_subject:
            subject = file[0:4]
            count = count + 1
            first_subject = False
        else:
            if(file[0:4] != subject):
                amount_BD.append(count)
                count = 1
                subject = file[0:4]
            else:
                count = count + 1
amount_BD.append(count)

frequency = {}
# iterating over the list
for item in amount_BD:
   # checking the element in dictionary
   if item in frequency:
      # incrementing the counr
      frequency[item] += 1
   else:
      # initializing the count
      frequency[item] = 1

# printing the frequency
pprint(frequency)

plt.title('Banco de Imagens - Fernanda e Liz')
plt.xlabel('Quantidade de Imagens por Pessoa')
plt.ylabel('Frequência')
plt.hist(amount_BD, 10, rwidth=0.9)
plt.xticks(range(min(amount_BD), max(amount_BD), 5))
name_plot = './Results/Histogram_BD'
plt.savefig(name_plot)
plt.show()

# 'FGNET' DataBase
amount_FGNET = []
first_subject = True
count = 0
for file in files_FGNET:
    if file != '.gitignore':
        if first_subject:
            subject = file[0:4]
            count = count + 1
            first_subject = False
        else:
            if(file[0:4] != subject):
                amount_FGNET.append(count)
                count = 1
                subject = file[0:4]
            else:
                count = count + 1
amount_FGNET.append(count)

frequency = {}
# iterating over the list
for item in amount_FGNET:
   # checking the element in dictionary
   if item in frequency:
      # incrementing the counr
      frequency[item] += 1
   else:
      # initializing the count
      frequency[item] = 1

# printing the frequency
pprint(frequency)

plt.title('Banco de Imagens - FGNET')
plt.xlabel('Quantidade de Imagens por Pessoa')
plt.ylabel('Frequência')
plt.hist(amount_FGNET, 10, rwidth=0.9)
plt.xticks(range(min(amount_FGNET), max(amount_FGNET), 2))
name_plot = './Results/Histogram_FGNET'
plt.savefig(name_plot)
plt.show()
