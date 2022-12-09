from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem, QGraphicsScene
from ui_mainwindow import Ui_MainWindow
from PySide2.QtGui import QPen, QColor, QTransform
from PySide2.QtCore import Slot
from Particulas import Particula
from Listas import Lista
from random import randint
from Algoritmos import distanciaEuclidiana

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.lista = Lista()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.puntos_cercanos = []
        self.punto = []

        ##Ventana de texto plano y tabla
        self.ui.pushButton_2.clicked.connect(self.click_agregar)
        self.ui.pushButton.clicked.connect(self.click_final)
        self.ui.pushButton_3.clicked.connect(self.click_mostrar)
        self.ui.mostrarTabla_pushButton.clicked.connect(self.mostrarTabla)
        self.ui.buscar_pushButton.clicked.connect(self.buscarId)

        ##Abrir y guardar
        self.ui.actionAbrir.triggered.connect(self.action_abrir_archivo)
        self.ui.actionGuardar.triggered.connect(self.action_guardar_archivo)

        ##Ordenamientos
        self.ui.actionOrd_Id_Asc.triggered.connect(self.ord_id_asc)
        self.ui.actionOrd_Id_Des.triggered.connect(self.ord_id_des)
        self.ui.actionOrd_Velocidad_Asc.triggered.connect(self.ord_velocidad_asc)
        self.ui.actionOrd_Velocidad_Des.triggered.connect(self.ord_velocidad_des)
        self.ui.actionOrd_Distancia_Asc.triggered.connect(self.ord_distancia_asc)
        self.ui.actionOrd_Distancia_Des.triggered.connect(self.ord_distancia_des)

        ##Pestana grafica
        self.ui.dibujar_pushButton.clicked.connect(self.dibujar)
        self.ui.limpiar_pushButton.clicked.connect(self.limpiar)
        self.ui.dibujarPuntos_pushButton.clicked.connect(self.generar)
        self.ui.puntosCercanos_pushButton.clicked.connect(self.calcular)
        self.scene = QGraphicsScene()
        self.ui.graphicsView.setScene(self.scene)

    def wheelEvent(self, event):
        if event.delta() > 0:
            self.ui.graphicsView.scale(1.2, 1.2)
        else:
            self.ui.graphicsView.scale(0.8, 0.8)

    @Slot()
    def ord_id_asc(self):
        self.lista.ordenarId()
        self.mostrarTabla()

    @Slot()
    def generar(self):
        self.puntos = self.lista.get_puntos()
        for punto in self.puntos:
                x = punto.x
                y = punto.y

                r = punto.red
                b = punto.blue
                g = punto.green

                color = QColor(r,b,g)
                pen = QPen()
                pen.setColor(color)
                self.scene.addRect(x,y,5,5,pen)

    def conectar(self):
        for punto01, punto02 in self.puntos_cercanos:
            pen = QPen()
            color = QColor(punto01.red,punto01.green,punto01.blue)
            pen.setColor(color)
            self.scene.addLine(punto01.x+5,punto01.y+5,punto02.x+5,punto02.y+5,pen)   
            
        
    @Slot()
    def calcular(self):
        for punto01 in self.puntos:
            distMin = 1000
            punto = Lista()
            for todos in self.puntos:
                if punto01 == todos:
                    continue
                dist = distanciaEuclidiana(
                    punto01.x,punto01.y,
                    todos.x,todos.y
                )
                if dist < distMin:
                    distMin = dist
                    punto = todos
            self.puntos_cercanos.append([punto01,punto])
        self.conectar()

    @Slot()
    def ord_id_des(self):
        self.lista.ordenarIdDes()
        self.mostrarTabla()

    @Slot()
    def ord_velocidad_asc(self):
        self.lista.ordenarVelocidad()
        self.mostrarTabla()

    @Slot()
    def ord_velocidad_des(self):
        self.lista.ordenarVelocidadDes()
        self.mostrarTabla()

    @Slot()
    def ord_distancia_asc(self):
        self.lista.ordenarDistancia()
        self.mostrarTabla()

    @Slot()
    def ord_distancia_des(self):
        self.lista.ordenarDistanciaDes()
        self.mostrarTabla()

    @Slot()
    def dibujar(self):
        circleLen = 5
        pen = QPen()
        pen.setWidth(5)

        for Particula in self.lista:
            r = Particula.red
            g = Particula.green
            b = Particula.blue
            color = QColor(r, g, b)
            pen.setColor(color)

            self.scene.addEllipse(Particula.origen_x, Particula.origen_y, circleLen, circleLen, pen)
            self.scene.addEllipse(Particula.destino_x, Particula.destino_y, circleLen, circleLen, pen)
            self.scene.addLine(Particula.origen_x+(circleLen/2), Particula.origen_y+(circleLen/2),
            Particula.destino_x+(circleLen/2), Particula.destino_y+(circleLen/2), pen)


    @Slot()
    def dibujarPuntos(self):
        circleLen = 5
        pen = QPen()
        pen.setWidth(5)

        for Particula in self.lista:
            r = Particula.red
            g = Particula.green
            b = Particula.blue
            color = QColor(r, g, b)
            pen.setColor(color)

            self.scene.addEllipse(Particula.origen_x, Particula.origen_y, circleLen, circleLen, pen)
            self.scene.addEllipse(Particula.destino_x, Particula.destino_y, circleLen, circleLen, pen)
            

    @Slot()
    def limpiar(self):
        self.scene.clear()


    @Slot()
    def buscarId(self):
        idBusqueda = self.ui.buscar_lineEdit.text()
        identificado = False
        for Particula in self.lista:
            if idBusqueda == (str(Particula.id)):
                self.ui.tabla.clear()
                self.ui.tabla.setRowCount(1)

                headers = ["Id", "Origen X", "Origen Y", "Destino X", "Destino Y", "Velocidad", "Rojo", "Verde", "Azul", "Distancia"]
                self.ui.tabla.setHorizontalHeaderLabels(headers)

                id_widget = QTableWidgetItem (str(Particula.id))
                origen_x_widget = QTableWidgetItem (str(Particula.origen_x))
                origen_y_widget = QTableWidgetItem(str(Particula.origen_y))
                destino_x_widget = QTableWidgetItem(str(Particula.destino_x))
                destino_y_widget = QTableWidgetItem(str(Particula.destino_y))
                velocidad_widget = QTableWidgetItem(str(Particula.velocidad))
                red_widget = QTableWidgetItem(str(Particula.red))
                blue_widget = QTableWidgetItem(str(Particula.blue))
                green_widget = QTableWidgetItem(str(Particula.green))
                distancia_widget = QTableWidgetItem(str(Particula.distancia))
                self.ui.tabla.setItem(0,0,id_widget)
                self.ui.tabla.setItem(0,1,origen_x_widget)
                self.ui.tabla.setItem(0,2,origen_y_widget)
                self.ui.tabla.setItem(0,3,destino_x_widget)
                self.ui.tabla.setItem(0,4,destino_y_widget)
                self.ui.tabla.setItem(0,5,velocidad_widget)
                self.ui.tabla.setItem(0,6,red_widget)
                self.ui.tabla.setItem(0,7,blue_widget)
                self.ui.tabla.setItem(0,8,green_widget)
                self.ui.tabla.setItem(0,9,distancia_widget)
                identificado = True
                return 
        if not identificado:
            QMessageBox.warning(self, "Error", f'La particula con el id "{idBusqueda}" no fue encontrada')


    @Slot()
    def mostrarTabla(self):
        self.ui.tabla.clear()
        self.ui.tabla.setColumnCount(10)
        headers = ["Id", "Origen X", "Origen Y", "Destino X", "Destino Y", "Velocidad", "Rojo", "Verde", "Azul", "Distancia"]
        self.ui.tabla.setHorizontalHeaderLabels(headers)
        self.ui.tabla.setRowCount(len(self.lista))

        row = 0
        for Particula in self.lista:
            id_widget = QTableWidgetItem (str(Particula.id))
            origen_x_widget = QTableWidgetItem (str(Particula.origen_x))
            origen_y_widget = QTableWidgetItem(str(Particula.origen_y))
            destino_x_widget = QTableWidgetItem(str(Particula.destino_x))
            destino_y_widget = QTableWidgetItem(str(Particula.destino_y))
            velocidad_widget = QTableWidgetItem(str(Particula.velocidad))
            red_widget = QTableWidgetItem(str(Particula.red))
            blue_widget = QTableWidgetItem(str(Particula.blue))
            green_widget = QTableWidgetItem(str(Particula.green))
            distancia_widget = QTableWidgetItem(str(Particula.distancia))

            self.ui.tabla.setItem(row,0,id_widget)
            self.ui.tabla.setItem(row,1,origen_x_widget)
            self.ui.tabla.setItem(row,2,origen_y_widget)
            self.ui.tabla.setItem(row,3,destino_x_widget)
            self.ui.tabla.setItem(row,4,destino_y_widget)
            self.ui.tabla.setItem(row,5,velocidad_widget)
            self.ui.tabla.setItem(row,6,red_widget)
            self.ui.tabla.setItem(row,7,blue_widget)
            self.ui.tabla.setItem(row,8,green_widget)
            self.ui.tabla.setItem(row,9,distancia_widget)
            row += 1

    @Slot()
    def action_abrir_archivo(self):
        ubicacion = QFileDialog.getOpenFileName(self, 'Abrir archivo', '.', 'JSON (*.json)' )[0]
        if self.lista.abrir_archivo(ubicacion):
            self.ui.plainTextEdit.clear()
            self.ui.plainTextEdit.insertPlainText("Lista cargada\n")
            self.ui.plainTextEdit.insertPlainText(str(self.lista))
            QMessageBox.information(
                self,
                "Carga completada",
                "Se cargaron los datos contenidos en :" + ubicacion
            )
        else:
                QMessageBox.critical(
                    self,
                    "Error",
                    "Error al abrir el archivo" + ubicacion
            )

    @Slot()
    def action_guardar_archivo(self):
      ubicacion = QFileDialog.getSaveFileName(
            self,
            'Guardar',
            '.',
            'JSON (*.json)'
        )[0]
      print(ubicacion)
      if self.lista.guardar_archivo(ubicacion):
        QMessageBox.information(
            self,
            "Guardado completado",
            "Se pudo crear el archivo en la direccion : " + ubicacion,
            
        )

      else :
        QMessageBox.critical(
            self,
            "Error",
            "No se pudo crear el archivo" + ubicacion
        )

    @Slot()
    def click_mostrar(self):
        self.ui.plainTextEdit.clear()
        self.ui.plainTextEdit.insertPlainText(str(self.lista))

    @Slot()
    def click_agregar(self):
        id = self.ui.spinBox.value()
        origen_x = self.ui.spinBox_2.value()
        origen_y = self.ui.spinBox_3.value()
        destino_x = self.ui.spinBox_4.value()
        destino_y = self.ui.spinBox_5.value()
        velocidad = self.ui.spinBox_6.value()
        rojo = self.ui.spinBox_7.value()
        verde = self.ui.spinBox_8.value()
        azul = self.ui.spinBox_9.value()

        particula = Particula(id,origen_x,origen_y,destino_x,destino_y,velocidad,rojo,verde,azul)
        self.lista.insertar_inicio(particula)

    @Slot()
    def click_final(self):
        id = self.ui.spinBox.value()
        origen_x = self.ui.spinBox_2.value()
        origen_y = self.ui.spinBox_3.value()
        destino_x = self.ui.spinBox_4.value()
        destino_y = self.ui.spinBox_5.value()
        velocidad = self.ui.spinBox_6.value()
        rojo = self.ui.spinBox_7.value()
        verde = self.ui.spinBox_8.value()
        azul = self.ui.spinBox_9.value()

        particula = Particula(id,origen_x,origen_y,destino_x,destino_y,velocidad,rojo,verde,azul)
        self.lista.insertar_final(particula)