from PyQt5.QtWidgets import QComboBox, QDateEdit, QApplication, QWidget, QPushButton, \
    QVBoxLayout, QLabel, QLineEdit, QTabWidget, QHBoxLayout, QGridLayout, QSpacerItem, QSizePolicy

from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import QDate, Qt


class Tab(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        # Elements
        self.bouton = QPushButton("Search")
