import cv2
import numpy as np
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import QTimer, Qt, QSize


class QCamLabel(QLabel):
    """Extension Caméra + Détection de visage"""

    def __init__(self, arg, datalog):
        super().__init__(arg)
        self.arg = arg
        self.datalog = datalog

        self.cap = cv2.VideoCapture(1)  # Init de la caméra
        if self.cap.isOpened() == False:
            self.cap = cv2.VideoCapture(0)
        if self.cap.isOpened() == False:
            raise('Caméra non détecté')
        
        self.detection = False
        self.classCascades = list()  # Init des données de détection

        #  Création du Timer permettant l'actualisation de l'image  
        self.timer = QTimer() 
        self.timer.setInterval(10)
        self.timer.start()
        self.timer.timeout.connect(self.refresh)

        self.benoit = False

        self.face_center = list()
        self.maxSize = self.datalog.config["maxSize"]
        self.minSize = self.datalog.config["minSize"]
        self.minNeighbors = self.datalog.config["minNeighbors"]
        self.scaleFactor = self.datalog.config["scaleFactor"]

    def setMaxSize(self, arg):
        self.maxSize = (arg, arg)
        self.datalog.setMaxSize(arg)

    def setMinSize(self, arg):
        self.minSize = (arg, arg)
        self.datalog.setMinSize(arg)

    def setMinNeighbors(self, arg):
        self.minNeighbors = arg
        self.datalog.setMinNeighbors(arg)

    def setScaleFactor(self, arg):
        self.scaleFactor = arg/100.0
        self.datalog.setScaleFactor(arg/100.0)

    def toggleDetection(self):
        self.detection = not self.detection

    def refresh(self):  
        """ Récupére, convertit et affiche l'image de la WebCam """
        ret, image = self.cap.read()
        #image = np.array(([[255,255,255],[255,255,255],[255,255,255]],[[255,255,255],[255,255,255],[255,255,255]]))
        #print(image.shape)
        ret = True
        if ret is True:
            if self.detection:
                image = self.faceDetection(image)
                self.face_diretion()

            self.pixmap = self.npImageToQPixmap(image)
            print(self.size())
            size_with_marge = (self.size().width()-15, self.size().height())
            self.setPixmap(self.pixmap.scaled(QSize(*size_with_marge),
                                              aspectRatioMode=Qt.KeepAspectRatio))

    def face_diretion(self):
        if len(self.face_center) > 0:
            target = self.face_center[-1]
            deltaX = target[0] - self.center_image[0]
            deltaY = target[1] - self.center_image[1]
            self.datalog.setFaceDelta((deltaX,deltaY))

    def faceDetection(self, npImage):
        """ Détection de visage """
        gray = cv2.cvtColor(npImage, cv2.COLOR_BGR2GRAY)  # Convertion en niveau de gris
        faces = list()
        for classCascade in self.classCascades:

            face = classCascade.detectMultiScale( 
                gray,
                scaleFactor=self.datalog.config["scaleFactor"],
                minNeighbors=self.datalog.config["minNeighbors"],
                minSize=self.datalog.config["minSize"],
                flags=cv2.CASCADE_SCALE_IMAGE
            )
            if len(face) != 0:
                self.datalog.setTracking(True)
                for a in list(map(list, face)):
                    faces.append(a)  # Lancement de la detection 
            else : 
                self.datalog.setTracking(False)

        facesCoef = list()
        for (x, y, w, h) in faces:  # Affichage des visages
            facesCoef.append((w*h))
        
            cv2.rectangle(npImage, (x, y), (x+w, y+h), (0, 255, 0), 4)

        #  print(f"visage {faces} ")
        self.center_image = (len(npImage[1])//2,len(npImage)//2)
        if len(facesCoef) != 0:
            maxCoef = max(facesCoef)
            x, y, w, h = faces[facesCoef.index(maxCoef)]
            center = (x+w//2, y+h//2)
            self.face_center.append(center)
            cv2.line(npImage, center, self.center_image, (255,0,0), 10)
            cv2.circle(npImage, center, 10, (255,0,0), -1)
            cv2.rectangle(npImage, (x, y), (x+w, y+h), (255, 0, 0), 4)

        return npImage

    def npImageToQPixmap(self, npImage):
        """ Converti une image en format np.array (OpenCV) en QImage """
        qimage = QImage(npImage, npImage.shape[1], npImage.shape[0],                                                                                                                                                 
                        QImage.Format_RGB888)
        return QPixmap(qimage)
