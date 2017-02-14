# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'inventory.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_inventoryWindow(object):
    def setupUi(self, inventoryWindow):
        inventoryWindow.setObjectName(_fromUtf8("inventoryWindow"))
        inventoryWindow.resize(1110, 672)
        inventoryWindow.setStyleSheet(_fromUtf8("QPushButton {padding: 10px}\n"
"QWidget {background-color: white}\n"
""))
        self.centralwidget = QtGui.QWidget(inventoryWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_3 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans"))
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(_fromUtf8("font: 24pt \"Noto Sans\";"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 3, QtCore.Qt.AlignHCenter)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 1, 0, 1, 3)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.partID = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.partID.setFont(font)
        self.partID.setObjectName(_fromUtf8("partID"))
        self.gridLayout.addWidget(self.partID, 2, 1, 1, 1)
        self.partBox = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.partBox.setFont(font)
        self.partBox.setObjectName(_fromUtf8("partBox"))
        self.gridLayout.addWidget(self.partBox, 5, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.partQty = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.partQty.setFont(font)
        self.partQty.setObjectName(_fromUtf8("partQty"))
        self.gridLayout.addWidget(self.partQty, 6, 1, 1, 1)
        self.addToCartButton = QtGui.QPushButton(self.centralwidget)
        self.addToCartButton.setObjectName(_fromUtf8("addToCartButton"))
        self.gridLayout.addWidget(self.addToCartButton, 8, 0, 1, 1)
        self.label_12 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout.addWidget(self.label_12, 6, 0, 1, 1)
        self.partName = QtGui.QLabel(self.centralwidget)
        self.partName.setMinimumSize(QtCore.QSize(400, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans"))
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.partName.setFont(font)
        self.partName.setStyleSheet(_fromUtf8("font: 20pt \"Noto Sans\";"))
        self.partName.setObjectName(_fromUtf8("partName"))
        self.gridLayout.addWidget(self.partName, 0, 0, 1, 2)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 7, 0, 1, 2)
        self.partRFID = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.partRFID.setFont(font)
        self.partRFID.setObjectName(_fromUtf8("partRFID"))
        self.gridLayout.addWidget(self.partRFID, 3, 1, 1, 1)
        self.label_11 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout.addWidget(self.label_11, 3, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)
        self.qtySpinBox = QtGui.QSpinBox(self.centralwidget)
        self.qtySpinBox.setMinimumSize(QtCore.QSize(0, 45))
        self.qtySpinBox.setObjectName(_fromUtf8("qtySpinBox"))
        self.gridLayout.addWidget(self.qtySpinBox, 8, 1, 1, 1)
        self.partShelf = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.partShelf.setFont(font)
        self.partShelf.setObjectName(_fromUtf8("partShelf"))
        self.gridLayout.addWidget(self.partShelf, 4, 1, 1, 1)
        self.partCategory = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans"))
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.partCategory.setFont(font)
        self.partCategory.setStyleSheet(_fromUtf8("font: italic 16pt \"Noto Sans\";"))
        self.partCategory.setObjectName(_fromUtf8("partCategory"))
        self.gridLayout.addWidget(self.partCategory, 1, 0, 1, 2)
        self.gridLayout_2.addLayout(self.gridLayout, 4, 2, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 6, 0, 1, 3)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 9, 0, 1, 3)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 4, 1, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(self.centralwidget)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout_2.addWidget(self.buttonBox, 8, 0, 1, 3, QtCore.Qt.AlignHCenter)
        self.cartButton = QtGui.QPushButton(self.centralwidget)
        self.cartButton.setObjectName(_fromUtf8("cartButton"))
        self.gridLayout_2.addWidget(self.cartButton, 5, 2, 1, 1)
        self.treeView = QtGui.QTreeView(self.centralwidget)
        self.treeView.setMinimumSize(QtCore.QSize(400, 350))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.treeView.setFont(font)
        self.treeView.setMouseTracking(False)
        self.treeView.setFrameShape(QtGui.QFrame.StyledPanel)
        self.treeView.setFrameShadow(QtGui.QFrame.Sunken)
        self.treeView.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.treeView.setAlternatingRowColors(True)
        self.treeView.setHeaderHidden(True)
        self.treeView.setObjectName(_fromUtf8("treeView"))
        self.gridLayout_2.addWidget(self.treeView, 4, 0, 2, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 1, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem5, 0, 0, 1, 1)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem6, 0, 2, 1, 1)
        inventoryWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(inventoryWindow)
        QtCore.QMetaObject.connectSlotsByName(inventoryWindow)

    def retranslateUi(self, inventoryWindow):
        inventoryWindow.setWindowTitle(_translate("inventoryWindow", "MainWindow", None))
        self.label_2.setText(_translate("inventoryWindow", "Inventory Browser", None))
        self.partID.setText(_translate("inventoryWindow", "035", None))
        self.partBox.setText(_translate("inventoryWindow", "5", None))
        self.label_4.setText(_translate("inventoryWindow", "Shelf", None))
        self.partQty.setText(_translate("inventoryWindow", "5", None))
        self.addToCartButton.setText(_translate("inventoryWindow", "Add to Cart", None))
        self.label_12.setText(_translate("inventoryWindow", "Available Quantity", None))
        self.partName.setText(_translate("inventoryWindow", "<html><head/><body><p align=\"center\">ATMega328</p></body></html>", None))
        self.partRFID.setText(_translate("inventoryWindow", "68206165", None))
        self.label_11.setText(_translate("inventoryWindow", "RFID", None))
        self.label_3.setText(_translate("inventoryWindow", "ID", None))
        self.label_5.setText(_translate("inventoryWindow", "Box", None))
        self.partShelf.setText(_translate("inventoryWindow", "3", None))
        self.partCategory.setText(_translate("inventoryWindow", "<html><head/><body><p align=\"center\"><span style=\" font-style:italic;\">Microcontroller</span></p></body></html>", None))
        self.cartButton.setText(_translate("inventoryWindow", "View Cart", None))

