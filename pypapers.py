# -*- coding: utf-8 -*-
"""
Created on Fri FEb 10 13:45:27 2014

@author: grunert
"""
import sys
import os
from PyQt4 import QtGui, QtCore
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument

class PYPAPERS(QtGui.QWidget):
    path = ""
    def __init__(self, argpath):
        super(PYPAPERS, self).__init__()   
        self.path = argpath
        self.initUI()


    def initUI(self):
        
        QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))
        
        #self.setToolTip('Close this!')

        #lbox1 = QtGui.QListWidget(self) 
        #lbox1.resize(280,260)
        #lbox1.move (10,10)
        authorbox = QtGui.QTreeWidget(self) 
        authorbox.resize(580,260)
        authorbox.move (10,10)
        authorbox.setHeaderLabels(["Title","Author","Journal","Data_Name"])
        i = 0
        print self.path
        for dirname, dirnames, filenames in os.walk(self.path):
            for filename in filenames:
                i += 1
                if i >= 30:
                    break;
                if filename.endswith(".pdf"):
                    try:
                        #print filename
                        fp = open(dirname + "\\" + filename, 'rb')
                        parser = PDFParser(fp)
                        doc = PDFDocument(parser)
                        parser.set_document(doc)
                        try:
                            authordict = doc.info[0]["Author"]
                        except:
                            authordict = "NA"
                        try:
                            titledict = doc.info[0]["Title"]
                        except:
                            titledict = "NA"
                        try:
                            journaldict = doc.info[0]["Subject"]
                        except:
                            journaldict = "NA"
                        QtGui.QTreeWidgetItem(authorbox,[titledict,authordict,journaldict,filename])
                        fp.close
                    except:
                        QtGui.QTreeWidgetItem(authorbox,["NA","NA","NA",filename])
                
                #lbox1.addItem('%s' % filename)
        btn = QtGui.QPushButton('Close', self)
        btn.clicked.connect(QtCore.QCoreApplication.quit)
 
        btn.setToolTip('<b>Close</b>')
        btn.resize(btn.sizeHint())
        btn.move(220, 270)       
        
        self.resize(600, 300) #breite,hoehe
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
    pypapers = PYPAPERS(sys.argv[1])    
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()