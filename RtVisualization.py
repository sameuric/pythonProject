from PyQt5.QtWidgets import QComboBox, QDateEdit, QApplication, QWidget, QPushButton, \
    QVBoxLayout, QLabel, QLineEdit, QTabWidget, QHBoxLayout, QGridLayout, QSpacerItem, QSizePolicy, QTextBrowser

from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import QDate, Qt


class Tab(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.htmlView = QTextBrowser()
        self.htmlView.setHtml("""<!DOCTYPE html>
<html lang="en">
<head>

    <meta charset="utf-8">
    <title>Map</title>
    <link rel="stylesheet" href="css/index.css">
    <link rel="stylesheet" href="css/table.css">
    <link rel="icon" type="image/png" href="favicon.png">

    <meta name="viewport" content="width=device-width, initial-scale=1.0">

</head>
<body>

    <h1>My Webpage Title</h1>

    <div>
        My webpage content<br>
        <a href="#">My webpage link</a>
    </div>

</body>
</html>""")

        # Elements
        self.bouton = QPushButton("Search")
