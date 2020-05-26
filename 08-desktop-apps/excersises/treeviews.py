import csv

from os.path import expanduser
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QAbstractTableModel, QVariant

headers = []
rows = []
with open('data.csv', 'r') as csvfile:
    data = list(csv.reader(csvfile, delimiter=','))
    headers = data[0]
    rows = data[1:]

class MyTableModel(QAbstractTableModel):

    def rowCount(self, parent):
        return len(rows)

    def columnCount(self, parent):
        return len(headers)
    
    def data(self, index, role):
        if role != Qt.DisplayRole:
            return QVariant()
        return rows[index.row()][index.column()]

    def headerData(self, section, orientation, role):
        if role != Qt.DisplayRole or orientation!= Qt.Horizontal:
            return QVariant()        
        return headers[section]

def on_cell_clicked(index):
    print(index.data())


app = QApplication([])
model = MyTableModel()

view = QTableView()
view.setModel(model)
view.doubleClicked.connect(on_cell_clicked)

view.show()
app.exec()