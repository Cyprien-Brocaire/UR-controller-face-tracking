import sys
from PyQt5.QtWidgets import QApplication
from mainWindow import MainWindow



app = QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()
app.exec_()
