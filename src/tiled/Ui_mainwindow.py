# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\opensource\tiled\src\tiled\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(553, 367)
        MainWindow.setAcceptDrops(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/32x32/tiled.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 553, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuRecentFiles = QtWidgets.QMenu(self.menuFile)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/16x16/document-open-recent.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuRecentFiles.setIcon(icon1)
        self.menuRecentFiles.setObjectName("menuRecentFiles")
        self.menuEdit = QtWidgets.QMenu(self.menuBar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuMap = QtWidgets.QMenu(self.menuBar)
        self.menuMap.setObjectName("menuMap")
        self.menuView = QtWidgets.QMenu(self.menuBar)
        self.menuView.setObjectName("menuView")
        self.menuShowObjectNames = QtWidgets.QMenu(self.menuView)
        self.menuShowObjectNames.setObjectName("menuShowObjectNames")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.toolsToolBar = QtWidgets.QToolBar(MainWindow)
        self.toolsToolBar.setObjectName("toolsToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolsToolBar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/16x16/document-open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon2)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/16x16/document-save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon3)
        self.actionSave.setObjectName("actionSave")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images/16x16/application-exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionQuit.setIcon(icon4)
        self.actionQuit.setMenuRole(QtWidgets.QAction.QuitRole)
        self.actionQuit.setObjectName("actionQuit")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setEnabled(False)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/images/16x16/edit-copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCopy.setIcon(icon5)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setEnabled(False)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/images/16x16/edit-paste.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPaste.setIcon(icon6)
        self.actionPaste.setObjectName("actionPaste")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/images/16x16/help-about.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout.setIcon(icon7)
        self.actionAbout.setMenuRole(QtWidgets.QAction.AboutRole)
        self.actionAbout.setObjectName("actionAbout")
        self.actionAboutQt = QtWidgets.QAction(MainWindow)
        self.actionAboutQt.setMenuRole(QtWidgets.QAction.AboutQtRole)
        self.actionAboutQt.setObjectName("actionAboutQt")
        self.actionResizeMap = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/images/16x16/document-page-setup.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionResizeMap.setIcon(icon8)
        self.actionResizeMap.setObjectName("actionResizeMap")
        self.actionMapProperties = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/images/16x16/document-properties.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionMapProperties.setIcon(icon9)
        self.actionMapProperties.setObjectName("actionMapProperties")
        self.actionAutoMap = QtWidgets.QAction(MainWindow)
        self.actionAutoMap.setObjectName("actionAutoMap")
        self.actionShowGrid = QtWidgets.QAction(MainWindow)
        self.actionShowGrid.setCheckable(True)
        self.actionShowGrid.setObjectName("actionShowGrid")
        self.actionSaveAs = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/images/16x16/document-save-as.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSaveAs.setIcon(icon10)
        self.actionSaveAs.setObjectName("actionSaveAs")
        self.actionNew = QtWidgets.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/images/16x16/document-new.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew.setIcon(icon11)
        self.actionNew.setObjectName("actionNew")
        self.actionNewTileset = QtWidgets.QAction(MainWindow)
        self.actionNewTileset.setIcon(icon11)
        self.actionNewTileset.setObjectName("actionNewTileset")
        self.actionClose = QtWidgets.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/images/16x16/window-close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClose.setIcon(icon12)
        self.actionClose.setObjectName("actionClose")
        self.actionZoomIn = QtWidgets.QAction(MainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/images/16x16/zoom-in.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionZoomIn.setIcon(icon13)
        self.actionZoomIn.setObjectName("actionZoomIn")
        self.actionZoomOut = QtWidgets.QAction(MainWindow)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/images/16x16/zoom-out.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionZoomOut.setIcon(icon14)
        self.actionZoomOut.setObjectName("actionZoomOut")
        self.actionZoomNormal = QtWidgets.QAction(MainWindow)
        self.actionZoomNormal.setEnabled(False)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/images/16x16/zoom-original.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionZoomNormal.setIcon(icon15)
        self.actionZoomNormal.setObjectName("actionZoomNormal")
        self.actionExportAsImage = QtWidgets.QAction(MainWindow)
        self.actionExportAsImage.setObjectName("actionExportAsImage")
        self.actionCut = QtWidgets.QAction(MainWindow)
        self.actionCut.setEnabled(False)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(":/images/16x16/edit-cut.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCut.setIcon(icon16)
        self.actionCut.setObjectName("actionCut")
        self.actionOffsetMap = QtWidgets.QAction(MainWindow)
        self.actionOffsetMap.setObjectName("actionOffsetMap")
        self.actionPreferences = QtWidgets.QAction(MainWindow)
        self.actionPreferences.setMenuRole(QtWidgets.QAction.PreferencesRole)
        self.actionPreferences.setObjectName("actionPreferences")
        self.actionClearRecentFiles = QtWidgets.QAction(MainWindow)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(":/images/16x16/edit-clear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClearRecentFiles.setIcon(icon17)
        self.actionClearRecentFiles.setObjectName("actionClearRecentFiles")
        self.actionExportAs = QtWidgets.QAction(MainWindow)
        self.actionExportAs.setObjectName("actionExportAs")
        self.actionAddExternalTileset = QtWidgets.QAction(MainWindow)
        self.actionAddExternalTileset.setObjectName("actionAddExternalTileset")
        self.actionSnapToGrid = QtWidgets.QAction(MainWindow)
        self.actionSnapToGrid.setCheckable(True)
        self.actionSnapToGrid.setObjectName("actionSnapToGrid")
        self.actionCloseAll = QtWidgets.QAction(MainWindow)
        self.actionCloseAll.setObjectName("actionCloseAll")
        self.actionDelete = QtWidgets.QAction(MainWindow)
        self.actionDelete.setEnabled(False)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(":/images/16x16/edit-delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDelete.setIcon(icon18)
        self.actionDelete.setObjectName("actionDelete")
        self.actionHighlightCurrentLayer = QtWidgets.QAction(MainWindow)
        self.actionHighlightCurrentLayer.setCheckable(True)
        self.actionHighlightCurrentLayer.setObjectName("actionHighlightCurrentLayer")
        self.actionShowTileObjectOutlines = QtWidgets.QAction(MainWindow)
        self.actionShowTileObjectOutlines.setCheckable(True)
        self.actionShowTileObjectOutlines.setObjectName("actionShowTileObjectOutlines")
        self.actionSnapToFineGrid = QtWidgets.QAction(MainWindow)
        self.actionSnapToFineGrid.setCheckable(True)
        self.actionSnapToFineGrid.setObjectName("actionSnapToFineGrid")
        self.actionShowTileAnimations = QtWidgets.QAction(MainWindow)
        self.actionShowTileAnimations.setCheckable(True)
        self.actionShowTileAnimations.setObjectName("actionShowTileAnimations")
        self.actionReload = QtWidgets.QAction(MainWindow)
        self.actionReload.setObjectName("actionReload")
        self.actionExport = QtWidgets.QAction(MainWindow)
        self.actionExport.setObjectName("actionExport")
        self.actionBecomePatron = QtWidgets.QAction(MainWindow)
        self.actionBecomePatron.setObjectName("actionBecomePatron")
        self.actionSaveAll = QtWidgets.QAction(MainWindow)
        self.actionSaveAll.setObjectName("actionSaveAll")
        self.actionDocumentation = QtWidgets.QAction(MainWindow)
        self.actionDocumentation.setObjectName("actionDocumentation")
        self.actionNoLabels = QtWidgets.QAction(MainWindow)
        self.actionNoLabels.setCheckable(True)
        self.actionNoLabels.setObjectName("actionNoLabels")
        self.actionLabelsForSelectedObjects = QtWidgets.QAction(MainWindow)
        self.actionLabelsForSelectedObjects.setCheckable(True)
        self.actionLabelsForSelectedObjects.setChecked(True)
        self.actionLabelsForSelectedObjects.setObjectName("actionLabelsForSelectedObjects")
        self.actionLabelsForAllObjects = QtWidgets.QAction(MainWindow)
        self.actionLabelsForAllObjects.setCheckable(True)
        self.actionLabelsForAllObjects.setObjectName("actionLabelsForAllObjects")
        self.menuRecentFiles.addAction(self.actionClearRecentFiles)
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.menuRecentFiles.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSaveAs)
        self.menuFile.addAction(self.actionSaveAll)
        self.menuFile.addAction(self.actionExport)
        self.menuFile.addAction(self.actionExportAs)
        self.menuFile.addAction(self.actionExportAsImage)
        self.menuFile.addAction(self.actionReload)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose)
        self.menuFile.addAction(self.actionCloseAll)
        self.menuFile.addAction(self.actionQuit)
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addAction(self.actionDelete)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionPreferences)
        self.menuHelp.addAction(self.actionDocumentation)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionBecomePatron)
        self.menuHelp.addAction(self.actionAbout)
        self.menuMap.addAction(self.actionNewTileset)
        self.menuMap.addAction(self.actionAddExternalTileset)
        self.menuMap.addSeparator()
        self.menuMap.addAction(self.actionResizeMap)
        self.menuMap.addAction(self.actionOffsetMap)
        self.menuMap.addSeparator()
        self.menuMap.addAction(self.actionMapProperties)
        self.menuMap.addAction(self.actionAutoMap)
        self.menuShowObjectNames.addAction(self.actionNoLabels)
        self.menuShowObjectNames.addAction(self.actionLabelsForSelectedObjects)
        self.menuShowObjectNames.addAction(self.actionLabelsForAllObjects)
        self.menuView.addAction(self.actionShowGrid)
        self.menuView.addAction(self.actionShowTileObjectOutlines)
        self.menuView.addAction(self.menuShowObjectNames.menuAction())
        self.menuView.addAction(self.actionShowTileAnimations)
        self.menuView.addAction(self.actionHighlightCurrentLayer)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionSnapToGrid)
        self.menuView.addAction(self.actionSnapToFineGrid)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionZoomIn)
        self.menuView.addAction(self.actionZoomOut)
        self.menuView.addAction(self.actionZoomNormal)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuEdit.menuAction())
        self.menuBar.addAction(self.menuView.menuAction())
        self.menuBar.addAction(self.menuMap.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())
        self.mainToolBar.addAction(self.actionNew)
        self.mainToolBar.addAction(self.actionOpen)
        self.mainToolBar.addAction(self.actionSave)
        self.mainToolBar.addSeparator()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.menuFile.setTitle(_translate("MainWindow", "&File"))
        self.menuRecentFiles.setTitle(_translate("MainWindow", "&Recent Files"))
        self.menuEdit.setTitle(_translate("MainWindow", "&Edit"))
        self.menuHelp.setTitle(_translate("MainWindow", "&Help"))
        self.menuMap.setTitle(_translate("MainWindow", "&Map"))
        self.menuView.setTitle(_translate("MainWindow", "&View"))
        self.menuShowObjectNames.setTitle(_translate("MainWindow", "Show Object &Names"))
        self.mainToolBar.setWindowTitle(_translate("MainWindow", "Main Toolbar"))
        self.toolsToolBar.setWindowTitle(_translate("MainWindow", "Tools"))
        self.actionOpen.setText(_translate("MainWindow", "&Open..."))
        self.actionSave.setText(_translate("MainWindow", "&Save"))
        self.actionQuit.setText(_translate("MainWindow", "&Quit"))
        self.actionCopy.setText(_translate("MainWindow", "&Copy"))
        self.actionPaste.setText(_translate("MainWindow", "&Paste"))
        self.actionAbout.setText(_translate("MainWindow", "&About Tiled"))
        self.actionAboutQt.setText(_translate("MainWindow", "About Qt"))
        self.actionResizeMap.setText(_translate("MainWindow", "&Resize Map..."))
        self.actionMapProperties.setText(_translate("MainWindow", "Map &Properties"))
        self.actionAutoMap.setText(_translate("MainWindow", "AutoMap"))
        self.actionAutoMap.setShortcut(_translate("MainWindow", "A"))
        self.actionShowGrid.setText(_translate("MainWindow", "Show &Grid"))
        self.actionShowGrid.setShortcut(_translate("MainWindow", "Ctrl+G"))
        self.actionSaveAs.setText(_translate("MainWindow", "Save &As..."))
        self.actionNew.setText(_translate("MainWindow", "&New..."))
        self.actionNewTileset.setText(_translate("MainWindow", "New &Tileset..."))
        self.actionClose.setText(_translate("MainWindow", "&Close"))
        self.actionZoomIn.setText(_translate("MainWindow", "Zoom In"))
        self.actionZoomOut.setText(_translate("MainWindow", "Zoom Out"))
        self.actionZoomNormal.setText(_translate("MainWindow", "Normal Size"))
        self.actionZoomNormal.setShortcut(_translate("MainWindow", "Ctrl+0"))
        self.actionExportAsImage.setText(_translate("MainWindow", "Export As &Image..."))
        self.actionCut.setText(_translate("MainWindow", "Cu&t"))
        self.actionOffsetMap.setText(_translate("MainWindow", "&Offset Map..."))
        self.actionOffsetMap.setToolTip(_translate("MainWindow", "Offsets everything in a layer"))
        self.actionPreferences.setText(_translate("MainWindow", "Pre&ferences..."))
        self.actionClearRecentFiles.setText(_translate("MainWindow", "Clear Recent Files"))
        self.actionExportAs.setText(_translate("MainWindow", "E&xport As..."))
        self.actionExportAs.setShortcut(_translate("MainWindow", "Ctrl+Shift+E"))
        self.actionAddExternalTileset.setText(_translate("MainWindow", "&Add External Tileset..."))
        self.actionSnapToGrid.setText(_translate("MainWindow", "&Snap to Grid"))
        self.actionCloseAll.setText(_translate("MainWindow", "C&lose All"))
        self.actionCloseAll.setShortcut(_translate("MainWindow", "Ctrl+Shift+W"))
        self.actionDelete.setText(_translate("MainWindow", "&Delete"))
        self.actionDelete.setIconText(_translate("MainWindow", "Delete"))
        self.actionHighlightCurrentLayer.setText(_translate("MainWindow", "&Highlight Current Layer"))
        self.actionHighlightCurrentLayer.setShortcut(_translate("MainWindow", "H"))
        self.actionShowTileObjectOutlines.setText(_translate("MainWindow", "Show Tile Object &Outlines"))
        self.actionSnapToFineGrid.setText(_translate("MainWindow", "Snap to &Fine Grid"))
        self.actionShowTileAnimations.setText(_translate("MainWindow", "Show Tile Animations"))
        self.actionReload.setText(_translate("MainWindow", "Reload"))
        self.actionReload.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.actionExport.setText(_translate("MainWindow", "&Export"))
        self.actionExport.setShortcut(_translate("MainWindow", "Ctrl+E"))
        self.actionBecomePatron.setText(_translate("MainWindow", "Become a Patron"))
        self.actionSaveAll.setText(_translate("MainWindow", "Save All"))
        self.actionDocumentation.setText(_translate("MainWindow", "Documentation"))
        self.actionNoLabels.setText(_translate("MainWindow", "&Never"))
        self.actionLabelsForSelectedObjects.setText(_translate("MainWindow", "For &Selected Objects"))
        self.actionLabelsForAllObjects.setText(_translate("MainWindow", "For &All Objects"))

import tiled_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

