# Form implementation generated from reading ui file 'NewDistributorForm.ui'
#
# Created by: PyQt6 UI code generator 6.0.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_NewDistributorForm(object):
    def setupUi(self, NewDistributorForm):
        NewDistributorForm.setObjectName("NewDistributorForm")
        NewDistributorForm.resize(1181, 690)
        NewDistributorForm.setStyleSheet("background-color:#D0DBE8;")
        self.centralwidget = QtWidgets.QWidget(NewDistributorForm)
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
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1159, 668))
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
        self.Form_Name_2 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.Form_Name_2.setFont(font)
        self.Form_Name_2.setStyleSheet("color:#6A7AA6")
        self.Form_Name_2.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.Form_Name_2.setObjectName("Form_Name_2")
        self.horizontalLayout_2.addWidget(self.Form_Name_2)
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
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:#8FA0C9")
        self.label_2.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:red")
        self.label.setAlignment(QtCore.Qt.Alignment.AlignRight|QtCore.Qt.Alignment.AlignTrailing|QtCore.Qt.Alignment.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: #8FA0C9")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.frame_4 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.frame_4.setFont(font)
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
        self.lineEdit_DisName.setMinimumSize(QtCore.QSize(350, 25))
        self.lineEdit_DisName.setMaximumSize(QtCore.QSize(350, 25))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(9)
        self.lineEdit_DisName.setFont(font)
        self.lineEdit_DisName.setInputMask("")
        self.lineEdit_DisName.setMaxLength(50)
        self.lineEdit_DisName.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.lineEdit_DisName.setObjectName("lineEdit_DisName")
        self.gridLayout_2.addWidget(self.lineEdit_DisName, 0, 2, 1, 1)
        self.label_DisAddress = QtWidgets.QLabel(self.frame_4)
        self.label_DisAddress.setMinimumSize(QtCore.QSize(220, 25))
        self.label_DisAddress.setMaximumSize(QtCore.QSize(220, 25))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(10)
        self.label_DisAddress.setFont(font)
        self.label_DisAddress.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.label_DisAddress.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.label_DisAddress.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.label_DisAddress.setObjectName("label_DisAddress")
        self.gridLayout_2.addWidget(self.label_DisAddress, 1, 0, 1, 1)
        self.label_DisDesc = QtWidgets.QLabel(self.frame_4)
        self.label_DisDesc.setMinimumSize(QtCore.QSize(220, 25))
        self.label_DisDesc.setMaximumSize(QtCore.QSize(220, 25))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(10)
        self.label_DisDesc.setFont(font)
        self.label_DisDesc.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.label_DisDesc.setObjectName("label_DisDesc")
        self.gridLayout_2.addWidget(self.label_DisDesc, 6, 0, 1, 1)
        self.label_DisPC = QtWidgets.QLabel(self.frame_4)
        self.label_DisPC.setMinimumSize(QtCore.QSize(220, 25))
        self.label_DisPC.setMaximumSize(QtCore.QSize(220, 25))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(10)
        self.label_DisPC.setFont(font)
        self.label_DisPC.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.label_DisPC.setObjectName("label_DisPC")
        self.gridLayout_2.addWidget(self.label_DisPC, 5, 0, 1, 1)
        self.label_DisCity = QtWidgets.QLabel(self.frame_4)
        self.label_DisCity.setMinimumSize(QtCore.QSize(220, 25))
        self.label_DisCity.setMaximumSize(QtCore.QSize(220, 25))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(10)
        self.label_DisCity.setFont(font)
        self.label_DisCity.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.label_DisCity.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.label_DisCity.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.label_DisCity.setObjectName("label_DisCity")
        self.gridLayout_2.addWidget(self.label_DisCity, 2, 0, 1, 1)
        self.lineEdit_postalcode = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_postalcode.setMinimumSize(QtCore.QSize(55, 25))
        self.lineEdit_postalcode.setMaximumSize(QtCore.QSize(55, 25))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(9)
        self.lineEdit_postalcode.setFont(font)
        self.lineEdit_postalcode.setMaxLength(6)
        self.lineEdit_postalcode.setObjectName("lineEdit_postalcode")
        self.gridLayout_2.addWidget(self.lineEdit_postalcode, 5, 2, 1, 1)
        self.label_DisState = QtWidgets.QLabel(self.frame_4)
        self.label_DisState.setMinimumSize(QtCore.QSize(220, 25))
        self.label_DisState.setMaximumSize(QtCore.QSize(220, 25))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(10)
        self.label_DisState.setFont(font)
        self.label_DisState.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.label_DisState.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.label_DisState.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.label_DisState.setObjectName("label_DisState")
        self.gridLayout_2.addWidget(self.label_DisState, 4, 0, 1, 1)
        self.lineEdit_DisCity = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_DisCity.setMinimumSize(QtCore.QSize(230, 25))
        self.lineEdit_DisCity.setMaximumSize(QtCore.QSize(230, 25))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(9)
        self.lineEdit_DisCity.setFont(font)
        self.lineEdit_DisCity.setMaxLength(30)
        self.lineEdit_DisCity.setObjectName("lineEdit_DisCity")
        self.gridLayout_2.addWidget(self.lineEdit_DisCity, 2, 2, 1, 1)
        self.lineEdit_DisAddress = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_DisAddress.setMinimumSize(QtCore.QSize(700, 25))
        self.lineEdit_DisAddress.setMaximumSize(QtCore.QSize(700, 24))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(9)
        self.lineEdit_DisAddress.setFont(font)
        self.lineEdit_DisAddress.setMaxLength(250)
        self.lineEdit_DisAddress.setObjectName("lineEdit_DisAddress")
        self.gridLayout_2.addWidget(self.lineEdit_DisAddress, 1, 2, 1, 1)
        self.comboBox_state = QtWidgets.QComboBox(self.frame_4)
        self.comboBox_state.setMinimumSize(QtCore.QSize(230, 25))
        self.comboBox_state.setMaximumSize(QtCore.QSize(240, 25))
        self.comboBox_state.setObjectName("comboBox_state")
        self.gridLayout_2.addWidget(self.comboBox_state, 4, 2, 1, 1)
        self.comboBox_disstat = QtWidgets.QComboBox(self.frame_4)
        self.comboBox_disstat.setMinimumSize(QtCore.QSize(190, 25))
        self.comboBox_disstat.setMaximumSize(QtCore.QSize(190, 25))
        self.comboBox_disstat.setObjectName("comboBox_disstat")
        self.gridLayout_2.addWidget(self.comboBox_disstat, 6, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame_4)
        self.label_4.setMinimumSize(QtCore.QSize(10, 20))
        self.label_4.setMaximumSize(QtCore.QSize(10, 20))
        self.label_4.setStyleSheet("background: none; color:red; font-weight: bold; \n"
"    font: 75 18pt \"Arial\";")
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame_4)
        self.label_5.setMinimumSize(QtCore.QSize(10, 20))
        self.label_5.setMaximumSize(QtCore.QSize(10, 20))
        self.label_5.setStyleSheet("background: none; color:red; font-weight: bold; \n"
"    font: 75 18pt \"Arial\";")
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.frame_4)
        self.label_6.setMinimumSize(QtCore.QSize(10, 20))
        self.label_6.setMaximumSize(QtCore.QSize(10, 20))
        self.label_6.setStyleSheet("background: none; color:red; font-weight: bold; \n"
"    font: 75 18pt \"Arial\";")
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 2, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.frame_4)
        self.label_7.setMinimumSize(QtCore.QSize(10, 20))
        self.label_7.setMaximumSize(QtCore.QSize(10, 20))
        self.label_7.setStyleSheet("background: none; color:red; font-weight: bold; \n"
"    font: 75 18pt \"Arial\";")
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 4, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.frame_4)
        self.label_8.setMinimumSize(QtCore.QSize(10, 20))
        self.label_8.setMaximumSize(QtCore.QSize(10, 20))
        self.label_8.setStyleSheet("background: none; color:red; font-weight: bold; \n"
"    font: 75 18pt \"Arial\";")
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 5, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.frame_4)
        self.label_9.setMinimumSize(QtCore.QSize(10, 20))
        self.label_9.setMaximumSize(QtCore.QSize(10, 20))
        self.label_9.setStyleSheet("background: none; color:red; font-weight: bold; \n"
"    font: 75 18pt \"Arial\";")
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 6, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_5.setStyleSheet("QPushButton{color:#F27E14; border:2px solid #F17300; border-radius: 10px;padding:2px;background-color:white;}\n"
"QPushButton::hover{border:2px solid white; background-color:#F27E14; color:white;}")
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.save_Button = QtWidgets.QPushButton(self.frame_5)
        self.save_Button.setMinimumSize(QtCore.QSize(125, 30))
        self.save_Button.setMaximumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.save_Button.setFont(font)
        self.save_Button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.save_Button.setObjectName("save_Button")
        self.horizontalLayout_4.addWidget(self.save_Button)
        self.delete_Button = QtWidgets.QPushButton(self.frame_5)
        self.delete_Button.setMinimumSize(QtCore.QSize(150, 30))
        self.delete_Button.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.delete_Button.setFont(font)
        self.delete_Button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.delete_Button.setObjectName("delete_Button")
        self.horizontalLayout_4.addWidget(self.delete_Button)
        self.verticalLayout_2.addWidget(self.frame_5)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        NewDistributorForm.setCentralWidget(self.centralwidget)

        self.retranslateUi(NewDistributorForm)
        QtCore.QMetaObject.connectSlotsByName(NewDistributorForm)

    def retranslateUi(self, NewDistributorForm):
        _translate = QtCore.QCoreApplication.translate
        NewDistributorForm.setWindowTitle(_translate("NewDistributorForm", "New Distributor Form"))
        self.Form_Name_2.setText(_translate("NewDistributorForm", "<html><head/><body><p><span style=\" font-weight:600;\">New Distributor</span></p></body></html>"))
        self.label_title.setText(_translate("NewDistributorForm", "<strong>HallyWell</strong> \n"
"Linen Company"))
        self.label_2.setText(_translate("NewDistributorForm", "Please fill out all required and applicable information."))
        self.label.setText(_translate("NewDistributorForm", "*"))
        self.label_3.setText(_translate("NewDistributorForm", "- required fields"))
        self.label_DisName.setText(_translate("NewDistributorForm", "Name"))
        self.lineEdit_DisName.setPlaceholderText(_translate("NewDistributorForm", "Enter First & Last Name"))
        self.label_DisAddress.setText(_translate("NewDistributorForm", "Address"))
        self.label_DisDesc.setText(_translate("NewDistributorForm", "Distributor Status"))
        self.label_DisPC.setText(_translate("NewDistributorForm", "Postal Code"))
        self.label_DisCity.setText(_translate("NewDistributorForm", "City"))
        self.lineEdit_postalcode.setInputMask(_translate("NewDistributorForm", "000000;_"))
        self.label_DisState.setText(_translate("NewDistributorForm", "State"))
        self.lineEdit_DisCity.setPlaceholderText(_translate("NewDistributorForm", "Enter City"))
        self.lineEdit_DisAddress.setPlaceholderText(_translate("NewDistributorForm", "Enter Distributor Addess"))
        self.label_4.setText(_translate("NewDistributorForm", "*"))
        self.label_5.setText(_translate("NewDistributorForm", "*"))
        self.label_6.setText(_translate("NewDistributorForm", "*"))
        self.label_7.setText(_translate("NewDistributorForm", "*"))
        self.label_8.setText(_translate("NewDistributorForm", "*"))
        self.label_9.setText(_translate("NewDistributorForm", "*"))
        self.save_Button.setText(_translate("NewDistributorForm", "Submit Form"))
        self.delete_Button.setText(_translate("NewDistributorForm", "Clear Form"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NewDistributorForm = QtWidgets.QMainWindow()
    ui = Ui_NewDistributorForm()
    ui.setupUi(NewDistributorForm)
    NewDistributorForm.show()
    sys.exit(app.exec())
