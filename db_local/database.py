import sqlite3
import os

# Correct way to get the path of the database relative to this file
DB_PATH = os.path.join(os.path.dirname(__file__), '../inventory.db')

def create_connection():
    conn = sqlite3.connect(DB_PATH)
    return conn

def initialize_database():
    conn = create_connection()
    cursor = conn.cursor()

    # USERS table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT
        )
    """)

    # PRODUCTS table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            description TEXT,
            category TEXT,
            subcategory TEXT,
            barcode TEXT,
            sku TEXT,
            price REAL,
            tax REAL,
            default_unit TEXT
        )
    """)

    # GOODS RECEIVING table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS goods_receiving (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_id INTEGER,
            supplier TEXT,
            quantity REAL,
            unit TEXT,
            rate REAL,
            total_rate REAL,
            tax REAL,
            FOREIGN KEY (product_id) REFERENCES products(id)
        )
    """)

    # SALES table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sales (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_id INTEGER,
            customer TEXT,
            quantity REAL,
            unit TEXT,
            rate REAL,
            total_rate REAL,
            tax REAL,
            FOREIGN KEY (product_id) REFERENCES products(id)
        )
    """)

    # Optional: insert sa
print("DB Path:", DB_PATH)