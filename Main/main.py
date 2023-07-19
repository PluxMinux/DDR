from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5.QtGui import QIntValidator
from PyQt5 import uic, QtWidgets
from PyQt5.QtCore import Qt
from sub_main import Main
import sys, os, time

upload_state = False
path_state = False

ui_path = os.path.dirname(os.path.abspath(__file__)) + "\main.ui"

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        uic.loadUi(ui_path, self)

        self.setWindowTitle("Data Duplicated Remover") 
        
        
        self.le_unique.setValidator(QIntValidator())
        self.btn_upload.clicked.connect(self.getFile)
        self.btn_path_selection.clicked.connect(self.getDir)
        self.btn_ok.clicked.connect(self.clicked_ok)
        
        
        
        self.show()


    def getFile(self):
        global upload_state
        if upload_state == False:
            fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', 'c:\\',"CSV (*.csv)")
            self.label_upload.setText(str(fname[0]))


    def getDir(self):
        global path_state
        if path_state == False:
            fname = QtWidgets.QFileDialog.getSaveFileName(self, "Save File",'', "CSV Files(*.csv)")
            self.label_path_selection.setText(str(fname[0]))

        

    def clicked_ok(self):
        if(self.label_upload.text() and self.label_path_selection.text()) == '':
            message = "Please select the CSV file or path to be saved."
            self.message_handling(message)
            
        elif(self.le_unique.text() == "" or self.le_unique.text() == "0"):
            message = "Please enter a column number for unique data."
            self.message_handling(message)
        
        else:
            upload_path = self.label_upload.text()
            selected_path = self.label_path_selection.text()
            
            QApplication.setOverrideCursor(Qt.WaitCursor)
            time.sleep(2)
            paths = Main(upload_path, selected_path, self.le_unique.text())
            paths.dups_remover()
            QApplication.restoreOverrideCursor()
            
            msg_title = "Program Messege"
            msg_text = "Successfully removed duplicated data."
            msg = QMessageBox.information(self, msg_title, msg_text, QMessageBox.Ok)
            
            if msg == QMessageBox.Ok:
                self.le_unique.setText("")
                self.label_upload.setText("")
                self.label_path_selection.setText("")


    def message_handling(self, text):
        self.messagebox = QMessageBox()
        self.messagebox.setText(text)
        self.messagebox.setWindowTitle("Program Message")
        self.messagebox.setIcon(QMessageBox.Information)
        self.messagebox.show()
            


        

if __name__ == '__main__':
	App = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	sys.exit(App.exec_())




