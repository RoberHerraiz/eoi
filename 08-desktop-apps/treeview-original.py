from os.path import expanduser
from PyQt5.QtWidgets import *

home = expanduser('.')

app = QApplication([])
model = QDirModel()
view  = QListView()
view.setModel(model)
view.setRootIndex(model.index(home))
view.show()
app.exec()


