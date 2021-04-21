# Form implementation generated from reading ui file 'NewDistributorContact.ui'
#
# Created by: PyQt6 UI code generator 6.0.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_NewDistributorContact(object):
    def setupUi(self, NewDistributorContact):
        NewDistributorContact.setObjectName("NewDistributorContact")
        NewDistributorContact.resize(953, 628)
        NewDistributorContact.setMinimumSize(QtCore.QSize(700, 25))
        NewDistributorContact.setMaximumSize(QtCore.QSize(953, 16777215))
        NewDistributorContact.setStyleSheet("background-color:#D0DBE8;")
        self.centralwidget = QtWidgets.QWidget(NewDistributorContact)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setStyleSheet("QLineEdit{background-color:white;}\n"
"QPushButton{border:1px solid white; border-radius:10px;color:#F27E14;}\n"
"QPushButton::hover{border: solid black; background-color:white;}\n"
"QLabel{color: #8FA0C9;}\n"
"QComboBox{background-color:white;}\n"
"QScrollBar{background: black;}")
        self.scrollArea.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 931, 606))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.DisContact = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.DisContact.setFont(font)
        self.DisContact.setStyleSheet("color:#6A7AA6")
        self.DisContact.setAlignment(QtCore.Qt.Alignment.AlignLeading|QtCore.Qt.Alignment.AlignLeft|QtCore.Qt.Alignment.AlignVCenter)
        self.DisContact.setObjectName("DisContact")
        self.horizontalLayout_2.addWidget(self.DisContact)
        self.label_title = QtWidgets.QLabel(self.frame)
        self.label_title.setMinimumSize(QtCore.QSize(440, 135))
        self.label_title.setMaximumSize(QtCore.QSize(440, 135))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(30)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet("color:#FF800C")
        self.label_title.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.label_title.setWordWrap(True)
        self.label_title.setObjectName("label_title")
        self.horizontalLayout_2.addWidget(self.label_title)
        self.verticalLayout_2.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:#8FA0C9")
        self.label_4.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:red")
        self.label_5.setAlignment(QtCore.Qt.Alignment.AlignRight|QtCore.Qt.Alignment.AlignTrailing|QtCore.Qt.Alignment.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: #8FA0C9")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.frame_4 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_4.setStyleSheet("QLineEdit{background-color:white;}\n"
"QComboBox{background-color:white;}\n"
"QComboBox QAbstractItemView{background-color:#F17300; color:white;}\n"
"QLabel{color:white;background-color:#F17300; border: solid white; border-radius: 0;}\n"
"QDoubleSpinBox{background-color:white;}\n"
"QPlainTextEdit{background-color:white;}\n"
"")
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_2.setHorizontalSpacing(12)
        self.gridLayout_2.setVerticalSpacing(32)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_7 = QtWidgets.QLabel(self.frame_4)
        self.label_7.setMinimumSize(QtCore.QSize(220, 25))
        self.label_7.setMaximumSize(QtCore.QSize(220, 25))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 3, 0, 1, 1)
        self.comboBox_manu = QtWidgets.QComboBox(self.frame_4)
        self.comboBox_manu.setMinimumSize(QtCore.QSize(250, 25))
        self.comboBox_manu.setMaximumSize(QtCore.QSize(250, 25))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(9)
        self.comboBox_manu.setFont(font)
        self.comboBox_manu.setObjectName("comboBox_manu")
        self.gridLayout_2.addWidget(self.comboBox_manu, 3, 2, 1, 1)
        self.lineEdit_email = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_email.setMinimumSize(QtCore.QSize(400, 25))
        self.lineEdit_email.setMaximumSize(QtCore.QSize(400, 25))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(9)
        self.lineEdit_email.setFont(font)
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.gridLayout_2.addWidget(self.lineEdit_email, 2, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame_4)
        self.label_2.setMinimumSize(QtCore.QSize(220, 25))
        self.label_2.setMaximumSize(QtCore.QSize(220, 25))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)
        self.label_DisCN = QtWidgets.QLabel(self.frame_4)
        self.label_DisCN.setMinimumSize(QtCore.QSize(220, 25))
        self.label_DisCN.setMaximumSize(QtCore.QSize(250, 25))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(10)
        self.label_DisCN.setFont(font)
        self.label_DisCN.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.label_DisCN.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.label_DisCN.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.label_DisCN.setObjectName("label_DisCN")
        self.gridLayout_2.addWidget(self.label_DisCN, 1, 0, 1, 1)
        self.lineEdit_DisCN = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_DisCN.setMinimumSize(QtCore.QSize(220, 25))
        self.lineEdit_DisCN.setMaximumSize(QtCore.QSize(220, 25))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(7)
        self.lineEdit_DisCN.setFont(font)
        self.lineEdit_DisCN.setMaxLength(15)
        self.lineEdit_DisCN.setObjectName("lineEdit_DisCN")
        self.gridLayout_2.addWidget(self.lineEdit_DisCN, 1, 2, 1, 1)
        self.label_DisName = QtWidgets.QLabel(self.frame_4)
        self.label_DisName.setMinimumSize(QtCore.QSize(220, 25))
        self.label_DisName.setMaximumSize(QtCore.QSize(220, 25))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(10)
        self.label_DisName.setFont(font)
        self.label_DisName.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.label_DisName.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.label_DisName.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.label_DisName.setObjectName("label_DisName")
        self.gridLayout_2.addWidget(self.label_DisName, 0, 0, 1, 1)
        self.lineEdit_DisName = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_DisName.setMinimumSize(QtCore.QSize(250, 25))
        self.lineEdit_DisName.setMaximumSize(QtCore.QSize(250, 25))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(9)
        self.lineEdit_DisName.setFont(font)
        self.lineEdit_DisName.setMaxLength(50)
        self.lineEdit_DisName.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.lineEdit_DisName.setObjectName("lineEdit_DisName")
        self.gridLayout_2.addWidget(self.lineEdit_DisName, 0, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.frame_4)
        self.label.setMinimumSize(QtCore.QSize(10, 20))
        self.label.setMaximumSize(QtCore.QSize(10, 20))
        self.label.setStyleSheet("background: none; color:red; font-weight: bold; \n"
"    font: 75 18pt \"Arial\";")
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame_4)
        self.label_3.setMinimumSize(QtCore.QSize(10, 20))
        self.label_3.setMaximumSize(QtCore.QSize(10, 20))
        self.label_3.setStyleSheet("background: none; color:red; font-weight: bold; \n"
"    font: 75 18pt \"Arial\";")
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.frame_4)
        self.label_8.setMinimumSize(QtCore.QSize(10, 20))
        self.label_8.setMaximumSize(QtCore.QSize(10, 20))
        self.label_8.setStyleSheet("background: none; color:red; font-weight: bold; \n"
"    font: 75 18pt \"Arial\";")
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 2, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.frame_4)
        self.label_9.setMinimumSize(QtCore.QSize(10, 20))
        self.label_9.setMaximumSize(QtCore.QSize(10, 20))
        self.label_9.setStyleSheet("background: none; color:red; font-weight: bold; \n"
"    font: 75 18pt \"Arial\";")
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 3, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_5.setStyleSheet("QPushButton{color:#F27E14; border:2px solid #F17300; border-radius: 10px;padding:2px;background-color:white;}\n"
"QPushButton::hover{border:2px solid white; background-color:#F27E14; color:white;}")
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.save_Button_DC = QtWidgets.QPushButton(self.frame_5)
        self.save_Button_DC.setMinimumSize(QtCore.QSize(125, 30))
        self.save_Button_DC.setMaximumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.save_Button_DC.setFont(font)
        self.save_Button_DC.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.save_Button_DC.setObjectName("save_Button_DC")
        self.horizontalLayout_4.addWidget(self.save_Button_DC)
        self.delete_Button_DC = QtWidgets.QPushButton(self.frame_5)
        self.delete_Button_DC.setMinimumSize(QtCore.QSize(125, 30))
        self.delete_Button_DC.setMaximumSize(QtCore.QSize(125, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.delete_Button_DC.setFont(font)
        self.delete_Button_DC.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.delete_Button_DC.setObjectName("delete_Button_DC")
        self.horizontalLayout_4.addWidget(self.delete_Button_DC)
        self.verticalLayout_2.addWidget(self.frame_5)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        NewDistributorContact.setCentralWidget(self.centralwidget)

        self.retranslateUi(NewDistributorContact)
        QtCore.QMetaObject.connectSlotsByName(NewDistributorContact)

    def retranslateUi(self, NewDistributorContact):
        _translate = QtCore.QCoreApplication.translate
        NewDistributorContact.setWindowTitle(_translate("NewDistributorContact", "New Distributor Contact"))
        self.DisContact.setText(_translate("NewDistributorContact", "New <strong> Distributor </strong> Contact"))
        self.label_title.setText(_translate("NewDistributorContact", "<strong>HallyWell</strong> \n"
"Linen Company"))
        self.label_4.setText(_translate("NewDistributorContact", "Please fill out all required and applicable information."))
        self.label_5.setText(_translate("NewDistributorContact", "*"))
        self.label_6.setText(_translate("NewDistributorContact", "- required fields"))
        self.label_7.setText(_translate("NewDistributorContact", "Distributor Name"))
        self.lineEdit_email.setPlaceholderText(_translate("NewDistributorContact", "Enter valid email address"))
        self.label_2.setText(_translate("NewDistributorContact", "Email"))
        self.label_DisCN.setText(_translate("NewDistributorContact", "Contact Number"))
        self.lineEdit_DisCN.setPlaceholderText(_translate("NewDistributorContact", "Enter Contact Number (no spaces)"))
        self.label_DisName.setText(_translate("NewDistributorContact", "Name"))
        self.lineEdit_DisName.setPlaceholderText(_translate("NewDistributorContact", "First and Last Name"))
        self.label.setText(_translate("NewDistributorContact", "*"))
        self.label_3.setText(_translate("NewDistributorContact", "*"))
        self.label_8.setText(_translate("NewDistributorContact", "*"))
        self.label_9.setText(_translate("NewDistributorContact", "*"))
        self.save_Button_DC.setText(_translate("NewDistributorContact", "Submit Form"))
        self.delete_Button_DC.setText(_translate("NewDistributorContact", "Clear Form"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NewDistributorContact = QtWidgets.QMainWindow()
    ui = Ui_NewDistributorContact()
    ui.setupUi(NewDistributorContact)
    NewDistributorContact.show()
    sys.exit(app.exec())
