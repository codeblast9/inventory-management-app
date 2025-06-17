from PySide6.QtWidgets import QDialog, QFormLayout, QLineEdit, QPushButton, QMessageBox
from db_local.database import create_connection

class LoginWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        layout = QFormLayout()

        self.username_input = QLineEdit()
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)

        login_btn = QPushButton("Login")
        login_btn.clicked.connect(self.check_login)

        layout.addRow("Username:", self.username_input)
        layout.addRow("Password:", self.password_input)
        layout.addWidget(login_btn)

        self.setLayout(layout)

    def check_login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        conn = create_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        user = cur.fetchone()
        conn.close()

        if user:
            self.accept()  # Login success
        else:
            QMessageBox.warning(self, "Error", "Invalid username or password.")
