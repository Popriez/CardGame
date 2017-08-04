from PySide import QtGui,QtCore
import sys


class CardGame(QtGui.QDialog):
    
    def __init__(self):
        super(CardGame, self).__init__()

        self.setStyleSheet("""QDialog{ background:rgba(255, 255, 0);  border-radius:15px;}""")
        

        self.setFixedSize(QtCore.QSize(1000,500))
        self.widget()
        self.layout()

        self.setAcceptDrops(True)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)


    def widget(self):

        self.label = QtGui.QLabel("ccccc")
        self.label2 = QtGui.QLabel("dddddddddddddddddd")
        #self.label.setFixedSize(QtCore.QSize(1000,500))
        #self.label.setStyleSheet("""QLabel{ background:rgba(255, 255, 255); color : grey; border-radius:15px;}""")
        self.s = QtGui.QPushButton("asd")
        #self.s.setStyleSheet("QPushButton{background:red;color:yellow;}")

        

    def layout(self):
        mainlayout = QtGui.QVBoxLayout()
        suplayout = QtGui.QVBoxLayout()

        dialog = QtGui.QDialog()
        dialog.setLayout(mainlayout)

        panel = QtGui.QVBoxLayout()
        panel.addWidget(dialog)
        self.setLayout(panel)

        dialog.setStyleSheet("""QDialog{ background:rgba(255, 255, 255, 20);  border-radius:15px;}""")


        mainlayout.addWidget(self.label)
        mainlayout.addWidget(self.label2)
        mainlayout.addWidget(self.s)

        mainlayout.addLayout(suplayout)

        self.label.setAlignment(QtCore.Qt.AlignCenter)

        suplayout.setAlignment(QtCore.Qt.AlignCenter)
        #self.clear.setAlignment(QtCore.Qt.AlignCenter)
        self.setLayout(mainlayout)
        self.setWindowTitle("Picture")




    def keyPressEvent(self,event):
        key = event.key()

        if key == QtCore.Qt.Key_Escape:
            window.close()




app = QtGui.QApplication(sys.argv)
window = CardGame()
window.show()
app.exec_()
