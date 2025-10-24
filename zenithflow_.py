

import sys
from cryptography.fernet import Fernet
from PyQt5 import QtWidgets, QtGui, QtCore

# --- کلید ثابت برای رمزنگاری سریع ---
APP_SECRET_KEY = Fernet.generate_key()
fernet = Fernet(APP_SECRET_KEY)

class ZenithFlow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ZENITHFLOWCRYPTOBOT")
        self.setGeometry(100, 100, 700, 500)

        try:
            self.setWindowIcon(QtGui.QIcon("photo_2025-08-21_13-07-54.jpg"))
        except:
            pass  
        self.tabs = QtWidgets.QTabWidget()
        self.setCentralWidget(self.tabs)

        # تب رمزنگاری سریع
        self.quick_tab = QtWidgets.QWidget()
        self.build_quick_tab()
        self.tabs.addTab(self.quick_tab, "🔑 رمزنگاری سریع")

    def build_quick_tab(self):
        layout = QtWidgets.QVBoxLayout()

        # ورودی متن
        self.input_text = QtWidgets.QTextEdit()
        self.input_text.setPlaceholderText("اینجا متن خود را وارد کنید...")
        layout.addWidget(QtWidgets.QLabel("متن اصلی یا رمز شده:"))
        layout.addWidget(self.input_text)

        # دکمه‌ها
        button_layout = QtWidgets.QHBoxLayout()
        self.encrypt_button = QtWidgets.QPushButton("🔒 رمزنگاری کن")
        self.decrypt_button = QtWidgets.QPushButton("🔓 رمزگشایی کن")
        self.encrypt_button.setStyleSheet("background-color:#ff9800;color:white;font-weight:bold;")
        self.decrypt_button.setStyleSheet("background-color:#4caf50;color:white;font-weight:bold;")

        self.encrypt_button.clicked.connect(self.encrypt_text)
        self.decrypt_button.clicked.connect(self.decrypt_text)

        button_layout.addWidget(self.encrypt_button)
        button_layout.addWidget(self.decrypt_button)
        layout.addLayout(button_layout)

        # خروجی
        self.output_text = QtWidgets.QTextEdit()
        self.output_text.setPlaceholderText("نتیجه اینجا نمایش داده می‌شود...")
        self.output_text.setReadOnly(True)
        layout.addWidget(QtWidgets.QLabel("نتیجه:"))
        layout.addWidget(self.output_text)

        self.quick_tab.setLayout(layout)

    def encrypt_text(self):
        text = self.input_text.toPlainText().strip()
        if not text:
            self.output_text.setPlainText("⚠️ لطفاً یک متن وارد کنید.")
            return
        encrypted = fernet.encrypt(text.encode()).decode()
        self.output_text.setPlainText(encrypted)

    def decrypt_text(self):
        text = self.input_text.toPlainText().strip()
        if not text:
            self.output_text.setPlainText("⚠️ لطفاً متن رمز شده وارد کنید.")
            return
        try:
            decrypted = fernet.decrypt(text.encode()).decode()
            self.output_text.setPlainText(decrypted)
        except Exception:
            self.output_text.setPlainText("❌ متن معتبر نیست یا با این کلید رمزنگاری نشده است.")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = ZenithFlow()
    window.show()
    sys.exit(app.exec_())
