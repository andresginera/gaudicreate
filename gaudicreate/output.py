# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'output.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_GeneticalAlgorithm(object):
    def setupUi(self, GeneticalAlgorithm):
        GeneticalAlgorithm.setObjectName("GeneticalAlgorithm")
        GeneticalAlgorithm.resize(527, 382)
        GeneticalAlgorithm.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        GeneticalAlgorithm.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout(GeneticalAlgorithm)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(GeneticalAlgorithm)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.lineEdit = QtWidgets.QLineEdit(GeneticalAlgorithm)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(GeneticalAlgorithm)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(GeneticalAlgorithm)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setItalic(True)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(GeneticalAlgorithm)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setItalic(True)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_2.addWidget(self.lineEdit_3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.checkBox = QtWidgets.QCheckBox(GeneticalAlgorithm)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_8.addWidget(self.checkBox)
        self.verticalLayout_6.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.checkBox_2 = QtWidgets.QCheckBox(GeneticalAlgorithm)
        self.checkBox_2.setObjectName("checkBox_2")
        self.horizontalLayout_9.addWidget(self.checkBox_2)
        self.verticalLayout_6.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.checkBox_3 = QtWidgets.QCheckBox(GeneticalAlgorithm)
        self.checkBox_3.setObjectName("checkBox_3")
        self.horizontalLayout_10.addWidget(self.checkBox_3)
        self.verticalLayout_6.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_3.addLayout(self.verticalLayout_6)
        spacerItem = QtWidgets.QSpacerItem(30, 10, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.checkBox_4 = QtWidgets.QCheckBox(GeneticalAlgorithm)
        self.checkBox_4.setObjectName("checkBox_4")
        self.horizontalLayout_6.addWidget(self.checkBox_4)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.check_every = QtWidgets.QCheckBox(GeneticalAlgorithm)
        self.check_every.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.check_every.sizePolicy().hasHeightForWidth())
        self.check_every.setSizePolicy(sizePolicy)
        self.check_every.setObjectName("check_every")
        self.horizontalLayout_4.addWidget(self.check_every)
        self.lineEdit_4 = QtWidgets.QLineEdit(GeneticalAlgorithm)
        self.lineEdit_4.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy)
        self.lineEdit_4.setMaximumSize(QtCore.QSize(40, 21))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_4.addWidget(self.lineEdit_4)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.checkBox_6 = QtWidgets.QCheckBox(GeneticalAlgorithm)
        self.checkBox_6.setObjectName("checkBox_6")
        self.horizontalLayout_7.addWidget(self.checkBox_6)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(GeneticalAlgorithm)
        self.check_every.clicked['bool'].connect(self.lineEdit_4.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(GeneticalAlgorithm)

    def retranslateUi(self, GeneticalAlgorithm):
        _translate = QtCore.QCoreApplication.translate
        GeneticalAlgorithm.setWindowTitle(_translate("GeneticalAlgorithm", "GroupBox"))
        GeneticalAlgorithm.setTitle(_translate("GeneticalAlgorithm", "Output"))
        self.pushButton.setText(_translate("GeneticalAlgorithm", "Save as"))
        self.label_2.setText(_translate("GeneticalAlgorithm", "Precision: "))
        self.lineEdit_2.setText(_translate("GeneticalAlgorithm", "min"))
        self.lineEdit_3.setText(_translate("GeneticalAlgorithm", "max"))
        self.checkBox.setText(_translate("GeneticalAlgorithm", "Compress"))
        self.checkBox_2.setText(_translate("GeneticalAlgorithm", "History"))
        self.checkBox_3.setText(_translate("GeneticalAlgorithm", "Pareto"))
        self.checkBox_4.setText(_translate("GeneticalAlgorithm", "Verbose"))
        self.check_every.setText(_translate("GeneticalAlgorithm", "Check Every"))
        self.checkBox_6.setText(_translate("GeneticalAlgorithm", "Prompt on exception"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GeneticalAlgorithm = QtWidgets.QGroupBox()
    ui = Ui_GeneticalAlgorithm()
    ui.setupUi(GeneticalAlgorithm)
    GeneticalAlgorithm.show()
    sys.exit(app.exec_())
