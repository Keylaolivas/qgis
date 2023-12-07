from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QFileInfo
from PyQt5.QtGui import *
from qgis.core import *
from qgis.gui import *

import sys

class ventana(QtWidgets.QMainWindow):
    def __init__(self):
        super(ventana, self).__init__()
        uic.loadUi( "untitled.ui", self)
        self.mapa = QgsMapCanvas()
        self.mapa.setCanvasColor(QColor(255, 255, 255))
        self.mapa.enableAntiAliasing(True)
        self.mapa.show()
        self.layout = QtWidgets.QHBoxLayout(self.frame)
        self.layout.addWidget(self.mapa)

        self.botonAgregarCapa = QtWidgets.QAction(QIcon('iconos/agregar.png'), "agregar capa", self.frame)
        self.botonAgregarCapa.triggered.connect(self.AgregarCapa)
        self.botonMover = QtWidgets.QAction(QIcon('iconos/mover.png'), "Mover", self.frame)
        self.botonMover.triggered.connect(self.Movermapa)
        self.botonAcercar = QtWidgets.QAction(QIcon('iconos/acercar.png'), "Acercar", self.frame)
        self.botonAlejar = QtWidgets.QAction(QIcon('iconos/alejar.png'), "Alejar", self.frame)

        self.barra = self.addToolBar("Mapa")
        self.barra.addAction(self.botonAgregarCapa)
        self.barra.addAction(self.botonMover)
        self.barra.addAction(self.botonAcercar)
        self.barra.addAction(self.botonAlejar)

        #crear las herramientas para el mapa
        self.herramientaMover = QgsMapToolPan(self.mapa)

        self. show()

    def Movermapa(self):
            self.mapa.setMapTool(self.herramientaMover)
    def AgregarCapa(self):
        print("Acción de agregar capa")

        ruta_capa = QtWidgets.QFileDialog.getOpenFileName(self, "Abrir archivo", ".", "*.shp")
        print(ruta_capa)
        capa_informacion = QFileInfo(ruta_capa[0])
        capa_proovedor = "ogr"
        capa = QgsVectorLayer(ruta_capa[0], capa_informacion.fileName(), capa_proovedor)
        QgsProject.instance().addMapLayer(capa)
        self.mapa.setExtent(capa.extent())
        self.mapa.setLayers([capa])
        self.mapa.show()
        self.mapa.refresh()

aplicacion = QtWidgets.QApplication(sys.argv)
ventana= ventana()
aplicacion.exec_()
