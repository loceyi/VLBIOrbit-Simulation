# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Parameter_Input.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.NonModal)
        Dialog.setEnabled(True)
        Dialog.resize(1100, 755)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setBaseSize(QtCore.QSize(400, 400))
        Dialog.setStyleSheet("background-color: rgb(240, 240, 240);")
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(False)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(6, 6, 111, 31))
        self.label.setStyleSheet("font: 11pt \"Arial\";")
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(0, 40, 951, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(10, 150, 101, 41))
        self.label_9.setStyleSheet("font: 10pt \"Adobe 黑体 Std R\";")
        self.label_9.setObjectName("label_9")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(10, 80, 101, 31))
        self.label_8.setStyleSheet("font: 10pt \"Adobe 黑体 Std R\";")
        self.label_8.setObjectName("label_8")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(10, 240, 101, 31))
        self.label_10.setStyleSheet("font: 10pt \"Adobe 黑体 Std R\";")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(10, 320, 141, 41))
        self.label_11.setStyleSheet("font: 10pt \"Adobe 黑体 Std R\";")
        self.label_11.setObjectName("label_11")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(460, 80, 191, 31))
        self.label_2.setStyleSheet("font: 10pt \"Adobe 黑体 Std R\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(460, 240, 161, 31))
        self.label_3.setStyleSheet("font: 10pt \"Adobe 黑体 Std R\";")
        self.label_3.setObjectName("label_3")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(460, 160, 151, 31))
        self.label_6.setStyleSheet("font: 10pt \"Adobe 黑体 Std R\";")
        self.label_6.setObjectName("label_6")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(460, 310, 191, 41))
        self.label_4.setStyleSheet("font: 10pt \"Adobe 黑体 Std R\";")
        self.label_4.setObjectName("label_4")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(460, 400, 131, 31))
        self.label_7.setStyleSheet("font: 10pt \"Adobe 黑体 Std R\";")
        self.label_7.setObjectName("label_7")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(460, 480, 171, 31))
        self.label_5.setStyleSheet("font: 10pt \"Adobe 黑体 Std R\";")
        self.label_5.setObjectName("label_5")
        self.Coord_System = QtWidgets.QComboBox(Dialog)
        self.Coord_System.setGeometry(QtCore.QRect(150, 330, 281, 31))
        self.Coord_System.setObjectName("Coord_System")
        self.Coord_System.addItem("")
        self.Coord_System.addItem("")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(810, 630, 101, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(980, 630, 91, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.Start_Time = QtWidgets.QLineEdit(Dialog)
        self.Start_Time.setGeometry(QtCore.QRect(150, 80, 281, 31))
        self.Start_Time.setToolTipDuration(-3)
        self.Start_Time.setObjectName("Start_Time")
        self.Stop_Time = QtWidgets.QLineEdit(Dialog)
        self.Stop_Time.setGeometry(QtCore.QRect(150, 160, 281, 31))
        self.Stop_Time.setToolTipDuration(-1)
        self.Stop_Time.setObjectName("Stop_Time")
        self.Step_Size = QtWidgets.QLineEdit(Dialog)
        self.Step_Size.setGeometry(QtCore.QRect(150, 240, 281, 31))
        self.Step_Size.setObjectName("Step_Size")
        self.Semimajor_Axis = QtWidgets.QLineEdit(Dialog)
        self.Semimajor_Axis.setGeometry(QtCore.QRect(700, 80, 241, 31))
        self.Semimajor_Axis.setObjectName("Semimajor_Axis")
        self.Inclination = QtWidgets.QLineEdit(Dialog)
        self.Inclination.setGeometry(QtCore.QRect(700, 160, 241, 31))
        self.Inclination.setObjectName("Inclination")
        self.Eccentricity = QtWidgets.QLineEdit(Dialog)
        self.Eccentricity.setGeometry(QtCore.QRect(700, 240, 241, 31))
        self.Eccentricity.setObjectName("Eccentricity")
        self.Perigee = QtWidgets.QLineEdit(Dialog)
        self.Perigee.setGeometry(QtCore.QRect(700, 320, 241, 31))
        self.Perigee.setObjectName("Perigee")
        self.RAAN = QtWidgets.QLineEdit(Dialog)
        self.RAAN.setGeometry(QtCore.QRect(700, 400, 241, 31))
        self.RAAN.setObjectName("RAAN")
        self.TA = QtWidgets.QLineEdit(Dialog)
        self.TA.setGeometry(QtCore.QRect(700, 480, 241, 31))
        self.TA.setObjectName("TA")

        self.retranslateUi(Dialog)
        self.pushButton_2.clicked.connect(Dialog.reject)
        self.pushButton.clicked.connect(Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Parameter Input"))
        self.label.setText(_translate("Dialog", "Propagator:HPOP"))
        self.label_9.setText(_translate("Dialog", "Stop Time:"))
        self.label_8.setText(_translate("Dialog", "Start Time:"))
        self.label_10.setText(_translate("Dialog", "Step Size:"))
        self.label_11.setText(_translate("Dialog", "Coord System:"))
        self.label_2.setText(_translate("Dialog", "Semimajor Axis:"))
        self.label_3.setText(_translate("Dialog", "Eccentricity:"))
        self.label_6.setText(_translate("Dialog", "Inclination:"))
        self.label_4.setText(_translate("Dialog", "Perigee:"))
        self.label_7.setText(_translate("Dialog", "RAAN:"))
        self.label_5.setText(_translate("Dialog", "True Anomaly:"))
        self.Coord_System.setItemText(0, _translate("Dialog", "GCRF"))
        self.Coord_System.setItemText(1, _translate("Dialog", "J2000"))
        self.pushButton.setText(_translate("Dialog", "OK"))
        self.pushButton_2.setText(_translate("Dialog", "Cancel"))
        self.Start_Time.setToolTip(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">SEC/MIN/HR/DAY/MONTH/YEAR</span></p></body></html>"))
        self.Start_Time.setText(_translate("Dialog", "00/00/00/00/01/2015"))
        self.Stop_Time.setToolTip(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">SEC/MIN/HR/DAY/MONTH/YEAR</span></p></body></html>"))
        self.Stop_Time.setText(_translate("Dialog", "00/00/00/01/01/2015"))
        self.Step_Size.setToolTip(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">1s</span></p></body></html>"))
        self.Step_Size.setText(_translate("Dialog", "1s"))
        self.Semimajor_Axis.setToolTip(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">i.e.7000 KM</span></p></body></html>"))
        self.Semimajor_Axis.setText(_translate("Dialog", "7000 km"))
        self.Inclination.setToolTip(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">45 deg</span></p></body></html>"))
        self.Inclination.setText(_translate("Dialog", "45 deg"))
        self.Eccentricity.setToolTip(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">0.1</span></p></body></html>"))
        self.Eccentricity.setText(_translate("Dialog", "0.1"))
        self.Perigee.setToolTip(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">12 deg</span></p></body></html>"))
        self.Perigee.setText(_translate("Dialog", "12 deg"))
        self.RAAN.setToolTip(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">12 deg</span></p></body></html>"))
        self.RAAN.setText(_translate("Dialog", "12 deg"))
        self.TA.setToolTip(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">12 deg</span></p></body></html>"))
        self.TA.setText(_translate("Dialog", "12 deg"))

