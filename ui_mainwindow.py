# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(554, 503)
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionGuardar = QAction(MainWindow)
        self.actionGuardar.setObjectName(u"actionGuardar")
        self.actionOrd_Id_Asc = QAction(MainWindow)
        self.actionOrd_Id_Asc.setObjectName(u"actionOrd_Id_Asc")
        self.actionOrd_Id_Des = QAction(MainWindow)
        self.actionOrd_Id_Des.setObjectName(u"actionOrd_Id_Des")
        self.actionOrd_Distancia_Asc = QAction(MainWindow)
        self.actionOrd_Distancia_Asc.setObjectName(u"actionOrd_Distancia_Asc")
        self.actionOrd_Distancia_Des = QAction(MainWindow)
        self.actionOrd_Distancia_Des.setObjectName(u"actionOrd_Distancia_Des")
        self.actionOrd_Velocidad_Asc = QAction(MainWindow)
        self.actionOrd_Velocidad_Asc.setObjectName(u"actionOrd_Velocidad_Asc")
        self.actionOrd_Velocidad_Des = QAction(MainWindow)
        self.actionOrd_Velocidad_Des.setObjectName(u"actionOrd_Velocidad_Des")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.Graficas = QTabWidget(self.centralwidget)
        self.Graficas.setObjectName(u"Graficas")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_3 = QGridLayout(self.tab)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.pushButton_3 = QPushButton(self.tab)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout_3.addWidget(self.pushButton_3, 2, 0, 1, 1)

        self.plainTextEdit = QPlainTextEdit(self.tab)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.gridLayout_3.addWidget(self.plainTextEdit, 0, 2, 3, 1)

        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_4 = QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)

        self.spinBox = QSpinBox(self.groupBox)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMaximum(200)

        self.gridLayout_4.addWidget(self.spinBox, 0, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_4.addWidget(self.label_2, 1, 0, 1, 1)

        self.spinBox_2 = QSpinBox(self.groupBox)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setMaximum(200)

        self.gridLayout_4.addWidget(self.spinBox_2, 1, 1, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_4.addWidget(self.label_3, 2, 0, 1, 1)

        self.spinBox_3 = QSpinBox(self.groupBox)
        self.spinBox_3.setObjectName(u"spinBox_3")
        self.spinBox_3.setMaximum(200)

        self.gridLayout_4.addWidget(self.spinBox_3, 2, 1, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_4.addWidget(self.label_4, 3, 0, 1, 1)

        self.spinBox_4 = QSpinBox(self.groupBox)
        self.spinBox_4.setObjectName(u"spinBox_4")
        self.spinBox_4.setMaximum(200)

        self.gridLayout_4.addWidget(self.spinBox_4, 3, 1, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_4.addWidget(self.label_5, 4, 0, 1, 1)

        self.spinBox_5 = QSpinBox(self.groupBox)
        self.spinBox_5.setObjectName(u"spinBox_5")
        self.spinBox_5.setMaximum(200)

        self.gridLayout_4.addWidget(self.spinBox_5, 4, 1, 1, 1)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_4.addWidget(self.label_6, 5, 0, 1, 1)

        self.spinBox_6 = QSpinBox(self.groupBox)
        self.spinBox_6.setObjectName(u"spinBox_6")

        self.gridLayout_4.addWidget(self.spinBox_6, 5, 1, 1, 1)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_4.addWidget(self.label_7, 6, 0, 1, 1)

        self.spinBox_7 = QSpinBox(self.groupBox)
        self.spinBox_7.setObjectName(u"spinBox_7")
        self.spinBox_7.setMaximum(255)

        self.gridLayout_4.addWidget(self.spinBox_7, 6, 1, 1, 1)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_4.addWidget(self.label_8, 7, 0, 1, 1)

        self.spinBox_8 = QSpinBox(self.groupBox)
        self.spinBox_8.setObjectName(u"spinBox_8")
        self.spinBox_8.setMaximum(255)

        self.gridLayout_4.addWidget(self.spinBox_8, 7, 1, 1, 1)

        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_4.addWidget(self.label_9, 8, 0, 1, 1)

        self.spinBox_9 = QSpinBox(self.groupBox)
        self.spinBox_9.setObjectName(u"spinBox_9")
        self.spinBox_9.setMaximum(255)

        self.gridLayout_4.addWidget(self.spinBox_9, 8, 1, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 2)

        self.pushButton = QPushButton(self.tab)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_3.addWidget(self.pushButton, 1, 1, 1, 1)

        self.pushButton_2 = QPushButton(self.tab)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout_3.addWidget(self.pushButton_2, 1, 0, 1, 1)

        self.Graficas.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout = QGridLayout(self.tab_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabla = QTableWidget(self.tab_2)
        self.tabla.setObjectName(u"tabla")

        self.gridLayout.addWidget(self.tabla, 0, 0, 1, 3)

        self.buscar_lineEdit = QLineEdit(self.tab_2)
        self.buscar_lineEdit.setObjectName(u"buscar_lineEdit")

        self.gridLayout.addWidget(self.buscar_lineEdit, 1, 0, 1, 1)

        self.buscar_pushButton = QPushButton(self.tab_2)
        self.buscar_pushButton.setObjectName(u"buscar_pushButton")

        self.gridLayout.addWidget(self.buscar_pushButton, 1, 1, 1, 1)

        self.mostrarTabla_pushButton = QPushButton(self.tab_2)
        self.mostrarTabla_pushButton.setObjectName(u"mostrarTabla_pushButton")

        self.gridLayout.addWidget(self.mostrarTabla_pushButton, 1, 2, 1, 1)

        self.Graficas.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_5 = QGridLayout(self.tab_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.graphicsView = QGraphicsView(self.tab_3)
        self.graphicsView.setObjectName(u"graphicsView")

        self.gridLayout_5.addWidget(self.graphicsView, 0, 0, 1, 2)

        self.dibujar_pushButton = QPushButton(self.tab_3)
        self.dibujar_pushButton.setObjectName(u"dibujar_pushButton")

        self.gridLayout_5.addWidget(self.dibujar_pushButton, 2, 0, 1, 1)

        self.limpiar_pushButton = QPushButton(self.tab_3)
        self.limpiar_pushButton.setObjectName(u"limpiar_pushButton")

        self.gridLayout_5.addWidget(self.limpiar_pushButton, 2, 1, 1, 1)

        self.dibujarPuntos_pushButton = QPushButton(self.tab_3)
        self.dibujarPuntos_pushButton.setObjectName(u"dibujarPuntos_pushButton")

        self.gridLayout_5.addWidget(self.dibujarPuntos_pushButton, 1, 0, 1, 1)

        self.puntosCercanos_pushButton = QPushButton(self.tab_3)
        self.puntosCercanos_pushButton.setObjectName(u"puntosCercanos_pushButton")

        self.gridLayout_5.addWidget(self.puntosCercanos_pushButton, 1, 1, 1, 1)

        self.Graficas.addTab(self.tab_3, "")

        self.gridLayout_2.addWidget(self.Graficas, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 554, 22))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        self.actionOrdenar = QMenu(self.menubar)
        self.actionOrdenar.setObjectName(u"actionOrdenar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.actionOrdenar.menuAction())
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addAction(self.actionGuardar)
        self.actionOrdenar.addAction(self.actionOrd_Id_Asc)
        self.actionOrdenar.addAction(self.actionOrd_Id_Des)
        self.actionOrdenar.addAction(self.actionOrd_Distancia_Asc)
        self.actionOrdenar.addAction(self.actionOrd_Distancia_Des)
        self.actionOrdenar.addAction(self.actionOrd_Velocidad_Asc)
        self.actionOrdenar.addAction(self.actionOrd_Velocidad_Des)

        self.retranslateUi(MainWindow)

        self.Graficas.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
#if QT_CONFIG(shortcut)
        self.actionAbrir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
#if QT_CONFIG(shortcut)
        self.actionGuardar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionOrd_Id_Asc.setText(QCoreApplication.translate("MainWindow", u"ID (ascendente)", None))
        self.actionOrd_Id_Des.setText(QCoreApplication.translate("MainWindow", u"ID (descendente)", None))
        self.actionOrd_Distancia_Asc.setText(QCoreApplication.translate("MainWindow", u"Distancia (ascendente)", None))
        self.actionOrd_Distancia_Des.setText(QCoreApplication.translate("MainWindow", u"Distancia (descendente)", None))
        self.actionOrd_Velocidad_Asc.setText(QCoreApplication.translate("MainWindow", u"Velocidad (ascendente)", None))
        self.actionOrd_Velocidad_Des.setText(QCoreApplication.translate("MainWindow", u"Velocidad (descendente)", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Imprimir", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Editor de particulas", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"ID:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Origen X", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Origen Y", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Destino X", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Destino Y", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Velocidad", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Rojo", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Verde", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Azul", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Insertar al final", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Insertar al Inicio", None))
        self.Graficas.setTabText(self.Graficas.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.buscar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.mostrarTabla_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.Graficas.setTabText(self.Graficas.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tabla", None))
        self.dibujar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Dibujar todo", None))
        self.limpiar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.dibujarPuntos_pushButton.setText(QCoreApplication.translate("MainWindow", u"Dibujar solo puntos", None))
        self.puntosCercanos_pushButton.setText(QCoreApplication.translate("MainWindow", u"Puntos mas cercanos", None))
        self.Graficas.setTabText(self.Graficas.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Graficas", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
        self.actionOrdenar.setTitle(QCoreApplication.translate("MainWindow", u"Ordenar", None))
    # retranslateUi

