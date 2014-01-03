# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_nvdb.ui'
#
# Created: Thu Jan 02 13:48:22 2014
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Nvdb(object):
    def setupUi(self, Nvdb):
        Nvdb.setObjectName(_fromUtf8("Nvdb"))
        Nvdb.resize(313, 174)
        self.layoutWidget = QtGui.QWidget(Nvdb)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 20, 261, 128))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_5 = QtGui.QLabel(self.layoutWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 2, 0, 1, 1)
        self.comboBoxFylke = QtGui.QComboBox(self.layoutWidget)
        self.comboBoxFylke.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.comboBoxFylke.setObjectName(_fromUtf8("comboBoxFylke"))
        self.comboBoxFylke.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.comboBoxFylke, 1, 1, 1, 2)
        self.label_4 = QtGui.QLabel(self.layoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)
        self.comboBoxKommune = QtGui.QComboBox(self.layoutWidget)
        self.comboBoxKommune.setObjectName(_fromUtf8("comboBoxKommune"))
        self.comboBoxKommune.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.comboBoxKommune, 2, 1, 1, 2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.E = QtGui.QCheckBox(self.layoutWidget)
        self.E.setChecked(True)
        self.E.setObjectName(_fromUtf8("E"))
        self.horizontalLayout_3.addWidget(self.E)
        self.R = QtGui.QCheckBox(self.layoutWidget)
        self.R.setChecked(True)
        self.R.setObjectName(_fromUtf8("R"))
        self.horizontalLayout_3.addWidget(self.R)
        self.F = QtGui.QCheckBox(self.layoutWidget)
        self.F.setChecked(True)
        self.F.setObjectName(_fromUtf8("F"))
        self.horizontalLayout_3.addWidget(self.F)
        self.K = QtGui.QCheckBox(self.layoutWidget)
        self.K.setObjectName(_fromUtf8("K"))
        self.horizontalLayout_3.addWidget(self.K)
        self.P = QtGui.QCheckBox(self.layoutWidget)
        self.P.setObjectName(_fromUtf8("P"))
        self.horizontalLayout_3.addWidget(self.P)
        self.S = QtGui.QCheckBox(self.layoutWidget)
        self.S.setObjectName(_fromUtf8("S"))
        self.horizontalLayout_3.addWidget(self.S)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 3, 0, 1, 3)
        self.pushButton = QtGui.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout_2.addWidget(self.pushButton, 4, 0, 1, 3)
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.comboBoxObjekttype = QtGui.QComboBox(self.layoutWidget)
        self.comboBoxObjekttype.setObjectName(_fromUtf8("comboBoxObjekttype"))
        self.comboBoxObjekttype.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.comboBoxObjekttype, 0, 1, 1, 2)

        self.retranslateUi(Nvdb)
        QtCore.QMetaObject.connectSlotsByName(Nvdb)

    def retranslateUi(self, Nvdb):
        Nvdb.setWindowTitle(QtGui.QApplication.translate("Nvdb", "Nvdb", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Nvdb", "Kommune", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxFylke.setItemText(0, QtGui.QApplication.translate("Nvdb", "Hele Norge", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Nvdb", "Fylke", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxKommune.setItemText(0, QtGui.QApplication.translate("Nvdb", "Velg fylke", None, QtGui.QApplication.UnicodeUTF8))
        self.E.setText(QtGui.QApplication.translate("Nvdb", "E", None, QtGui.QApplication.UnicodeUTF8))
        self.R.setText(QtGui.QApplication.translate("Nvdb", "R", None, QtGui.QApplication.UnicodeUTF8))
        self.F.setText(QtGui.QApplication.translate("Nvdb", "F", None, QtGui.QApplication.UnicodeUTF8))
        self.K.setText(QtGui.QApplication.translate("Nvdb", "K", None, QtGui.QApplication.UnicodeUTF8))
        self.P.setText(QtGui.QApplication.translate("Nvdb", "P", None, QtGui.QApplication.UnicodeUTF8))
        self.S.setText(QtGui.QApplication.translate("Nvdb", "S", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Nvdb", "Legg til lag", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Nvdb", "Objekttype", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxObjekttype.setItemText(0, QtGui.QApplication.translate("Nvdb", "Vegnett", None, QtGui.QApplication.UnicodeUTF8))

