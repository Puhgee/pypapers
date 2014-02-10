# -*- coding: utf-8 -*-
"""
Created on Fri FEb 10 13:45:27 2014

@author: grunert
"""
import sys
from PyQt4 import QtGui, QtCore

class PYPAPERS(QtGui.QWidget):
    def __init__(self):
        super(PYPAPERS, self).__init__()        
        self.initUI()

    def initUI(self):
        
        QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))
        
        self.setToolTip('Close this!')
        
        btn = QtGui.QPushButton('Close', self)
        btn.clicked.connect(QtCore.QCoreApplication.quit)
 
        btn.setToolTip('This is a <b>Button</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)       
        
        self.resize(300, 200) #position,groesse
        self.center()
        self.setWindowTitle('pypapers')    
        
        self.show() 
        
    def center(self):        
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def closeEvent(self, event):        
        reply = QtGui.QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QtGui.QMessageBox.Yes | 
            QtGui.QMessageBox.No, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()          
        
def main():  
    app = QtGui.QApplication(sys.argv)
    pypapers = PYPAPERS()    
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()