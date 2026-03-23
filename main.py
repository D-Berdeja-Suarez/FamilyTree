import sys
from PySide6.QtWidgets import QApplication
from basics import WelcomeScreen


########################################################### Ignore #####################################################
def welcome( ):

    application = QApplication(sys.argv)

    welcome_screen = WelcomeScreen()

    welcome_screen.show()

    sys.exit(application.exec_())

########################################################### Execute by running the following ###########################

if __name__ == "__main__":

    welcome()