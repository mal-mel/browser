from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWebEngineWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MiniBrowser")
        MainWindow.resize(842, 630)
        MainWindow.setMinimumSize(QtCore.QSize(842, 630))
        MainWindow.setMaximumSize(QtCore.QSize(842, 630))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.webView = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.webView.setGeometry(QtCore.QRect(10, 40, 821, 561))
        self.webView.setUrl(QtCore.QUrl("about:blank"))
        self.webView.setObjectName("webView")
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setGeometry(QtCore.QRect(122, 4, 89, 31))
        self.backButton.setObjectName("backButton")
        self.reloadButton = QtWidgets.QPushButton(self.centralwidget)
        self.reloadButton.setGeometry(QtCore.QRect(10, 4, 89, 31))
        self.reloadButton.setObjectName("reloadButton")
        self.urlLine = QtWidgets.QLineEdit(self.centralwidget)
        self.urlLine.setGeometry(QtCore.QRect(210, 4, 451, 31))
        self.urlLine.setObjectName("urlLine")
        self.goButton = QtWidgets.QPushButton(self.centralwidget)
        self.goButton.setGeometry(QtCore.QRect(660, 4, 71, 31))
        self.goButton.setObjectName("goButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 842, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MiniBrowser", "MiniBrowser"))
        self.backButton.setText(_translate("MiniBrowser", "Back"))
        self.reloadButton.setText(_translate("MiniBrowser", "Reload"))
        self.goButton.setText(_translate("MiniBrowser", "Go"))
