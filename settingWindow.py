from PyQt5.QtWidgets import QMainWindow, QFileDialog, QListWidgetItem
from interface.ui_RecoFaceSettings import Ui_RecoFaceSettings
import cv2


class SettingWindows(QMainWindow, Ui_RecoFaceSettings):

    def __init__(self, camWindow, datalog): 
        super(SettingWindows, self).__init__() 
        super(Ui_RecoFaceSettings, self).__init__() 
        self.camWindow = camWindow
        self.setupUi(self)
        self.initConnect()


        self.datalog = datalog
        for file in self.datalog.config["classCascadesFiles"]:
            self.camWindow.classCascades.append(cv2.CascadeClassifier(file))
            item = QListWidgetItem(self.listWidget)
            item.setText(file.split("/")[-1])

        self.horizontalSlider_ScaleFactor.setProperty("value", self.datalog.config["scaleFactor"]*100)
        self.horizontalSlider_MinNeighbors.setProperty("value", self.datalog.config["minNeighbors"])
        self.horizontalSlider_MinSize.setProperty("value", self.datalog.config["minSize"])
        self.datalog.config["maxSize"]

    def initConnect(self):
        self.horizontalSlider_MaxSize.valueChanged.connect(self.camWindow.setMaxSize)
        self.horizontalSlider_MinSize.valueChanged.connect(self.camWindow.setMinSize)
        self.horizontalSlider_ScaleFactor.valueChanged.connect(self.camWindow.setScaleFactor)
        self.horizontalSlider_MinNeighbors.valueChanged.connect(self.camWindow.setMinNeighbors)

        self.checkBox_detectionState.toggled['bool'].connect(self.camWindow.toggleDetection)

        self.pushButton_Ajouter.clicked.connect(self.openFile)
        self.pushButton_Supprimer.clicked.connect(self.removeFile)

    def openFile(self):

        file = QFileDialog.getOpenFileName(self, "Ouvrir fichier bibliothèque", filter="*.xml")[0]
        if len(file) != 0:
            self.camWindow.classCascades.append(cv2.CascadeClassifier(file))
            self.datalog.addClassCascadesFiles(file)
            print(file)
            item = QListWidgetItem(self.listWidget)
            item.setText(file.split("/")[-1])

    def removeFile(self):
        try:
            indexItem = self.listWidget.currentRow()
            self.listWidget.takeItem(indexItem)
            del self.camWindow.classCascades[indexItem]
            self.datalog.removeClassCascadesFilesByIndex(indexItem)
        except IndexError as err:
            print(err)


