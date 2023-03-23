"""
    Test with the MediaPipe face detector directly from the mediapipe library==0.8.9.1.
"""
import mediapipe 
import cv2
import os

pasta = '../C2FPW/'
imagens = os.listdir(pasta)
arquivo_txt = open("Logs/mediapipe_failures.txt", "w")
imagens_falhas = []

mp_face_detection = mediapipe.solutions.face_detection
face_detector =  mp_face_detection.FaceDetection( min_detection_confidence = 0.6)

for imagem in imagens: 
    print('Image ' + imagem) 
    img = cv2.imread('../C2FPW/' + imagem)
    results = face_detector.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    if not results.detections:
        imagens_falhas.append(imagem)
        print('Detection Failure.')

arquivo_txt.write('Images not detected with detection model - MediaPipe')
arquivo_txt.write('\n')
for im in imagens_falhas:
    arquivo_txt.write(im)
    arquivo_txt.write('\n')
arquivo_txt.write('\n')