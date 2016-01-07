# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Z:\src\tiled\editterraindialog.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_EditTerrainDialog(object):
    def setupUi(self, EditTerrainDialog):
        EditTerrainDialog.setObjectName("EditTerrainDialog")
        EditTerrainDialog.resize(615, 372)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(EditTerrainDialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.undo = QtWidgets.QToolButton(EditTerrainDialog)
        self.undo.setEnabled(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/24x24/edit-undo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.undo.setIcon(icon)
        self.undo.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.undo.setAutoRaise(True)
        self.undo.setObjectName("undo")
        self.horizontalLayout_3.addWidget(self.undo)
        self.redo = QtWidgets.QToolButton(EditTerrainDialog)
        self.redo.setEnabled(False)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/24x24/edit-redo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.redo.setIcon(icon1)
        self.redo.setAutoRaise(True)
        self.redo.setObjectName("redo")
        self.horizontalLayout_3.addWidget(self.redo)
        self.eraseTerrain = QtWidgets.QToolButton(EditTerrainDialog)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/22x22/stock-tool-eraser.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.eraseTerrain.setIcon(icon2)
        self.eraseTerrain.setCheckable(True)
        self.eraseTerrain.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.eraseTerrain.setAutoRaise(True)
        self.eraseTerrain.setObjectName("eraseTerrain")
        self.horizontalLayout_3.addWidget(self.eraseTerrain)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.zoomComboBox = QtWidgets.QComboBox(EditTerrainDialog)
        self.zoomComboBox.setObjectName("zoomComboBox")
        self.horizontalLayout_3.addWidget(self.zoomComboBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.terrainList = TerrainView(EditTerrainDialog)
        self.terrainList.setMaximumSize(QtCore.QSize(200, 16777215))
        self.terrainList.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.terrainList.setIndentation(0)
        self.terrainList.setRootIsDecorated(False)
        self.terrainList.setItemsExpandable(False)
        self.terrainList.setObjectName("terrainList")
        self.terrainList.header().setVisible(False)
        self.verticalLayout.addWidget(self.terrainList)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.tilesetView = TilesetView(EditTerrainDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tilesetView.sizePolicy().hasHeightForWidth())
        self.tilesetView.setSizePolicy(sizePolicy)
        self.tilesetView.setMinimumSize(QtCore.QSize(200, 0))
        self.tilesetView.setObjectName("tilesetView")
        self.horizontalLayout_2.addWidget(self.tilesetView)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.addTerrainTypeButton = QtWidgets.QToolButton(EditTerrainDialog)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/22x22/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addTerrainTypeButton.setIcon(icon3)
        self.addTerrainTypeButton.setAutoRaise(True)
        self.addTerrainTypeButton.setObjectName("addTerrainTypeButton")
        self.horizontalLayout.addWidget(self.addTerrainTypeButton)
        self.removeTerrainTypeButton = QtWidgets.QToolButton(EditTerrainDialog)
        self.removeTerrainTypeButton.setEnabled(False)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images/22x22/remove.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.removeTerrainTypeButton.setIcon(icon4)
        self.removeTerrainTypeButton.setAutoRaise(True)
        self.removeTerrainTypeButton.setObjectName("removeTerrainTypeButton")
        self.horizontalLayout.addWidget(self.removeTerrainTypeButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(EditTerrainDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(EditTerrainDialog)
        self.buttonBox.accepted.connect(EditTerrainDialog.accept)
        self.buttonBox.rejected.connect(EditTerrainDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(EditTerrainDialog)
        EditTerrainDialog.setTabOrder(self.tilesetView, self.addTerrainTypeButton)
        EditTerrainDialog.setTabOrder(self.addTerrainTypeButton, self.removeTerrainTypeButton)
        EditTerrainDialog.setTabOrder(self.removeTerrainTypeButton, self.buttonBox)

    def retranslateUi(self, EditTerrainDialog):
        _translate = QtCore.QCoreApplication.translate
        EditTerrainDialog.setWindowTitle(_translate("EditTerrainDialog", "Edit Terrain Information"))
        self.undo.setToolTip(_translate("EditTerrainDialog", "Undo"))
        self.undo.setText(_translate("EditTerrainDialog", "Undo"))
        self.redo.setToolTip(_translate("EditTerrainDialog", "Redo"))
        self.redo.setText(_translate("EditTerrainDialog", "Redo"))
        self.eraseTerrain.setText(_translate("EditTerrainDialog", "Erase"))
        self.addTerrainTypeButton.setToolTip(_translate("EditTerrainDialog", "Add Terrain Type"))
        self.addTerrainTypeButton.setText(_translate("EditTerrainDialog", "Add"))
        self.removeTerrainTypeButton.setToolTip(_translate("EditTerrainDialog", "Remove Terrain Type"))
        self.removeTerrainTypeButton.setText(_translate("EditTerrainDialog", "Remove"))

from tilesetview import TilesetView
from terrainview import TerrainView
import tiled_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EditTerrainDialog = QtWidgets.QDialog()
    ui = Ui_EditTerrainDialog()
    ui.setupUi(EditTerrainDialog)
    EditTerrainDialog.show()
    sys.exit(app.exec_())

