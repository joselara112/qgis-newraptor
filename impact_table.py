from qgis.PyQt.QtWidgets import *
from .impact_table_dialog import Ui_dlgimpacts

class DlgTable(QDialog, Ui_dlgimpacts):
    def __init__(self):
        super(DlgTable, self).__init__()
        self.setupUi(self)
        self.tableimpacts.setColumnWidth(1, 275)
