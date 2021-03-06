# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface/ui_RecoFaceSettings.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RecoFaceSettings(object):
    def setupUi(self, RecoFaceSettings):

        self.horizontalLayoutWidget = QtWidgets.QWidget(RecoFaceSettings)
        RecoFaceSettings.setCentralWidget(self.horizontalLayoutWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.checkBox_detectionState = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkBox_detectionState.setObjectName("checkBox_detectionState")
        self.horizontalLayout_3.addWidget(self.checkBox_detectionState)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.checkBox_ScaleFactor = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkBox_ScaleFactor.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkBox_ScaleFactor.setAcceptDrops(False)
        self.checkBox_ScaleFactor.setCheckable(True)
        self.checkBox_ScaleFactor.setChecked(True)
        self.checkBox_ScaleFactor.setAutoRepeat(False)
        self.checkBox_ScaleFactor.setAutoRepeatDelay(10)
        self.checkBox_ScaleFactor.setAutoRepeatInterval(10)
        self.checkBox_ScaleFactor.setObjectName("checkBox_ScaleFactor")
        self.verticalLayout_2.addWidget(self.checkBox_ScaleFactor)
        self.horizontalSlider_ScaleFactor = QtWidgets.QSlider(self.horizontalLayoutWidget)
        self.horizontalSlider_ScaleFactor.setEnabled(True)
        self.horizontalSlider_ScaleFactor.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.horizontalSlider_ScaleFactor.setMouseTracking(True)
        self.horizontalSlider_ScaleFactor.setMinimum(101)
        self.horizontalSlider_ScaleFactor.setMaximum(200)
        self.horizontalSlider_ScaleFactor.setSingleStep(1)
        self.horizontalSlider_ScaleFactor.setPageStep(1)
        self.horizontalSlider_ScaleFactor.setProperty("value", 150)
        self.horizontalSlider_ScaleFactor.setSliderPosition(150)
        self.horizontalSlider_ScaleFactor.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_ScaleFactor.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.horizontalSlider_ScaleFactor.setObjectName("horizontalSlider_ScaleFactor")
        self.verticalLayout_2.addWidget(self.horizontalSlider_ScaleFactor)
        self.line_2 = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_2.addWidget(self.line_2)
        self.checkBox_MinNeighbors = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkBox_MinNeighbors.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkBox_MinNeighbors.setChecked(True)
        self.checkBox_MinNeighbors.setObjectName("checkBox_MinNeighbors")
        self.verticalLayout_2.addWidget(self.checkBox_MinNeighbors)
        self.horizontalSlider_MinNeighbors = QtWidgets.QSlider(self.horizontalLayoutWidget)
        self.horizontalSlider_MinNeighbors.setEnabled(True)
        self.horizontalSlider_MinNeighbors.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.horizontalSlider_MinNeighbors.setMinimum(2)
        self.horizontalSlider_MinNeighbors.setMaximum(8)
        self.horizontalSlider_MinNeighbors.setProperty("value", 5)
        self.horizontalSlider_MinNeighbors.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_MinNeighbors.setObjectName("horizontalSlider_MinNeighbors")
        self.verticalLayout_2.addWidget(self.horizontalSlider_MinNeighbors)
        self.line_3 = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_2.addWidget(self.line_3)
        self.checkBox_MinSize = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkBox_MinSize.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkBox_MinSize.setChecked(True)
        self.checkBox_MinSize.setObjectName("checkBox_MinSize")
        self.verticalLayout_2.addWidget(self.checkBox_MinSize)
        self.horizontalSlider_MinSize = QtWidgets.QSlider(self.horizontalLayoutWidget)
        self.horizontalSlider_MinSize.setEnabled(True)
        self.horizontalSlider_MinSize.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.horizontalSlider_MinSize.setMinimum(10)
        self.horizontalSlider_MinSize.setMaximum(200)
        self.horizontalSlider_MinSize.setProperty("value", 30)
        self.horizontalSlider_MinSize.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_MinSize.setObjectName("horizontalSlider_MinSize")
        self.verticalLayout_2.addWidget(self.horizontalSlider_MinSize)
        self.line_4 = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_2.addWidget(self.line_4)
        self.checkBox_MaxSizeMaxSize = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkBox_MaxSizeMaxSize.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkBox_MaxSizeMaxSize.setChecked(False)
        self.checkBox_MaxSizeMaxSize.setObjectName("checkBox_MaxSizeMaxSize")
        self.verticalLayout_2.addWidget(self.checkBox_MaxSizeMaxSize)
        self.horizontalSlider_MaxSize = QtWidgets.QSlider(self.horizontalLayoutWidget)
        self.horizontalSlider_MaxSize.setEnabled(False)
        self.horizontalSlider_MaxSize.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.horizontalSlider_MaxSize.setMinimum(20)
        self.horizontalSlider_MaxSize.setMaximum(400)
        self.horizontalSlider_MaxSize.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_MaxSize.setObjectName("horizontalSlider_MaxSize")
        self.verticalLayout_2.addWidget(self.horizontalSlider_MaxSize)
        self.line_5 = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.verticalLayout_2.addWidget(self.line_5)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.line = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_Ajouter = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_Ajouter.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_Ajouter.setObjectName("pushButton_Ajouter")
        self.horizontalLayout_2.addWidget(self.pushButton_Ajouter)
        self.pushButton_Supprimer = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_Supprimer.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_Supprimer.setObjectName("pushButton_Supprimer")
        self.horizontalLayout_2.addWidget(self.pushButton_Supprimer)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.listWidget = QtWidgets.QListWidget(self.horizontalLayoutWidget)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(RecoFaceSettings)
        self.checkBox_ScaleFactor.toggled['bool'].connect(self.horizontalSlider_ScaleFactor.setEnabled)
        self.checkBox_MinNeighbors.toggled['bool'].connect(self.horizontalSlider_MinNeighbors.setEnabled)
        self.checkBox_MinSize.toggled['bool'].connect(self.horizontalSlider_MinSize.setEnabled)
        self.checkBox_MaxSizeMaxSize.toggled['bool'].connect(self.horizontalSlider_MaxSize.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(RecoFaceSettings)
        RecoFaceSettings.setTabOrder(self.checkBox_ScaleFactor, self.checkBox_MinNeighbors)
        RecoFaceSettings.setTabOrder(self.checkBox_MinNeighbors, self.horizontalSlider_MinNeighbors)
        RecoFaceSettings.setTabOrder(self.horizontalSlider_MinNeighbors, self.checkBox_MinSize)
        RecoFaceSettings.setTabOrder(self.checkBox_MinSize, self.horizontalSlider_MinSize)
        RecoFaceSettings.setTabOrder(self.horizontalSlider_MinSize, self.checkBox_MaxSizeMaxSize)
        RecoFaceSettings.setTabOrder(self.checkBox_MaxSizeMaxSize, self.horizontalSlider_MaxSize)
        RecoFaceSettings.setTabOrder(self.horizontalSlider_MaxSize, self.pushButton_Ajouter)
        RecoFaceSettings.setTabOrder(self.pushButton_Ajouter, self.pushButton_Supprimer)
        RecoFaceSettings.setTabOrder(self.pushButton_Supprimer, self.listWidget)

    def retranslateUi(self, RecoFaceSettings):
        _translate = QtCore.QCoreApplication.translate
        RecoFaceSettings.setWindowTitle(_translate("RecoFaceSettings", "Frame"))
        self.checkBox_detectionState.setText(_translate("RecoFaceSettings", "Activ??"))
        self.checkBox_ScaleFactor.setText(_translate("RecoFaceSettings", "ScaleFactor"))
        self.checkBox_MinNeighbors.setText(_translate("RecoFaceSettings", "MinNeighbors"))
        self.checkBox_MinSize.setText(_translate("RecoFaceSettings", "MinSize"))
        self.checkBox_MaxSizeMaxSize.setText(_translate("RecoFaceSettings", "MaxSize"))
        self.pushButton_Ajouter.setText(_translate("RecoFaceSettings", "Ajouter"))
        self.pushButton_Supprimer.setText(_translate("RecoFaceSettings", "Supprimer"))


if __name__ == "__main__":
    print("aa")
