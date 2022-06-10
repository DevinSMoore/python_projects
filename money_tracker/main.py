
from include.include_2 import GUI
import sys
from PySide6 import QtCore,QtWidgets,QtGui

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    
    widget = GUI.my_widget()
    widget.resize(500, 300)
    widget.show()
    
    sys.exit(app.exec())
    