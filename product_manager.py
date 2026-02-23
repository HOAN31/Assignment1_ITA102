import json 

FILE_NAME = "products.json"

# 1) Tải dữ liệu từ file
# def load_data():
#     try:
#         with open(FILE_NAME, 'r', encoding='utf-8') as file: #dictionary 
#             return json.load(file)

#     except FileNotFoundError:
#         print("Không tìm thấy file!")
#         return [] 
def load_data():
    try:
        file = open(FILE_NAME, "r", encoding = "utf-8")
        data = json.load(file)
        file.close()
        return data
    except:
        print("Không tìm thấy file!")
        return[]
# # 2) Lưu dữ liệu vào file
# def save_data(products): 
#     with open(FILE_NAME, 'w', encoding='utf-8') as file: 
#         json.dump(products, file, indent=4, ensure_ascii=False)
# # json.dump( ghi dữ liệu 
# # products nguồn dữ liệu
# # file, đích đến
# # indent=4, thụt lề tạo khoảng trống dữ liệu
# # ensure_ascii=False) đảm bảo ghi đúng tiếng việt vì trong thư viện sẽ cố mã hóa dấu của tiếng việt
#     print("Đã lưu dữ liệu thành công!")
def save_data(products):
    file = open(FILE_NAME,"w",encoding="utf-8")
    json.dump(products, file)
    file.close()
    

# # 3) Thêm sản phẩm
# def add_product(products):
#     print("\n--- THÊM SẢN PHẨM MỚI ---")
#     name = input("Nhập tên sản phẩm: ")
#     brand = input("Nhập thương hiệu: ")
#     price = int(input("Nhập giá (VNĐ): "))
#     quantity = int(input("Nhập số lượng tồn kho: "))

#     new_id = f"LT{len(products) + 1:02d}" 
    
#     new_product = {
#         "id": new_id,
#         "name": name,
#         "brand": brand,
#         "price": price,
#         "quantity": quantity
#     }
#     products.append(new_product) 
#     print(f"Đã thêm sản phẩm {new_id} thành công!")
#     return products
# def add_product(products):
#     products.id = len(products)+1
#     name = input("Nhập tên sản phẩm mới: ")
#     price = int(input("Nhập giá sản phẩm mới: "))
#     brand = input("Nhập tên thương hiệu sản phẩm mới: ")
#     quantity = int(input("Nhập số lượng sản phẩm mới: "))
#     product ={
#         "id":products.id,
#         "name": name,
#         "price": price,
#         "brand": brand,
#         "quantity": quantity
#     }
#     products.appen(product)
#     return(products)
def add_product(products):
    print("\n--- THÊM SẢN PHẨM MỚI ---")
    
    # 1. Tự động tạo mã sản phẩm mới dựa trên số lượng hiện có
    # Ví dụ: nếu có 2 sản phẩm, mã mới sẽ là LT03
    ma_so_moi = len(products) + 1
    new_id = "LT" + str(ma_so_moi).zfill(2) 
    
    # 2. Nhập thông tin từ bàn phím
    name = input("Nhập tên sản phẩm mới: ")
    brand = input("Nhập tên thương hiệu: ")
    price = int(input("Nhập giá sản phẩm: "))
    quantity = int(input("Nhập số lượng tồn kho: "))
    
    # 3. Tạo dictionary cho sản phẩm mới
    product = {
        "id": new_id,
        "name": name,
        "brand": brand,
        "price": price,
        "quantity": quantity
    }
    
    # 4. Thêm vào danh sách và thông báo thành công
    products.append(product)
    print("Đã thêm sản phẩm mới với mã:", new_id)
    
    return products 
    
    

# # 4) Cập nhật sản phẩm
# def update_product(products):
#     print("\n--- CẬP NHẬT SẢN PHẨM ---")
#     product_id = input("Nhập mã sản phẩm cần cập nhật: ").upper() 
    
#     for product in products:
#         if product["id"] == product_id:
#             print(f"Đang cập nhật cho sản phẩm: {product['name']}")
#             product["name"] = input(f"Tên mới ({product['name']}): ") or product["name"]
#             product["brand"] = input(f"Thương hiệu mới ({product['brand']}): ") or product["brand"]
#             new_price = input(f"Giá mới ({product['price']}): ")
#             if new_price: product["price"] = int(new_price)
                
#             new_quantity = input(f"Số lượng mới ({product['quantity']}): ")
#             if new_quantity: product["quantity"] = int(new_quantity)
                
#             print("Cập nhật thành công!")
#             return
            
#     print("Lỗi: Không tìm thấy sản phẩm!")
def update_product(products):
    product_id = int(input("Nhập sản phẩm cần cập nhập: "))
    for product in products:
        if product[id] == product_id:
            print("Tìm thấy sản phẩm. Nhập thông tin mới: ")
            
            product["name"] = input("Tên sản phẩm mới: ")
            product["brand"] = input("Thương hiệu sản phẩm mới: ")
            product["price"] = int(input("Giá mới: "))
            product["quantity"] = int(input("Số lượng lưu kho: "))
            
            print("Cập nhập sản phẩm thành công!")
            return products
    
    print("Không tìm thấy sản phẩm có mã: ", product_id)
    return products

# # 5) Xóa sản phẩm
# def delete_product(products):
#     print("\n--- XÓA SẢN PHẨM ---")
#     product_id = input("Nhập mã sản phẩm cần xóa: ").upper()
    
#     for i in range(len(products)):
#         if products[i]["id"] == product_id:
#             del products[i]
#             print(f"Đã xóa sản phẩm có mã {product_id}.")
#             return
#     print("Lỗi: Không tìm thấy sản phẩm!")
def delete_product(products):
    product_id = int(input("Nhập mã sản phẩm cần xóa: "))
    for product in products:
        if product["id"] == product_id:
            product.remove(product)
            print("Đã xóa sản phẩm thành công!")
            return products
    print("Không tìm thấy sản phẩm có mã: ",product_id)
    return products

# # 6) Tìm kiếm sản phẩm theo tên
# def search_product_by_name(products):
#     print("\n--- TÌM KIẾM SẢN PHẨM ---")
#     keyword = input("Nhập từ khóa tìm kiếm: ").lower() 
    
#     found_products = [p for p in products if keyword in p["name"].lower()]
    
#     if found_products:
#         display_all_products(found_products)
#     else:
#         print("Không tìm thấy sản phẩm nào phù hợp.")
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

# # 7) Hiển thị toàn bộ sản phẩm
# def display_all_products(products):
#     print("\n--- DANH SÁCH SẢN PHẨM ---")
#     if not products:
#         print("Kho hàng trống.") 
#         return
        
        
#     print(f"{'ID':<5} | {'Tên sản phẩm':<30} | {'Thương hiệu':<15} | {'Giá':<12} | {'SL':<5}")
#     print("-" * 77)
#     for p in products:
#         print(f"{p['id']:<5} | {p['name']:<30} | {p['brand']:<15} | {p['price']:<12} | {p['quantity']:<5}") 
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