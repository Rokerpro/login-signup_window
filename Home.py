import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt, QTimer
import datetime
import json
import os

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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    home = Home()
    home.show()
    sys.exit(app.exec_())
