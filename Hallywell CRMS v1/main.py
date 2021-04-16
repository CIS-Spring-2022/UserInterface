from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import *
# todo: import all form classes here
from loadingscreen import Ui_LoadingScreen
from mainscreen import Ui_MainScreen
from NewProductForm import Ui_NewProductForm
from ProductColorDetail import Ui_ProductColorDetail
from ProductDetailForm import Ui_ProductDetails
from ProductRatingDetail import Ui_ProductRatingDetail
from ProductStatusDetail import Ui_ProductStatusDetail
from ProductTypeDetail import Ui_ProductTypeDetail

from DistributorDetails import Ui_DistributorDetails
from NewPaymentForm import Ui_NewShipmentForm
from NewShipmentform import Ui_NewShipmentForm
from OrderStatusDetails import Ui_PaymentDetails
from PaymentDetails import Ui_PaymentDetails
from ShipmentDetails import Ui_NewShipmentForm

from PromotionDetails import Ui_PromotionDetails
from EmployeeDetails import Ui_EmployeeDetails
from ManufacturerDetails import  Ui_ManufacturerDetails
from EmployeeStatusDetails import Ui_EmployeeStatusDetails
from ManufacturerStatusDetails import Ui_ManufacturerStatusDetails
from Promotion import Ui_Promotion
from NewCustomerForm import Ui_NewCustomerForm
from NewEmployeeForm import Ui_NewEmployeeForm
from ChannelDetailsForm import Ui_ChannelDetails
from CustomerDetailsForm import Ui_CustomerDetailsForm_2
from DistributorContactForm import Ui_DistributorContactForm
from ManufacturerContactForm import Ui_ManufacturerContact


counter = 0


# Loading Screen - DO NOT TOUCH
class LoadingWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_LoadingScreen()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.WindowFlags.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(35)
        self.ui.dropshadowframe.setGraphicsEffect(self.shadow)
        self.ui.label_description.setText("<strong>WELCOME</strong> To Our Customer Relationship Management System")
        QtCore.QTimer.singleShot(1500, lambda: self.ui.label_description.setText("<strong>LOADING</strong> DATABASE"))
        QtCore.QTimer.singleShot(3000,
                                 lambda: self.ui.label_description.setText("<strong>LOADING</strong> USER INTERFACE"))
        self.show()

    def progress(self):
        global counter
        self.ui.progressBar.setValue(counter)
        if counter > 100:
            self.timer.stop()
            self.open_mainscreen()
            self.close()
        counter += 1

    def open_mainscreen(self):
        self.ui = MainScreen()
        self.ui.show()
        self.ui.load_forms()


