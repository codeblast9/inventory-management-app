# ui/product_ui.py
from PySide6.QtWidgets import QWidget, QFormLayout, QLineEdit, QPushButton, QFileDialog
from db_local.database import create_connection

class ProductMaster(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Product Master")
        layout = QFormLayout()

        self.barcode = QLineEdit()
        self.sku_id = QLineEdit()
        self.category = QLineEdit()
        self.subcategory = QLineEdit()
        self.name = QLineEdit()
        self.description = QLineEdit()
        self.tax = QLineEdit()
        self.price = QLineEdit()
        self.unit = QLineEdit()
        self.image_path = QLineEdit()
        img_btn = QPushButton("Select Image")
        img_btn.clicked.connect(self.select_image)

        save_btn = QPushButton("Save Product")
        save_btn.clicked.connect(self.save_product)

        layout.addRow("Barcode", self.barcode)
        layout.addRow("SKU ID", self.sku_id)
        layout.addRow("Category", self.category)
        layout.addRow("Subcategory", self.subcategory)
        layout.addRow("Name", self.name)
        layout.addRow("Description", self.description)
        layout.addRow("Tax", self.tax)
        layout.addRow("Price", self.price)
        layout.addRow("Unit", self.unit)
        layout.addRow("Image Path", self.image_path)
        layout.addRow("", img_btn)
        layout.addRow("", save_btn)

        self.setLayout(layout)

    def select_image(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Image")
        self.image_path.setText(file_path)

    def save_product(self):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO products (barcode, sku_id, category, subcategory, image_path, name, description, tax, price, unit)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            self.barcode.text(), self.sku_id.text(), self.category.text(), self.subcategory.text(),
            self.image_path.text(), self.name.text(), self.description.text(),
            float(self.tax.text()), float(self.price.text()), self.unit.text()
        ))
        conn.commit()
        conn.close()
