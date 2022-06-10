from ctypes import alignment
from PySide6 import QtCore,QtWidgets,QtGui
import sys
import random

class my_widget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        
        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Cyrilic Characters"]
        
        self.button = QtWidgets.QPushButton("Click Me!")
        self.button.height(10)
        self.button.width(30)
        self.text = QtWidgets.QLabel("Hello World", alignment=QtCore.Qt.AlignCenter)
        
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)
        self.button.clicked.connect(self.magic)
        
    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))
        
        