import sys

from PyQt5 import QtWidgets
from PyQt5 import sip
from mainViewCode.Main_View import ToolMainWindow

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = ToolMainWindow()
    ui.show()
    sys.exit(app.exec_())
