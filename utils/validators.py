def is_empty(value: str) -> bool:
    return not value.strip()

def is_float(value: str) -> bool:
    try:
        float(value)
        return True
    except ValueError:
        return False

def is_positive(value: str) -> bool:
    try:
        return float(value) > 0
    except ValueError:
        return False

def validate_goods_input(data: dict) -> tuple[bool, str]:
    if is_empty(data.get('supplier', '')):
        return False, "Supplier name is required."
    if not is_float(data.get('quantity', '')):
        return False, "Quantity must be a number."
    if not is_positive(data.get('quantity', '')):
        return False, "Quantity must be greater than 0."
    if is_empty(data.get('unit', '')):
        return False, "Unit of measurement is required."
    if not is_float(data.get('rate', '')):
        return False, "Rate must be a number."
    if not is_positive(data.get('rate', '')):
        return False, "Rate must be greater than 0."
    if not is_float(data.get('tax', '')):
        return False, "Tax must be a number."
    return True, ""

def validate_sales_input(data: dict) -> tuple[bool, str]:
    if is_empty(data.get('customer', '')):
        return False, "Customer name is required."
    if not is_float(data.get('quantity', '')):
        return False, "Quantity must be a number."
    if not is_positive(data.get('quantity', '')):
        return False, "Quantity must be greater than 0."
    if is_empty(data.get('unit', '')):
        return False, "Unit of measurement is required."
    if not is_float(data.get('rate', '')):
        return False, "Rate must be a number."
    if not is_positive(data.get('rate', '')):
        return False, "Rate must be greater than 0."
    if not is_float(data.get('tax', '')):
        return False, "Tax must be a number."
    return True, ""

def validate_product_input(data: dict) -> tuple[bool, str]:
    if is_empty(data.get('barcode', '')):
        return False, "Barcode is required."
    if is_empty(data.get('sku_id', '')):
        return False, "SKU ID is required."
    if is_empty(data.get('category', '')):
        return False, "Category is required."
    if is_empty(data.get('subcategory', '')):
        return False, "Subcategory is required."
    if is_empty(data.get('name', '')):
        return False, "Product name is required."
    if is_empty(data.get('description', '')):
        return False, "Product description is required."
    if not is_float(data.get('tax', '')):
        return False, "Tax must be a number."
    if not is_float(data.get('price', '')):
        return False, "Price must be a number."
    if not is_positive(data.get('price', '')):
        return False, "Price must be greater than 0."
    if is_empty(data.get('unit', '')):
        return False, "Default unit of measurement is required."
    return True, ""
