import json 
FILE_NAME = "products.json"

# 1) Tải dữ liệu từ file
def load_data():
    try:
        file = open(FILE_NAME, "r", encoding = "utf-8")
        data = json.load(file)
        file.close()
        return data
    except:
        print("Không tìm thấy file!")
        return[]

# 2) Lưu dữ liệu vào file
def save_data(products):
    file = open(FILE_NAME,"w",encoding="utf-8")
    json.dump(products, file)
    file.close()
    

# 3) Thêm sản phẩm
def add_product(products):
    print("\n--- THÊM SẢN PHẨM MỚI ---")
    
    # 1. Tự động tạo mã sản phẩm mới dựa trên số lượng hiện có
    ma_so_moi = len(products) + 1
    new_id = "LT" + str(ma_so_moi).zfill(2) 
    
    name = input("Nhập tên sản phẩm mới: ")
    brand = input("Nhập tên thương hiệu: ")
    price = input_positive_int("Nhập giá sản phẩm: ")
    quantity = input_positive_int("Nhập số lượng tồn kho: ")
    
    #Tạo dictionary cho sản phẩm mới
    product = {
        "id": new_id,
        "name": name,
        "brand": brand,
        "price": price,
        "quantity": quantity
    }
    
    products.append(product)
    print("Đã thêm sản phẩm mới với mã:", new_id)
    
    return products 
    
# 4) Cập nhật sản phẩm
def update_product(products):
    product_id = input("Nhập mã sản phẩm cần cập nhật: ")
    for product in products:
        if product["id"] == product_id:
            print("Tìm thấy sản phẩm. Nhập thông tin mới: ")
            
            product["name"] = input("Tên sản phẩm mới: ")
            product["brand"] = input("Thương hiệu sản phẩm mới: ")
            product["price"] = input_positive_int("Giá mới: ")
            product["quantity"] = input_positive_int("Số lượng lưu kho: ")
            
            print("Cập nhập sản phẩm thành công!")
            return products
    
    print("Không tìm thấy sản phẩm có mã: ", product_id)
    return products

# 5) Xóa sản phẩm
def delete_product(products):
    product_id = int(input("Nhập mã sản phẩm cần xóa: "))
    for product in products:
        if product["id"] == product_id:
            products.remove(product)
            print("Đã xóa sản phẩm thành công!")
            return products
    print("Không tìm thấy sản phẩm có mã: ",product_id)
    return products

# 6) Tìm kiếm sản phẩm theo tên
def search_product_by_name(products):
    print("\n---TÌM KIẾM SẢN PHẨM ---")
    keyword = input("Nhập tên sản phẩm cần tìm: ").lower()
    found_products = []
    
    for p in products:
        if keyword in p["name"].lower():
            found_products.append(p)
    
    if len(found_products) > 0:
        display_all_products(found_products)
    else:
        print("Không tìm thấy sả phẩm nào phù hợp từ khóa: ",keyword)

# 7) Hiển thị toàn bộ sản phẩm
def display_all_products(products):
    print("\n--- DANH SÁCH SẢN PHẨM ---")
    if len(products) == 0:
        print("Danh sách rỗng!")
        return
    
    print("Mã ID | Tên sản phẩm             | Thương hiệu     | Giá bán       | Số lượng ")
    print("-"*80)

    for p in products:
        ma_id = p["id"]
        ten = p["name"]
        hang = p["brand"]
        gia = p["price"]
        sl = p["quantity"]
        
        print("{:<5} | {:<30} | {:<15} | {:<12} | {:<5}".format(ma_id, ten, hang, gia, sl))
        
# Hàm nhập số nguyên không âm
def input_positive_int(message):
    while True:
        try:
            value = int(input(message))
            if value < 0:
                print("Không được nhập số âm! Vui lòng nhập lại.")
                continue
            return value
        except ValueError:
            print("Sai kiểu dữ liệu! Vui lòng nhập số nguyên.")




