"""
    This script creates the image bank that will be used for Test 2.
"""

import os
from pathlib import Path
import random
import shutil

PATH_DIRECTORY_BD = Path().absolute().parents[0] / 'Banco-de-Imagens'
files = os.listdir(PATH_DIRECTORY_BD)

NEW_BD_PATH = Path().absolute() / 'BD'

# Subjects who did not admit the plastic and not even a specialist attested about
rejected_subjects = ['S077', 'S082']

subjects = []
n_subjects = 81 # final number of individuals to be selected

for file in files:
    if(file[0:4] not in subjects and file[0:4] not in rejected_subjects and file != '.gitignore'):
        subjects.append(file[0:4])

# randomly selects the desired amount among the available subjects
subjects.sort()
print('Subjects available: ', subjects)
random.seed()
selected = random.sample(subjects, k=n_subjects)
print('Subjects selected: ', selected)

for select in selected:
    images = []
    for file in files:
        if(file[0:4] == select):
            images.append(file)
    for i in range(len(images)):
        shutil.copy(PATH_DIRECTORY_BD / images[i], NEW_BD_PATH)