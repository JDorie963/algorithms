import sys
from PyQt5.QtWidgets import QApplication
from game_page import WelcomePage

if __name__ == "__main__":
    app = QApplication(sys.argv)
    welcome_page = WelcomePage()
    welcome_page.show()
    sys.exit(app.exec_())
