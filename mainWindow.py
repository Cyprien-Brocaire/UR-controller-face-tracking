from PyQt5.QtWidgets import (QMainWindow, QLabel, QPushButton, QWidget, QLineEdit, 
                             QHBoxLayout, QVBoxLayout)
from PyQtExtension.QtWidgetExtension import QCamLabel
from PyQt5.QtCore import QTimer, QSize
from settingWindow import SettingWindows
from interface.ui_mainWindow import Ui_MainWindow
from data import DataModel
import sys
from URcontroller import URobot
import URBasic
import pickle
from math import degrees

host = "192.168.0.37"   #E.g. a Universal Robot offline simulator, please adjust to match your IP
acc = 0.3
vel = 0.3

unconnect_mode = False

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self): 
        super(MainWindow, self).__init__() 
        super(Ui_MainWindow, self).__init__() 

        self.datalog = DataModel()

        self.setupUi(self)
        self.setWindowTitle("UR5 Controller ")
        self.setCentralWidget(self.horizontalLayoutWidget_2)
        self.initFaceTracking()
        if not unconnect_mode:
            self.initRobot()
            self.actuDial()
            self.actuPos()
        self.initConnect()
        self.initTimer()


    def initRobot(self):
        robotModle = URBasic.robotModel.RobotModel()
        self.robot = URobot(host=host, robotModel=robotModle)
        print(self.robot.get_actual_tcp_pose())
        self.robot.run()

    def initFaceTracking(self):
        self.camWidget = QCamLabel(self.horizontalLayoutWidget_2, self.datalog)
        self.camWidget.setObjectName("CamWidget")
        self.verticalLayout_12.addWidget(self.camWidget)
        self.settingWindowCam = SettingWindows(self.camWidget, self.datalog)


    def initConnect(self):
        self.pushButton_toggleTracking.clicked.connect(self.toggleTracking)

        self.horizontalSlider_posX.sliderReleased.connect(self.switchDialToPos)
        self.horizontalSlider_posY.sliderReleased.connect(self.switchDialToPos)
        self.horizontalSlider_posZ.sliderReleased.connect(self.switchDialToPos)
        self.horizontalSlider_posRotX.sliderReleased.connect(self.switchDialToPos)
        self.horizontalSlider_posRotY.sliderReleased.connect(self.switchDialToPos)
        self.horizontalSlider_posRotZ.sliderReleased.connect(self.switchDialToPos)

        self.dial_base.sliderReleased.connect(self.switchPosToDial)
        self.dial_shoulder.sliderReleased.connect(self.switchPosToDial)
        self.dial_elbow.sliderReleased.connect(self.switchPosToDial)
        self.dial_wrist1.sliderReleased.connect(self.switchPosToDial)
        self.dial_wrist2.sliderReleased.connect(self.switchPosToDial)
        self.dial_wrist3.sliderReleased.connect(self.switchPosToDial)

        self.pushButton_posJointMode.clicked.connect(self.sendPosJoinToRobot)
        self.pushButton_reset.clicked.connect(self.onPushButtonResetClicked)
        self.actionOpen_Settings.triggered.connect(self.settingWindowCam.show)

    def initTimer(self):
        self.timerFaceTracking = QTimer() 
        self.timerFaceTracking.setInterval(10)
        self.timerFaceTracking.timeout.connect(self.track)


        self.timerSendJoint = QTimer() 
        self.timerSendJoint.setInterval(1000)
        self.timerSendJoint.timeout.connect(self.sendPosJoinToRobot)
        self.timerActuLabelDial = QTimer() 
        self.timerActuLabelDial.setInterval(100)
        self.timerActuLabelDial.timeout.connect(self.actuLabelDial)
        self.timerActuDial = QTimer() 
        self.timerActuDial.setInterval(100)
        self.timerActuDial.timeout.connect(self.actuDial)

        self.timerSendPos = QTimer() 
        self.timerSendPos.setInterval(1000)
        self.timerSendPos.timeout.connect(self.sendPosToRobot)
        self.timerActuLabelPos = QTimer() 
        self.timerActuLabelPos.setInterval(100)
        self.timerActuLabelPos.timeout.connect(self.actuLabelPos)
        self.timerActuPos = QTimer() 
        self.timerActuPos.setInterval(100)
        self.timerActuPos.timeout.connect(self.actuPos)



        # ACTUALISE LE TEXTE DES SLIDERS
        self.timerActuLabelPos.start()
        self.timerActuLabelDial.start()

        # ENVOI LA POSITION DES SLIDER AU ROBOT
        # self.timerSendJoint.start()  
        #self.timerSendPos.start()

        # ACTUALISE LES SLIDERS
        # self.timerActuDial.start()
        self.timerActuPos.start()

    def actuDial(self):
        pose = self.robot.get_actual_joint_positions()

        self.dial_base.setValue(pose[0]*100)
        self.dial_shoulder.setValue(pose[1]*100)
        self.dial_elbow.setValue(pose[2]*100)
        self.dial_wrist1.setValue(pose[3]*100)
        self.dial_wrist2.setValue(pose[4]*100)
        self.dial_wrist3.setValue(pose[5]*100)

    def actuPos(self):
        pose = self.robot.get_actual_tcp_pose()
        self.horizontalSlider_posX.setValue(pose[0])
        self.horizontalSlider_posY.setValue(pose[1])
        self.horizontalSlider_posZ.setValue(pose[2])
        self.horizontalSlider_posRotX.setValue(pose[3]*100)
        self.horizontalSlider_posRotY.setValue(pose[4]*100)
        self.horizontalSlider_posRotZ.setValue(pose[5]*100)

    def actuLabelPos(self):
        self.label_posX.setText("PosX : "+ str(self.horizontalSlider_posX.value())[0:3])
        self.label_posY.setText("PosY : "+ str(self.horizontalSlider_posY.value())[0:3])
        self.label_posZ.setText("PosZ : "+ str(self.horizontalSlider_posZ.value())[0:3])
        self.label_posRotX.setText("PosRotX : "+ str(self.horizontalSlider_posRotX.value())[0:6])
        self.label_posRotY.setText("PosRotY : "+ str(self.horizontalSlider_posRotY.value())[0:6])
        self.label_posRotZ.setText("PosRotZ : "+ str(self.horizontalSlider_posRotZ.value())[0:6])

    def actuLabelDial(self):
        self.label_base.setText("base: "+ str(degrees(self.dial_base.value()/100))[0:4])
        self.label_shoulder.setText("shoulder: "+ str(degrees(self.dial_shoulder.value()/100))[0:4])
        self.label_elbow.setText("elbow: "+ str(degrees(self.dial_elbow.value()/100))[0:4])
        self.label_wrist1.setText("wrist1: "+ str(degrees(self.dial_wrist1.value()/100))[0:4])
        self.label_wrist2.setText("wrist2: "+ str(degrees(self.dial_wrist2.value()/100))[0:4])
        self.label_wrist3.setText("wrist3: "+ str(degrees(self.dial_wrist3.value()/100))[0:4])

    def sendPosJoinToRobot(self):
        if (self.robot.robotConnector.RobotModel.RuntimeState() 
            and not self.robot.robotConnector.RobotModel.StopRunningFlag()):
            return

        pose = [0, 0, 0, 0, 0, 0]
        pose[0] = self.dial_base.value()/100
        pose[1] = self.dial_shoulder.value()/100
        pose[2] = self.dial_elbow.value()/100
        pose[3] = self.dial_wrist1.value()/100
        pose[4] = self.dial_wrist2.value()/100
        pose[5] = self.dial_wrist3.value()/100
        self.robot.movej(q=pose, a=acc, v=vel, wait=False)

    def sendPosToRobot(self):
        if (self.robot.robotConnector.RobotModel.RuntimeState() 
            and not self.robot.robotConnector.RobotModel.StopRunningFlag()):
            return

        pose = [0, 0, 0, 0, 0, 0]
        pose[0] = self.horizontalSlider_posX.value()
        pose[1] = self.horizontalSlider_posY.value()
        pose[2] = self.horizontalSlider_posZ.value()
        pose[3] = self.horizontalSlider_posRotX.value()/100
        pose[4] = self.horizontalSlider_posRotY.value()/100
        pose[5] = self.horizontalSlider_posRotZ.value()/100
        self.robot.movel(pose=pose, a=acc, v=vel, wait=False)

    def switchPosToDial(self):
        print("Mode: Dial")
        self.timerSendJoint.start()
        self.timerSendPos.stop()
        self.timerActuPos.start()
        self.timerActuDial.stop()

    def switchDialToPos(self):
        print("Mode: Pos")
        self.timerSendJoint.stop()
        self.timerSendPos.start()
        self.timerActuPos.stop()
        self.timerActuDial.start()


    def toggleTracking(self):
        self.camWidget.toggleDetection()
        if self.pushButton_toggleTracking.text() == "Run FaceTracking":
            self.pushButton_toggleTracking.setText("Stop FaceTracking")
            #self.timerSendJoint.stop()
            self.timerFaceTracking.start()
        else :
            self.timerFaceTracking.stop()
            #self.timerSendJoint.start()
            self.pushButton_toggleTracking.setText("Run FaceTracking")

    def track(self):
        if self.datalog.settings["tracking"]:
            mode = self.comboBox_mode.currentText()
            if mode == "combined tracking":
                self.robot.tracking_combine(self.datalog.settings["face_delta"])
            elif mode == "rotary tracking": 
                self.robot.tracking_rotation(self.datalog.settings["face_delta"])
            elif mode == "linear tracking": 
                self.robot.tracking_translation(self.datalog.settings["face_delta"])

    def onPushButtonResetClicked(self):
        self.robot.close()
        robotModle = URBasic.robotModel.RobotModel()
        self.robot = URobot(host=host, robotModel=robotModle)
        print(self.robot.get_actual_tcp_pose())
        self.robot.run()
        self.camWidget.face_center = list()
        self.actuDial()
        self.actuPos()

    def closeEvent(self, event):
        event.accept()
        sys.exit()
