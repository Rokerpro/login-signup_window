import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt, QTimer
import datetime
import json
import os
class Signup_window(QWidget):
    def __init__(self):
        super().__init__()
        self.Email_sign = QLineEdit(self)
        self.password_sign = QLineEdit(self)
        self.password_sign.setEchoMode(QLineEdit.Password)
        self.Signup_button = QPushButton("Signup", self)
        self.signup_success = QLabel("", self)
        self.InitUI()
        self.valid_credentials_file = "Valid_credentials.json"
        self.email_domains = [
            "@gmail.com", "@yahoo.com", "@yahoo.co.in", "@yahoo.co.uk",
            "@outlook.com", "@hotmail.com", "@live.com", "@protonmail.com",
            "@proton.me", "@icloud.com", "@me.com", "@mac.com", "@mail.com",
            "@usa.com", "@gmx.com", "@aol.com", "@zoho.com", "@tutanota.com",
            "@tuta.io", "@yandex.com"
        ]

        # Load existing credentials
        if os.path.exists(self.valid_credentials_file):
            with open(self.valid_credentials_file, "r") as file:
                self.content = json.load(file)
        else:
            self.content = {}

    def InitUI(self):
        self.setWindowTitle("Sign Up")
        vbox = QVBoxLayout()

        vbox.addWidget(QLabel("Email:", self))
        vbox.addWidget(self.Email_sign)
        vbox.addWidget(QLabel("Password:", self))
        vbox.addWidget(self.password_sign)

        vbox.addWidget(self.Signup_button)
        vbox.addWidget(self.signup_success)

        self.setLayout(vbox)

        self.Email_sign.setAlignment(Qt.AlignLeft)
        self.password_sign.setAlignment(Qt.AlignLeft)
        self.signup_success.setAlignment(Qt.AlignCenter)

        self.Signup_button.setObjectName("Signup_button")
        self.Email_sign.setObjectName("Email_sign")
        self.password_sign.setObjectName("password_sign")
        self.signup_success.setObjectName("signup_success")

        self.setStyleSheet("""
                QWidget {
            background-color: #ADD8E6;  /* Light blue background */
        }
            QLabel, QPushButton{
                font-family: caliber;
            }
            QLabel#signup_success{
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

        self.Signup_button.clicked.connect(self.handle_signup)

    def handle_signup(self):
        email = self.Email_sign.text()
        password = self.password_sign.text()

        self.signup_success.setText("")

        valid_domain = any(email.endswith(domain) for domain in self.email_domains)
        if not valid_domain:
            self.signup_success.setText("Invalid email domain. Please use a supported provider.")
            return

        if email in self.content:
            self.signup_success.setText("Email already exists. Please use a different email.")
            return


        self.content[email] = password
        with open(self.valid_credentials_file, "w") as file:
            json.dump(self.content, file)

        self.signup_success.setText("Account Successfully Created!!!")
        self.close()