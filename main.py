import product_manager as pm 

def main():
    products = pm.load_data() 
    
    while True:
        print("\n--- QUẢN LÝ CỬA HÀNG POLY-LAP ---")
        print("1. Thêm sản phẩm")
        print("2. Cập nhật sản phẩm")
        print("3. Xóa sản phẩm")
        print("4. Tìm kiếm sản phẩm")
        print("5. Hiển thị tất cả sản phẩm")
        print("6. Thoát")
        
        choice = input("Nhập lựa chọn của bạn (1-6): ")
        
        if choice == '1':
            products = pm.add_product(products)
        elif choice == '2':
            pm.update_product(products)
        elif choice == '3':
            pm.delete_product(products)
        elif choice == '4':
            pm.search_product_by_name(products)
        elif choice == '5':
            pm.display_all_products(products)
        elif choice == '6':
            pm.save_data(products) 
            print("Cảm ơn bạn đã sử dụng chương trình. Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng thử lại!")

if __name__ == "__main__":
    main()