import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt, QTimer
import datetime
import json
import os
from login_win import *
from signup_win import *

class Home(QWidget):
    def __init__(self):
        super().__init__()
        self.login_window = None
        self.signup_window = None
        self.welcome = QLabel("Welcome", self)
        self.time = QLabel("", self)
        self.Login_button = QPushButton("Login", self)
        self.Sign_up_button = QPushButton("Signup", self)
        self.InitUI()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

    def InitUI(self):
        self.setWindowTitle("Home")

        vbox = QVBoxLayout()

        vbox.addWidget(self.welcome)
        vbox.addWidget(self.time)
        vbox.addWidget(self.Login_button)
        vbox.addWidget(self.Sign_up_button)

        self.setLayout(vbox)

        self.welcome.setAlignment(Qt.AlignCenter)
        self.time.setAlignment(Qt.AlignLeft)
        self.Login_button.setStyleSheet("text-align: center;")
        self.Sign_up_button.setStyleSheet("text-align: center;")

        self.welcome.setObjectName("welcome")
        self.time.setObjectName("time")
        self.Login_button.setObjectName("Login")
        self.Sign_up_button.setObjectName("Signup")

        self.setStyleSheet("""
                QWidget {
            background-color: #ADD8E6;  /* Light blue background */
        }
            QLabel, QPushButton{
                font-family: caliber;
            }
            QLabel#welcome{
                font-size: 40px;
                font-style: italic;
            }
            QPushButton{
                    font-size: 40px;
                    font-family: Arial;
                    padding: 15px 75px;             
                    margin: 20px;
                    border: 3px solid;
                    border-radius: 15px;
             }
            QLabel#time{
            font-size: 20px;
            }
            """)

        self.Login_button.clicked.connect(self.open_login_window)
        self.Sign_up_button.clicked.connect(self.open_signup_window)

    def open_login_window(self):
        self.close()
        self.login_window = Login_window()
        self.login_window.show()

    def open_signup_window(self):
        self.close()
        self.signup_window = Signup_window()
        self.signup_window.show()

    def update_time(self):
        current_time = datetime.datetime.now().strftime("%I:%M:%S %p")
        self.time.setText(current_time)






if __name__ == '__main__':
    app = QApplication(sys.argv)
    home = Home()
    home.show()
    sys.exit(app.exec_())
