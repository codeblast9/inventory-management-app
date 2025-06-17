# ui/goods_ui.py
from PySide6.QtWidgets import QWidget, QFormLayout, QLineEdit, QPushButton, QComboBox, QMessageBox
from db_local.database import create_connection

class GoodsReceiving(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Goods Receiving")

        layout = QFormLayout()

        self.product_dropdown = QComboBox()
        self.load_products()

        self.supplier_input = QLineEdit()
        self.quantity_input = QLineEdit()
        self.unit_input = QLineEdit()
        self.rate_input = QLineEdit()
        self.total_input = QLineEdit()
        self.tax_input = QLineEdit()

        self.rate_input.textChanged.connect(self.calculate_total)
        self.quantity_input.textChanged.connect(self.calculate_total)

        save_btn = QPushButton("Save")
        save_btn.clicked.connect(self.save_goods_receiving)

        layout.addRow("Product", self.product_dropdown)
        layout.addRow("Supplier", self.supplier_input)
        layout.addRow("Quantity", self.quantity_input)
        layout.addRow("Unit", self.unit_input)
        layout.addRow("Rate/Unit", self.rate_input)
        layout.addRow("Total Rate", self.total_input)
        layout.addRow("Tax", self.tax_input)
        layout.addRow("", save_btn)

        self.setLayout(layout)

    def load_products(self):
        conn = create_connection()
        cur = conn.cursor()
        cur.execute("SELECT id, name FROM products")
        self.products = cur.fetchall()
        self.product_dropdown.clear()
        for pid, name in self.products:
            self.product_dropdown.addItem(name, pid)
        conn.close()

    def calculate_total(self):
        try:
            quantity = float(self.quantity_input.text())
            rate = float(self.rate_input.text())
            self.total_input.setText(str(quantity * rate))
        except:
            self.total_input.setText("")

    def save_goods_receiving(self):
        try:
            conn = create_connection()
            cur = conn.cursor()
            product_id = self.product_dropdown.currentData()
            cur.execute('''
                INSERT INTO goods_receiving (product_id, supplier, quantity, unit, rate, total_rate, tax)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (
                product_id,
                self.supplier_input.text(),
                float(self.quantity_input.text()),
                self.unit_input.text(),
                float(self.rate_input.text()),
                float(self.total_input.text()),
                float(self.tax_input.text())
            ))
            conn.commit()
            conn.close()
            QMessageBox.information(self, "Success", "Goods received successfully.")
            self.clear_fields()
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def clear_fields(self):
        self.supplier_input.clear()
        self.quantity_input.clear()
        self.unit_input.clear()
        self.rate_input.clear()
        self.total_input.clear()
        self.tax_input.clear()
