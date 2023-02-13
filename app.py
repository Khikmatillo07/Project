from windows.window import MyWindow,QApplication
import sys

if __name__=="__main__":
    app = QApplication(sys.argv)
    win= MyWindow(600,600,"My projet")
    win.show()
    app.exec()