class MainScreen(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_MainScreen()
        self.ui.setupUi(self)
        self.ui.openform_button.clicked.connect(self.open_forms)

    # ADDS FORM NAMES TO FORM DROPDOWN LIST
    # todo: add all forms to this list
    # IDEA: We can create a text file or csv file and have it read the list of forms there
    def load_forms(self):
        self.ui.comboBox_form.addItems(["New Product Form", "Product Detail Form", "Product Color Detail",
                                        "Product Rating Detail", "Product Status Detail", ""])

    # THIS FUNCTION IS CALLED WHEN THE OPEN FORM BUTTON IS CLICKED
    # todo: add logic for each form
    def open_forms(self):
        # Retrieves selected value from drop down list
        selected = self.ui.comboBox_form.currentText()
        if selected == "New Product Form":
            self.open_productform()
        elif selected == "Product Detail Form":
            self.open_productdetail()
        elif selected == "Product Color Detail":
            self.open_productcolordetail()
        elif selected == "Product Rating Detail":
            self.open_productratingdetail()
        elif selected == "Product Status Detail":
            self.open_productstatusdetail()

    # ==> PLACE FORM DISPLAY FUNCTIONS BELOW HERE
    # todo: add functions to open all forms
    # NEW PRODUCT FORM
    def open_productform(self):
        self.form = NewProductForm()  # This is set to the design class name
        self.form.show()

    # PRODUCT DETAIL FORM
    def open_productdetail(self):
        self.form = ProductDetail()
        self.form.show()

    # PRODUCT COLOR DETAIL
    def open_productcolordetail(self):
        self.form = ProductColorDetail()
        self.form.show()

    # PRODUCT RATING DETAIL
    def open_productratingdetail(self):
        self.form = ProductRatingDetail()
        self.form.show()

    # PRODUCT STATUS DETAIL
    def open_productstatusdetail(self):
        self.form = ProductStatusDetail()
        self.form.show()

    # PRODUCT TYPE DETAIL
    def open_producttypedetail(self):
        self.form = ProductTypeDetail()
        self.form.show()

    # NEW CUSTOMER FORM
    def open_NewCustomerForm(self):
        self.form = NewCustomerForm()
        self.form.show()
        
    # NEW EMPLOYEE FORM
    def open_NewEmployeeForm(self):
        self.form = NewEmployeeForm()
        self.form.show()

    # CHANNEL DETAILS FORM
    def open_ChannelDetailsForm(self):
        self.form = ChannelDetailsForm()
        self.form.show()

    # CUSTOMER DETAILS FORM
    def open_CustomerDetailsForm(self):
        self.form = CustomerDetailsForm()
        self.form.show()

    # DISTRIBUTOR CONTACT FORM
    def open_DistributorContactForm(self):
        self.form = DistributorContactForm()
        self.form.show()

    # MANUFACTURER CONTACT FORM
    def open_ManufacturerContactForm(self):
        self.form = ManufacturerContactForm()
        self.form.show()
    
    # EMPLOYEE DETAILS
    def open_employeedetails(self):
        self.form = EmployeeDetails()
        self.form.show()

    # EMPLOYEE STATUS DETAILS
    def open_employeestatusdetails(self):
        self.form = EmployeeStatusDetails()
        self.form.show()

    # MANUFACTURER DETAILS
    def open_manufacturerdetails(self):
        self.form = ManufacturerDetails()
        self.form.show()

    # MANUFACTURER STATUS DETAILS
    def open_manufacturerstatusdetails(self):
        self.form = ManufacturerStatusDetails()
        self.form.show()

    # PROMOTION
    def open_promotion(self):
        self.form = Promotion()
        self.form.show()

    # PROMOTION DETAILS
    def open_promotiondetails(self):
        self.form = PromotionDetails()
        self.form.show()

    # DISTRIBUTOR DETAILS
    def open_distributordetails(self):
        self.form = DistributorDetails()
        self.form.show()

    # NEW PAYMENT
    def open_newpayment(self):
        self.form = NewPaymentForm()
        self.form.show()

    # NEW SHIPMENT
    def open_newshipment(self):
        self.form = NewShipmentform()
        self.form.show()

    # ORDER STATUS DETAILS
    def open_orderstatus(self):
        self.form = OrderStatusDetails()
        self.form.show()

    # PAYMENT DETAILS
    def open_paymentdetails(self):
        self.form = PaymentDetails()
        self.form.show()

    # SHIPMENT DETAILS
    def open_shipmentdetails(self):
        self.form = ShipmentDetails()
        self.form.show()


# ==> PLACE DESIGN CLASSES BELOW HERE
# REQ: All form functionality will be added here
# todo: Create classes for all forms
class NewProductForm(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_NewProductForm()
        self.ui.setupUi(self)


class ProductDetail(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_ProductDetails()
        self.ui.setupUi(self)


class ProductColorDetail(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_ProductColorDetail()
        self.ui.setupUi(self)


class ProductRatingDetail(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_ProductRatingDetail()
        self.ui.setupUi(self)


class ProductStatusDetail(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_ProductStatusDetail()
        self.ui.setupUi(self)


class EmployeeDetails(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_EmployeeDetails()
        self.ui.setupUi(self)


class EmployeeStatusDetails(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_EmployeeStatusDetails()
        self.ui.setupUi(self)


class ManufacturerDetails(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_ManufacturerDetails()
        self.ui.setupUi(self)


class ManufacturerStatusDetails(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_ManufacturerStatusDetails()
        self.ui.setupUi(self)


class Promotion(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_Promotion()
        self.ui.setupUi(self)


class PromotionDetails(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_PromotionDetails()
        self.ui.setupUi(self)


class NewCustomerForm(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_NewCustomerForm()
        self.ui.setupUi(self)


class NewEmployeeForm(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_NewEmployeeForm()
        self.ui.setupUi(self)


class ChannelDetailsForm(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_ChannelDetails()
        self.ui.setupUi(self)    


class CustomerDetailsForm(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_CustomerDetailsForm_2()
        self.ui.setupUi(self) 


class DistributorContactForm(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_DistributorContactForm()
        self.ui.setupUi(self)


class ManufacturerContactForm(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_ManufacturerContact()
        self.ui.setupUi(self) 


class DistributorDetails(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_DistributorDetails()
        self.ui.setupUi(self)


class NewPaymentForm(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_NewShipmentForm()
        self.ui.setupUi(self)


class NewShipmentform(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_NewShipmentForm()
        self.ui.setupUi(self)


class OrderStatusDetails(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_PaymentDetails()
        self.ui.setupUi(self)


class PaymentDetails(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_PaymentDetails()
        self.ui.setupUi(self)


class ShipmentDetails(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_NewShipmentForm()
        self.ui.setupUi(self)


class ProductTypeDetail(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_ProductTypeDetail()
        self.ui.setupUi(self)


if __name__ == '__main__':
    app = QApplication([])
    window = LoadingWindow()
    app.exec()
