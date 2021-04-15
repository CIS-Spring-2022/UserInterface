# Form implementation generated from reading ui file 'ProductDetailForm.ui'
#
# Created by: PyQt6 UI code generator 6.0.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ProductDetails(object):
    def setupUi(self, ProductDetails):
        ProductDetails.setObjectName("ProductDetails")
        ProductDetails.resize(951, 714)
        ProductDetails.setStyleSheet("background-color:#D0DBE8;")
        self.centralwidget = QtWidgets.QWidget(ProductDetails)
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
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 929, 692))
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
        font.setBold(True)
        font.setWeight(75)
        self.Form_Name_2.setFont(font)
        self.Form_Name_2.setStyleSheet("color:#8FA0C9")
        self.Form_Name_2.setAlignment(QtCore.Qt.Alignment.AlignLeading|QtCore.Qt.Alignment.AlignLeft|QtCore.Qt.Alignment.AlignVCenter)
        self.Form_Name_2.setObjectName("Form_Name_2")
        self.horizontalLayout_2.addWidget(self.Form_Name_2)
        self.Hallywell_Linen_Company_2 = QtWidgets.QLabel(self.frame)
        self.Hallywell_Linen_Company_2.setMaximumSize(QtCore.QSize(437, 133))
        self.Hallywell_Linen_Company_2.setText("")
        self.Hallywell_Linen_Company_2.setPixmap(QtGui.QPixmap("Hallywell_Linen_Company.png"))
        self.Hallywell_Linen_Company_2.setScaledContents(True)
        self.Hallywell_Linen_Company_2.setObjectName("Hallywell_Linen_Company_2")
        self.horizontalLayout_2.addWidget(self.Hallywell_Linen_Company_2)
        self.verticalLayout_2.addWidget(self.frame)
        self.frame_3 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_prodsearch = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_prodsearch.setMinimumSize(QtCore.QSize(250, 0))
        self.lineEdit_prodsearch.setMaximumSize(QtCore.QSize(275, 16777215))
        self.lineEdit_prodsearch.setMaxLength(250)
        self.lineEdit_prodsearch.setObjectName("lineEdit_prodsearch")
        self.gridLayout.addWidget(self.lineEdit_prodsearch, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.comboBox_selectProd = QtWidgets.QComboBox(self.frame_3)
        self.comboBox_selectProd.setMinimumSize(QtCore.QSize(250, 0))
        self.comboBox_selectProd.setMaximumSize(QtCore.QSize(275, 16777215))
        self.comboBox_selectProd.setObjectName("comboBox_selectProd")
        self.gridLayout.addWidget(self.comboBox_selectProd, 1, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.frame_3)
        self.pushButton.setMinimumSize(QtCore.QSize(125, 30))
        self.pushButton.setMaximumSize(QtCore.QSize(116, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame_3)
        self.label_4.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_4.setStyleSheet("QLineEdit{background-color:white;}\n"
"QComboBox{background-color:white;}\n"
"QLabel{color:#8FA0C9;}\n"
"QDoubleSpinBox{background-color:white;}\n"
"QPlainTextEdit{background-color:white;}\n"
"QLabel{border-radius:5px;border: 1px solid white;}")
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_2.setHorizontalSpacing(12)
        self.gridLayout_2.setVerticalSpacing(32)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.comboBox_History = QtWidgets.QComboBox(self.frame_4)
        self.comboBox_History.setMaximumSize(QtCore.QSize(150, 16777215))
        self.comboBox_History.setObjectName("comboBox_History")
        self.gridLayout_2.addWidget(self.comboBox_History, 2, 1, 1, 1)
        self.comboBox_Manu = QtWidgets.QComboBox(self.frame_4)
        self.comboBox_Manu.setMaximumSize(QtCore.QSize(150, 20))
        self.comboBox_Manu.setObjectName("comboBox_Manu")
        self.gridLayout_2.addWidget(self.comboBox_Manu, 1, 1, 1, 1)
        self.comboBox_Material = QtWidgets.QComboBox(self.frame_4)
        self.comboBox_Material.setMaximumSize(QtCore.QSize(150, 16777215))
        self.comboBox_Material.setObjectName("comboBox_Material")
        self.gridLayout_2.addWidget(self.comboBox_Material, 4, 3, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.frame_4)
        self.label_11.setMinimumSize(QtCore.QSize(175, 0))
        self.label_11.setMaximumSize(QtCore.QSize(175, 16777215))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 4, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.frame_4)
        self.label_6.setMinimumSize(QtCore.QSize(220, 0))
        self.label_6.setMaximumSize(QtCore.QSize(250, 35))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.label_6.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.label_6.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 1, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.frame_4)
        self.label_13.setMinimumSize(QtCore.QSize(220, 0))
        self.label_13.setMaximumSize(QtCore.QSize(180, 16777215))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 4, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.frame_4)
        self.label_12.setMinimumSize(QtCore.QSize(175, 0))
        self.label_12.setMaximumSize(QtCore.QSize(175, 16777215))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 5, 2, 1, 1)
        self.comboBox_Thread = QtWidgets.QComboBox(self.frame_4)
        self.comboBox_Thread.setMaximumSize(QtCore.QSize(150, 16777215))
        self.comboBox_Thread.setObjectName("comboBox_Thread")
        self.gridLayout_2.addWidget(self.comboBox_Thread, 5, 3, 1, 1)
        self.comboBox_Size = QtWidgets.QComboBox(self.frame_4)
        self.comboBox_Size.setMaximumSize(QtCore.QSize(150, 16777215))
        self.comboBox_Size.setObjectName("comboBox_Size")
        self.gridLayout_2.addWidget(self.comboBox_Size, 4, 1, 1, 1)
        self.comboBox_Type = QtWidgets.QComboBox(self.frame_4)
        self.comboBox_Type.setMaximumSize(QtCore.QSize(150, 16777215))
        self.comboBox_Type.setObjectName("comboBox_Type")
        self.gridLayout_2.addWidget(self.comboBox_Type, 3, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.frame_4)
        self.label_9.setMinimumSize(QtCore.QSize(220, 0))
        self.label_9.setMaximumSize(QtCore.QSize(180, 16777215))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.label_9.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.label_9.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 2, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame_4)
        self.label_5.setMinimumSize(QtCore.QSize(220, 0))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.label_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.label_5.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)
        self.lineEdit_ProductName = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_ProductName.setMinimumSize(QtCore.QSize(250, 0))
        self.lineEdit_ProductName.setMaximumSize(QtCore.QSize(260, 16777215))
        self.lineEdit_ProductName.setMaxLength(250)
        self.lineEdit_ProductName.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.lineEdit_ProductName.setObjectName("lineEdit_ProductName")
        self.gridLayout_2.addWidget(self.lineEdit_ProductName, 0, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.frame_4)
        self.label_10.setMinimumSize(QtCore.QSize(220, 0))
        self.label_10.setMaximumSize(QtCore.QSize(180, 16777215))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.label_10.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.label_10.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 3, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.frame_4)
        self.label_14.setMinimumSize(QtCore.QSize(220, 0))
        self.label_14.setMaximumSize(QtCore.QSize(180, 16777215))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout_2.addWidget(self.label_14, 5, 0, 1, 1)
        self.Product_Price = QtWidgets.QDoubleSpinBox(self.frame_4)
        self.Product_Price.setMaximumSize(QtCore.QSize(70, 16777215))
        self.Product_Price.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.Product_Price.setMaximum(99999999.99)
        self.Product_Price.setObjectName("Product_Price")
        self.gridLayout_2.addWidget(self.Product_Price, 3, 3, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.frame_4)
        self.label_8.setMinimumSize(QtCore.QSize(175, 0))
        self.label_8.setMaximumSize(QtCore.QSize(175, 16777215))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 3, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.label_7.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.label_7.setAlignment(QtCore.Qt.Alignment.AlignHCenter|QtCore.Qt.Alignment.AlignTop)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 0, 2, 1, 1)
        self.characters_remaining = QtWidgets.QLabel(self.frame_4)
        self.characters_remaining.setMaximumSize(QtCore.QSize(16777215, 20))
        self.characters_remaining.setStyleSheet("border: none;")
        self.characters_remaining.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.characters_remaining.setObjectName("characters_remaining")
        self.gridLayout_2.addWidget(self.characters_remaining, 2, 3, 1, 1)
        self.description_box = QtWidgets.QPlainTextEdit(self.frame_4)
        self.description_box.setMinimumSize(QtCore.QSize(200, 0))
        self.description_box.setMaximumSize(QtCore.QSize(200, 200))
        self.description_box.setObjectName("description_box")
        self.gridLayout_2.addWidget(self.description_box, 0, 3, 2, 1)
        self.comboBox_Color = QtWidgets.QComboBox(self.frame_4)
        self.comboBox_Color.setMaximumSize(QtCore.QSize(150, 16777215))
        self.comboBox_Color.setObjectName("comboBox_Color")
        self.gridLayout_2.addWidget(self.comboBox_Color, 5, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
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
        self.delete_Button.setMinimumSize(QtCore.QSize(125, 30))
        self.delete_Button.setMaximumSize(QtCore.QSize(125, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.delete_Button.setFont(font)
        self.delete_Button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.delete_Button.setObjectName("delete_Button")
        self.horizontalLayout_4.addWidget(self.delete_Button)
        self.verticalLayout_2.addWidget(self.frame_5)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        ProductDetails.setCentralWidget(self.centralwidget)

        self.retranslateUi(ProductDetails)
        QtCore.QMetaObject.connectSlotsByName(ProductDetails)

    def retranslateUi(self, ProductDetails):
        _translate = QtCore.QCoreApplication.translate
        ProductDetails.setWindowTitle(_translate("ProductDetails", "Product Detail Form"))
        self.Form_Name_2.setText(_translate("ProductDetails", "Product Details"))
        self.label_3.setText(_translate("ProductDetails", "Search Product Name"))
        self.pushButton.setText(_translate("ProductDetails", "Select Product"))
        self.label_4.setText(_translate("ProductDetails", "Select Product To Edit"))
        self.label_11.setText(_translate("ProductDetails", "Product Material"))
        self.label_6.setText(_translate("ProductDetails", "Product Manufacturer"))
        self.label_13.setText(_translate("ProductDetails", "Product Size"))
        self.label_12.setText(_translate("ProductDetails", "Product Thread"))
        self.label_9.setText(_translate("ProductDetails", "Product History"))
        self.label_5.setText(_translate("ProductDetails", "Product Name"))
        self.lineEdit_ProductName.setPlaceholderText(_translate("ProductDetails", "Enter Product Name"))
        self.label_10.setText(_translate("ProductDetails", "Product Type"))
        self.label_14.setText(_translate("ProductDetails", "Product Color"))
        self.Product_Price.setPrefix(_translate("ProductDetails", "$"))
        self.label_8.setText(_translate("ProductDetails", "Product Price"))
        self.label_7.setText(_translate("ProductDetails", "Product Description"))
        self.characters_remaining.setText(_translate("ProductDetails", "250 characters remaining"))
        self.description_box.setPlaceholderText(_translate("ProductDetails", "Enter Product Description"))
        self.save_Button.setText(_translate("ProductDetails", "Save Changes"))
        self.delete_Button.setText(_translate("ProductDetails", "Delete Product"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ProductDetails = QtWidgets.QMainWindow()
    ui = Ui_ProductDetails()
    ui.setupUi(ProductDetails)
    ProductDetails.show()
    sys.exit(app.exec())
