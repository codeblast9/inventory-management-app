from PySide6.QtWidgets import QApplication, QTabWidget
from ui.login_ui import LoginWindow
from ui.product_ui import ProductMaster
from ui.goods_ui import GoodsReceiving
from ui.sales_ui import SalesForm
from db_local.database import initialize_database
import sys

def show_main_app():
    tabs = QTabWidget()
    tabs.setWindowTitle("Inventory App")
    tabs.addTab(ProductMaster(), "Product Master")
    tabs.addTab(GoodsReceiving(), "Goods Receiving")
    tabs.addTab(SalesForm(), "Sales")
    tabs.resize(900, 600)
    tabs.show()
    return tabs

if __name__ == "__main__":
    initialize_database()  # ← this line initializes DB tables

    app = QApplication(sys.argv)
    login_window = LoginWindow()

    if login_window.exec() == 1:  # QDialog.Accepted
        main_window = show_main_app()
        sys.exit(app.exec())
    else:
        sys.exit()


