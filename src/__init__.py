from PyQt5.QtWidgets import QApplication

from .Templates.Login.Login_Screen import Login_Page
from .Templates.Welcome import Welcome_Interface

from .setup import Setup

import sys

def main(): 
    app = QApplication(sys.argv)
    setup = Setup()

    if setup.check(setup.root+"\\cache\\.cache"):
        pass
    else: 
        welcome_page = Welcome_Interface()
        setup.cache()

    login_page = Login_Page()

    sys.exit(app.exec_())