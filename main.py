import product_manager as pm
import user_manager as um   # <--- Import module mới

def user_menu():
    while True:
        print("\n--- QUẢN LÝ USER ---")
        print("1. Tạo user")
        print("2. Hiển thị danh sách user")
        print("0. Quay lại menu chính")

        choice = input("Nhập lựa chọn: ")

        if choice == "1":
            um.create_user()
        elif choice == "2":
            um.list_users()
        elif choice == "0":
            break
        else:
            print("Lựa chọn không hợp lệ, thử lại!")

def main():
    products = pm.load_data() 
    
    while True:
        print("\n--- QUẢN LÝ CỬA HÀNG POLY-LAP ---")
        print("1. Thêm sản phẩm")
        print("2. Cập nhật sản phẩm")
        print("3. Xóa sản phẩm")
        print("4. Tìm kiếm sản phẩm")
        print("5. Hiển thị tất cả sản phẩm")
        print("6. Quản lý user")   # <--- Thêm lựa chọn mới
        print("0. Thoát")
        
        choice = input("Nhập lựa chọn của bạn (0-6): ")
        
        if choice == '1':
            products = pm.add_product(products)
            pm.save_data(products)
        elif choice == '2':
            pm.update_product(products)
            pm.save_data(products)
        elif choice == '3':
            pm.delete_product(products)
            pm.save_data(products)
        elif choice == '4':
            pm.search_product_by_name(products)
        elif choice == '5':
            pm.display_all_products(products)
        elif choice == '6':
            user_menu()    # <--- Gọi menu con
        elif choice == '0':
            pm.save_data(products) 
            print("Cảm ơn bạn đã sử dụng chương trình. Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng thử lại!")

if __name__ == "__main__":
    main()