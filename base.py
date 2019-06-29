import os

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QUrl
import sys
import re

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QFileDialog, QAction

from window import Ui_MainWindow


class Browser(QtWidgets.QMainWindow):
    def __init__(self):
        super(Browser, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.url = self.make_true_url('http://127.0.0.1:5000')
        self.ui.webView.load(self.url)

        self.ui.reloadButton.clicked.connect(self.ui.webView.reload)
        self.ui.backButton.clicked.connect(self.ui.webView.back)
        self.ui.goButton.clicked.connect(self.go_to_page)
        self.ui.urlLine.setText(re.findall("('.+')", str(self.ui.webView.url()))[0][1:-1])

        self.ui.webView.urlChanged.connect(self.update_urlbar)
        self.ui.webView.titleChanged.connect(self.update_title)

    @staticmethod
    def make_true_url(url):
        return QUrl(url) if QUrl(url).scheme() else QUrl('http://' + url)

    def go_to_page(self):
        self.url = self.make_true_url(self.ui.urlLine.text())
        self.ui.webView.load(self.url)

    def update_urlbar(self):
        self.ui.urlLine.setText(re.findall("('.+')", str(self.ui.webView.url()))[0][1:-1])

    def update_title(self):
        title = self.ui.webView.page().title()
        self.setWindowTitle(f'{title} - MiniBrowser')


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = Browser()
    application.show()
    sys.exit(app.exec())
