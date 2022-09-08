import sqlalchemy

COLUMNS = {
    'customers': {
        'customer_id': sqlalchemy.types.INTEGER(),
        'customer_fname': sqlalchemy.types.String(45),
        'customer_lname': sqlalchemy.types.String(45),
        'customer_email': sqlalchemy.types.String(45),
        'customer_password': sqlalchemy.types.String(45),
        'customer_street': sqlalchemy.types.String(255),
        'customer_city': sqlalchemy.types.String(45),
        'customer_state': sqlalchemy.types.String(45),
        'customer_zipcode': sqlalchemy.types.String(45),
    },
    'departments': {
        'department_id': sqlalchemy.types.INTEGER(),
        'department_name': sqlalchemy.types.String(45),
    },
    'categories': {
        'category_id': sqlalchemy.types.INTEGER(),
        'category_department_id': sqlalchemy.types.INTEGER(),
        'category_name': sqlalchemy.types.String(45),
    },
    'products': {
        'product_id': sqlalchemy.types.INTEGER(),
        'product_category_id': sqlalchemy.types.INTEGER(),
        'product_name': sqlalchemy.types.String(45),
        'product_description': sqlalchemy.types.String(255),
        'product_price': sqlalchemy.types.Numeric(),
        'product_image': sqlalchemy.types.String(255),
    },
    'orders': {
        'order_id': sqlalchemy.types.INTEGER(),
        'order_date': sqlalchemy.types.DateTime(),
        'order_customer_id': sqlalchemy.types.INTEGER(),
        'order_status': sqlalchemy.types.String(45),
    },
    'order_items': {
        'order_item_id': sqlalchemy.types.INTEGER(),
        'order_item_order_id': sqlalchemy.types.INTEGER(),
        'order_item_product_id': sqlalchemy.types.INTEGER(),
        'order_item_quantity': sqlalchemy.types.INTEGER(),
        'order_item_subtotal': sqlalchemy.types.Numeric(),
        'order_item_product_price': sqlalchemy.types.Numeric(),
    }

}
