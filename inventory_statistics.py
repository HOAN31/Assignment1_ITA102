# 9) Thống kê tổng quan kho hàng
def inventory_statistics(products):
    print("\n--- THỐNG KÊ KHO HÀNG POLY-LAP ---")
    if len(products) == 0:
        print("Kho hàng hiện đang trống!")
        return

    tong_gia_tri = 0
    sap_het_hang = []

    for p in products:
        # Tính tổng giá trị = Giá * Số lượng
        tong_gia_tri += p["price"] * p["quantity"]
        
        # Lọc ra các sản phẩm tồn kho thấp (dưới 5 chiếc)
        if p["quantity"] < 5:
            sap_het_hang.append(p)

    print(f"Tổng số mẫu mã laptop: {len(products)}")
    print(f"Tổng giá trị tài sản trong kho: {tong_gia_tri:,} VNĐ")
    
    if len(sap_het_hang) > 0:
        print("\n[!] CẢNH BÁO SẮP HẾT HÀNG:")
        for p in sap_het_hang:
             print(f" - {p['name']} (Mã: {p['id']}) | Chỉ còn: {p['quantity']} chiếc")