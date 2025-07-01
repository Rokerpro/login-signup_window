import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt, QTimer
import datetime
import json
import os
class Login_window(QWidget):
    def __init__(self):
        super().__init__()
        self.Email = QLineEdit(self)
        self.password = QLineEdit(self)
        self.password.setEchoMode(QLineEdit.Password)
        self.Login_button = QPushButton("Login", self)
        self.login_success = QLabel("", self)
        self.InitUI()
        self.valid_credentials_file = "Valid_credentials.json"
        self.email_domains = [
            "@gmail.com", "@yahoo.com", "@yahoo.co.in", "@yahoo.co.uk",
            "@outlook.com", "@hotmail.com", "@live.com", "@protonmail.com",
            "@proton.me", "@icloud.com", "@me.com", "@mac.com", "@mail.com",
            "@usa.com", "@gmx.com", "@aol.com", "@zoho.com", "@tutanota.com",
            "@tuta.io", "@yandex.com"
        ]
        self.attempts = 3
        if os.path.exists(self.valid_credentials_file):
            with open(self.valid_credentials_file, "r") as file:
                self.content = json.load(file)
        else:
            self.content = {}

    def InitUI(self):
        self.setWindowTitle("Login")
        vbox = QVBoxLayout()

        vbox.addWidget(QLabel("Email:", self))
        vbox.addWidget(self.Email)
        vbox.addWidget(QLabel("Password:", self))
        vbox.addWidget(self.password)
        vbox.addWidget(self.Login_button)
        vbox.addWidget(self.login_success)

        self.setLayout(vbox)

        self.Email.setAlignment(Qt.AlignLeft)
        self.password.setAlignment(Qt.AlignLeft)
        self.login_success.setAlignment(Qt.AlignCenter)

        self.Login_button.setObjectName("Login_button")
        self.Email.setObjectName("Email")
        self.password.setObjectName("password")
        self.login_success.setObjectName("login_success")
        self.setStyleSheet("""
                QWidget {
            background-color: #ADD8E6;  /* Light blue background */
        }
            QLabel, QPushButton{
                font-family: caliber;
            }
            QLabel#login_success{
                font-size: 12px;
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
            QLineEdit{
                font-size: 20px;
            }
            """)

        self.Login_button.clicked.connect(self.handle_login)

    def handle_login(self):
        email = self.Email.text()
        password = self.password.text()

        self.login_success.setText("")

        valid_domain = any(email.endswith(domain) for domain in self.email_domains)
        if not valid_domain:
            self.login_success.setText("Invalid email domain. Please use a supported provider.")
            return

        if email in self.content and self.content[email] == password:
            self.login_success.setText("Login Successfully!!!")
            self.close()
        else:
            self.attempts -= 1
            if self.attempts > 0:
                self.login_success.setText(f"Incorrect email or password. Attempts left: {self.attempts}")
            else:
                self.login_success.setText("Too many failed attempts. Please try again later.")
                self.Login_button.setEnabled(False)