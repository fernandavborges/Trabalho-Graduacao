# Graduation work - Fernanda e Liz
This repository is intended for the scripts used during the graduation work with the theme: "Analysis of the impact of surgical facial modifications on deep learning algorithms for facial recognition".

## Pre-requisites
To run the scripts, functions from the DeepFace library are used. Therefore, you need to install some libraries, which can be found in the requirements.txt file.

## Files and Directories
### Donwloader
Script used to download images from image banks directly from google drive to the server used for testing. Token and credentials for client-server communication with google drive are also stored in the folder.

### Banco-de-Imagens
The image bank created by the authors, with images of celebrities who declared having undergone facial plastic surgery or specialists, confirmed this information. The images were taken from the internet and are in the public domain, but they will not be stored here, and can be collected from the links that will be provided in the FOLDER WHERE THE LINKS WILL BE SAVED.

### FGNET


### HDA-PlasticSurgery

### Test 1
Test in the bank of images created by the authors "Banco-de-Imagens", taking randomly an X amount of subjects from the base and for each subject an N amount of images. The number X is defined according to the number of subjects that will be taken from the image bank that will be used to compare the results, in this case the FGNET. The value N is defined as the minimum number of images among the individuals in the databases to be compared. For the first test, 81 subjects from the base are used, with 8 images of each one, and the selection of images is carried out by taking the extremes of the lists of images.

### Test 2
Test on the image bank created by the authors "Banco-de-Imagens", randomly removing an X amount of subjects from the base and for each subject all the collected images. The number X is defined according to the number of subjects that will be removed from the image bank that will be used to compare the results, in this case the FGNET. For the first test, 81 subjects from the database are used.

### Test 3
Test on the image bank created by FGNET in order to use all individuals who have at least 8 images, thus leaving 81 subjects out of the 82 available in the image bank. From each of the subjects, 8 images are used, which are selected from the extremes of the image lists.

### Test 4
Test performed on the HDA-PlasticSurgery image bank, where recognition is performed on before and after images of individuals undergoing plastic surgery.


### Autors: 
Fernanda Vaz - fernandavazbc@gmail.com - Mechatronics Engineering - University of Brasilia (UnB)
Liz Carolina - lizcostato@gmail.com - Mechatronics Engineering - University of Brasilia (UnB)

## References
-   **[Deep Face - Serengil](https://github.com/serengil/deepface)**
-   Christian Rathgeb, Didem Dogan, Fabian Stockhardt, Maria De Marsico, Christoph Busch, „Plastic Surgery: An Obstacle for Deep Face Recognition?“, in 15th IEEE Computer Society Workshop on Biometrics (CVPRW), pp. 3510-3517, 2020.
