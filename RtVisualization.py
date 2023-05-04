from PyQt5.QtWidgets import QComboBox, QDateEdit, QApplication, QWidget, QPushButton, \
    QVBoxLayout, QLabel, QLineEdit, QTabWidget, QHBoxLayout, QGridLayout, QSpacerItem, QSizePolicy, QTextBrowser, QMessageBox

from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import QDate, Qt
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Tab(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.htmlView = QTextBrowser()
        self.htmlView.setHtml("""<!DOCTYPE html>
<html lang="en">
<head>

    <meta charset="utf-8">
    <title>test</title>
    <link rel="icon" type="image/png" href="favicon.png">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

</head>
<body>

    <h1>Webpage Title</h1>
    <p>Paragraph element</p><br>
    <a href="#">A link</a>

</body>
</html>""")

        msg = QMessageBox()

        # Click
        def msgbtn(e):

            if self.searchBar.text == "Please enter a train":
                return

            msg.setText("Train: " + str(self.searchBar.text()))
            retval = msg.exec_()


        # Elements
        self.bouton = QPushButton("Vizualize")
        self.bouton.clicked.connect(msgbtn)

        self.searchBar = QLineEdit("Please enter a train")


        # Click
        def clearValue(e):
            self.searchBar.setText("")


        self.searchBar.setFixedWidth(300)
        self.searchBar.focusInEvent = clearValue

        # Visualize
        msg.setIcon(QMessageBox.Information)
        msg.setText("Please input a train to visualize")
        msg.setWindowTitle("Input required")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)



