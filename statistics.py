def inventory_summary(products):
    print("\n=== THỐNG KÊ SẢN PHẨM ===")

    total_products = len(products)
    total_value = sum(p["price"] * p["quantity"] for p in products)
    low_stock = [p for p in products if p["quantity"] < 5]

    print(f"Tổng số sản phẩm: {total_products}")
    print(f"Tổng giá trị tồn kho: {total_value} VND")

    print("\nSản phẩm gần hết hàng (số lượng < 5):")
    if low_stock:
        for p in low_stock:
            print(f"- {p['name']} | SL: {p['quantity']}")
    else:
        print("Không có sản phẩm nào gần hết hàng.")

    print("===========================")