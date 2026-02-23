def sort_products(products, by="price", reverse=False):
    """
    Sắp xếp danh sách sản phẩm.
    by: "price" hoặc "name"
    reverse: True = giảm dần, False = tăng dần
    """
    if by not in ["price", "name"]:
        print("Lựa chọn sắp xếp không hợp lệ.")
        return products
    
    return sorted(products, key=lambda x: x[by], reverse=reverse)


def sorting_menu(products):
    print("\n=== SẮP XẾP SẢN PHẨM ===")
    print("1. Theo giá tăng")
    print("2. Theo giá giảm")
    print("3. Theo tên A → Z")
    print("4. Theo tên Z → A")

    choice = input("Chọn chức năng: ")

    if choice == "1":
        return sort_products(products, "price", False)
    elif choice == "2":
        return sort_products(products, "price", True)
    elif choice == "3":
        return sort_products(products, "name", False)
    elif choice == "4":
        return sort_products(products, "name", True)
    else:
        print("Lựa chọn không hợp lệ.")
        return products