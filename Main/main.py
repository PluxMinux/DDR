from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic,QtWidgets
import sys, os
from sub_main import Main

upload_state = False
path_state = False

ui_path = os.path.dirname(os.path.abspath(__file__)) + "\main.ui"

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        uic.loadUi(ui_path, self)

        self.setWindowTitle("Data Duplicated Remover") 
        
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
        if (self.label_upload.text() and self.label_path_selection.text()) == '':
            print("No file")
        
        else:
            upload_path = self.label_upload.text()
            selected_path = self.label_path_selection.text()
            
            paths = Main(upload_path, selected_path)
            print(paths.dups_remover())
            

        

if __name__ == '__main__':
	App = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	sys.exit(App.exec_())




