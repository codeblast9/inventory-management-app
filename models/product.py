import sqlite3

def insert_product(conn, data: dict):
    """
    Inserts a new product into the ProductMaster table.
    """
    query = """
    INSERT INTO ProductMaster (
        barcode,
        sku_id,
        category,
        subcategory,
        name,
        description,
        tax,
        price,
        unit,
        image_path
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
    values = (
        data['barcode'],
        data['sku_id'],
        data['category'],
        data['subcategory'],
        data['name'],
        data['description'],
        float(data['tax']),
        float(data['price']),
        data['unit'],
        data['image_path']
    )
    cursor = conn.cursor()
    cursor.execute(query, values)
    conn.commit()

def get_all_products(conn):
    """
    Returns all products from the ProductMaster table.
    """
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ProductMaster ORDER BY id DESC")
    return cursor.fetchall()

def get_product_by_barcode(conn, barcode: str):
    """
    Fetches a single product by its barcode.
    """
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ProductMaster WHERE barcode = ?", (barcode,))
    return cursor.fetchone()

def delete_product_by_id(conn, product_id: int):
    """
    Deletes a product by ID.
    """
    cursor = conn.cursor()
    cursor.execute("DELETE FROM ProductMaster WHERE id = ?", (product_id,))
    conn.commit()
