from db_local.database import create_connection

def print_all_records():
    conn = create_connection()
    cur = conn.cursor()

    # Fetch and print products
    cur.execute("SELECT * FROM products")
    products = cur.fetchall()
    print("Products:")
    for product in products:
        print(product)

    # Fetch and print goods receiving
    cur.execute("SELECT * FROM goods_receiving")
    goods = cur.fetchall()
    print("\nGoods Receiving:")
    for item in goods:
        print(item)

    # Fetch and print sales
    cur.execute("SELECT * FROM sales")
    sales = cur.fetchall()
    print("\nSales:")
    for sale in sales:
        print(sale)

    conn.close()

if __name__ == "__main__":
    print_all_records()
