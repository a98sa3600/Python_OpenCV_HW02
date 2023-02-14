# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 40, 241, 491))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 30, 211, 451))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.load_image_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.load_image_button.setObjectName("load_image_button")
        self.verticalLayout.addWidget(self.load_image_button)
        self.show_image_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.show_image_button.setObjectName("show_image_button")
        self.verticalLayout.addWidget(self.show_image_button)
        self.show_distribution_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.show_distribution_button.setObjectName("show_distribution_button")
        self.verticalLayout.addWidget(self.show_distribution_button)
        self.show_model_structure_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.show_model_structure_button.setObjectName("show_model_structure_button")
        self.verticalLayout.addWidget(self.show_model_structure_button)
        self.show_comparision_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.show_comparision_button.setObjectName("show_comparision_button")
        self.verticalLayout.addWidget(self.show_comparision_button)
        self.inference_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.inference_button.setObjectName("inference_button")
        self.verticalLayout.addWidget(self.inference_button)
        self.label_image = QtWidgets.QLabel(self.centralwidget)
        self.label_image.setGeometry(QtCore.QRect(360, 70, 331, 361))
        self.label_image.setText("")
        self.label_image.setObjectName("label_image")
        self.label_predict = QtWidgets.QLabel(self.centralwidget)
        self.label_predict.setGeometry(QtCore.QRect(310, 450, 441, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_predict.setFont(font)
        self.label_predict.setAlignment(QtCore.Qt.AlignCenter)
        self.label_predict.setObjectName("label_predict")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "5.ResNet50"))
        self.load_image_button.setText(_translate("MainWindow", "Load Image"))
        self.show_image_button.setText(_translate("MainWindow", "1. Show Images"))
        self.show_distribution_button.setText(_translate("MainWindow", "2. Show Distribution"))
        self.show_model_structure_button.setText(_translate("MainWindow", "3. Show Model Structure"))
        self.show_comparision_button.setText(_translate("MainWindow", "4. Show Comparison"))
        self.inference_button.setText(_translate("MainWindow", "5. Inference"))
        self.label_predict.setText(_translate("MainWindow", "Prediction:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())