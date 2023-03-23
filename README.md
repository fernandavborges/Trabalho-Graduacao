# Graduation work - Fernanda e Liz
This repository is intended for the scripts used during the graduation work with the theme: "Analysis of the impact of surgical facial modifications on deep learning algorithms for facial recognition".

## Pre-requisites
To run the scripts, functions from the DeepFace library are used. Therefore, you need to install some libraries, which can be found in the requirements.txt file.

## Files and Directories
### Donwloader
Script used to download images from image banks directly from google drive to the server used for testing. Token and credentials for client-server communication with google drive are also stored in the folder.

### C2FPW
The image bank created by the authors, with images of celebrities who declared having undergone facial plastic surgery or specialists, confirmed this information. The images were taken from the internet and are in the public domain, but they will not be stored here, and can be collected from the links that will be provided in the FOLDER WHERE THE LINKS WILL BE SAVED.

### FGNET


### HDA-PlasticSurgery

### Test 1
Results from test in the bank of images created by the authors "C2FPW", taking randomly an X amount of subjects from the base and for each subject an N amount of images. The number X is defined according to the number of subjects that will be taken from the image bank that will be used to compare the results, in this case the FGNET. The value N is defined as the minimum number of images among the individuals in the databases to be compared. For the first test, 81 subjects from the base are used, with 8 images of each one, and the selection of images is carried out by taking the extremes of the lists of images.

### Test 2
Results from test on the image bank created by the authors "C2FPW", randomly removing an X amount of subjects from the base and for each subject all the collected images. The number X is defined according to the number of subjects that will be removed from the image bank that will be used to compare the results, in this case the FGNET. For the first test, 81 subjects from the database are used.

### Test 3
Results from test on the image bank created by FGNET in order to use all individuals who have at least 8 images, thus leaving 81 subjects out of the 82 available in the image bank. From each of the subjects, 8 images are used, which are selected from the extremes of the image lists.

### Test 4
Scripts and results from test performed on the HDA-PlasticSurgery image bank, where recognition is performed on before and after images of individuals undergoing plastic surgery.

### Analyser_Tests.py
Script performs the analysis of general information of the results of the folder indicated in the terminal. Among the information collected and saved in CSVs are: Subject, Ages, Ages GAP, Age Before GAP, Age After GAP, Recognized, Total Comparisons, Average (3), Difference Average (3), Average (4), Difference Average (4 ), Average (5), Difference Average (5). The results will be saved in a folder named like 'Analyser-TestXA' or 'Analyser-TestXB' with TestXA or TextXB matching the name of the analyzed results folder.

### BD_Tests.py
Script creates the image bank that will be used in test 1, 2 or 3. The image bank can be created in two ways: 1. Taking images by the extremities or 2. Taking images randomly.

### Cluster_Tests.py
Script performs the grouping of individuals with similar maximum age interval (gap) for a group analysis. The groupings are performed every 15 years and the CVS files with information on each cluster are saved in a folder with a name like Clusters-TestXA or Clusters-TestXB, where TestXA or TestXB represent the test results folder that will be grouped .

### Plot_Averages_Tests.py
Script generates images of the averages 3, 4 and 5 of the results found in the test in the indicated folder in the terminal. The name of the folder where the images will be saved will be of the type Images-TestXA-M3, Images-TestXA-M4, Images-TestXA-M5 or Images-TestXB-M3, Images-TestXB-M4, Images-TestXB-M5.

### Plot_Results_Tests.py
script generates images of the results found in the test in the indicated folder in the terminal. The name of the folder where the images will be saved will be Images-TestXA or Images-TestXB.

### Thread_Tests.py
Script intended to create the threads that will be responsible for running the recognition function in tests 1, 2 and 3. The results are saved in a folder corresponding to the test number indicated on the terminal. The folders will be of the type TestXA or TestXB, where X indicates the test number and the term A or B indicates the method of creation of the tested database, with A corresponding to the creation mode taking images of the extermos (extreme ages) and B corresponds to the creation mode taking random images from the base image bank.

## Autors: 
Fernanda Vaz - fernandavazbc@gmail.com - Mechatronics Engineering - University of Brasilia (UnB)
Liz Carolina - lizcostato@gmail.com - Mechatronics Engineering - University of Brasilia (UnB)

## References
-   **[Deep Face - Serengil](https://github.com/serengil/deepface)**
-   Christian Rathgeb, Didem Dogan, Fabian Stockhardt, Maria De Marsico, Christoph Busch, „Plastic Surgery: An Obstacle for Deep Face Recognition?“, in 15th IEEE Computer Society Workshop on Biometrics (CVPRW), pp. 3510-3517, 2020.
