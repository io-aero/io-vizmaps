from qgis.core import *

def setup_qgis():
    QgsApplication.setPrefixPath("C:\\OSGeo4W64\\apps\\qgis", True)
    qgs = QgsApplication([], True)
    qgs.initQgis()
    verbose =1
    if(verbose):
        print('QGIS setup complete')

def show_map(window):
    window.show()
    qgs.exec_()