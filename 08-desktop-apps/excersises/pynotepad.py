from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


app = QApplication([])
app.setApplicationName('PyNotePad')

editor = QPlainTextEdit()

window = QMainWindow()
window.setWindowTitle('PyNotePad')
window.setCentralWidget(editor)


file_menu = window.menuBar().addMenu('&File') # Con "&" le indicamos el atajo de alt + .

def show_open_dialog():
    filename, _ = QFileDialog.getOpenFileName(window, 'Open...')
    if filename:
        file_contents = open(filename, 'r').read()
        editor.setPlainText(file_contents)

open_action = QAction('&Open file')
open_action.triggered.connect(show_open_dialog)
open_action.setShortcut(QKeySequence.Open)
file_menu.addAction(open_action)


# WIP fast saving function

def show_save_dialog():
    filename = QFile.fileName()
    if filename:
        with Open(filename, 'w') as f:
            f.write(editor.toPlainText())

save_action = QAction('&Save')
save_action.triggered.connect(show_save_dialog)
save_action.setShortcut(QKeySequence.Save)
file_menu.addAction(save_action)

# https://doc.qt.io/qt-5/qsavefile.html



def show_save_as_dialog():
    filename, _ = QFileDialog.getSaveFileName(window, 'Saving file...')
    with open(filename, 'w') as f:
        f.write(editor.toPlainText())

save_as_action = QAction('&Save file')
save_as_action.triggered.connect(show_save_as_dialog)
save_as_action.setShortcut(QKeySequence.SaveAs)
file_menu.addAction(save_as_action)


close_action = QAction("&Close")
close_action.triggered.connect(window.close) #signal
file_menu.addAction(close_action) # asignamos a slot


def show_about_dialog():
    text = """
        <center>
        <h1>PyNotePad</h1>
        </br>
        <img src="logo.png" width=200 height=200>
        </center>
        <p>Versión 0.0.1</p>
    """
    QMessageBox.about(window, 'About PyNotePad', text) # Padre, título y contenido

help_menu = window.menuBar().addMenu('&Help')
about_action = QAction('&About')
about_action.triggered.connect(show_about_dialog)
help_menu.addAction(about_action)



window.resize(500, 600)
window.show()
app.exec()