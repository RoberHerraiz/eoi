from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


app = QApplication([])
app.setApplicationName('PyNotePad')

editor = QPlainTextEdit()

window = QMainWindow()
window.setWindowTitle('PyNotePad')
window.setCentralWidget(editor)


file_menu = window.menuBar().addMenu('&File') # Con "&" le indicamos el atajo de alt + .
file_path = None

def show_open_dialog():
    global file_path
    filename, _ = QFileDialog.getOpenFileName(window, 'Open...')
    if filename:
        file_contents = open(filename, 'r').read()
        editor.setPlainText(file_contents)
        file_path = filename

open_action = QAction('&Open file')
open_action.triggered.connect(show_open_dialog)
open_action.setShortcut(QKeySequence.Open)
file_menu.addAction(open_action)


def save():
    if file_path is None:
        show_save_dialog()
    else:
        with open(file_path, 'w') as f:
            f.write(editor.toPlainText())


def show_save_dialog():
    global file_path
    filename, _ = QFileDialog.getSaveFileName(window, 'Saving file...')
    if filename:
        file_path= filename
        save()

save_action = QAction('&Save file')
save_action.triggered.connect(save)
save_action.setShortcut(QKeySequence.Save)
file_menu.addAction(save_action)


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