""" (1) Phân tích và thiết kế giải pháp (Bắt buộc)
Phân tích Input/Output: Xác định rõ dữ liệu đầu vào (kiểu dữ liệu), dữ liệu đầu ra mong đợi.
input: ds dp (list), menu(str), 
Đề xuất giải pháp: Cách sử dụng các hàm, phương thức hợp lệ, kiểm tra dữ liệu hợp lệ và các bước thực hiện chương trình.
Thiết kế thuật toán: Viết Pseudocode hoặc mô tả luồng chương trình.
"""
# (2) Triển khai code
# Viết source code Python hoàn chỉnh.
# Xử lý các Edge cases đã nêu ở trên.
# Code phải sạch sẽ, dễ đọc, sử dụng snake_case cho tên biến và có comment. Chạy mượt mà với cả trường hợp hợp lệ và không hợp lệ.

product_list = [
    {
        "product_id": "SP001",
        "product_name": "Áo polo nam",
        "price": 299000,
        "quantity": 20
    },
    {
        "product_id": "SP002",
        "product_name": "Quần kaki nam",
        "price": 399000,
        "quantity": 15
    },
    {
        "product_id": "SP003",
        "product_name": "Váy công sở nữ",
        "price": 459000,
        "quantity": 10
    }
]

while True:
    print("===== HỆ THỐNG QUẢN LÝ SẢN PHẨM YODY =====")
    print("1. Hiển thị danh sách sản phẩm")
    print("2. Thêm sản phẩm mới")
    print("3. Cập nhật thông tin sản phẩm")
    print("4. Xóa sản phẩm theo mã")
    print("5. Thoát chương trình")

    menu = input("Nhập lựa chọn (1-5): ")

    match menu:
        case "1":
            numberical = 0
            print("Danh sách sản phẩm hiện tại:")

            if (product_list == []):
                print("Danh sách sản phẩm hiện đang trống.")

            for item in product_list:
                numberical += 1
                print(f"{numberical}. Mã SP: {item['product_id']:<5} | Tên: {item['product_name']:<20} | Giá: {item['price']:<5} | Số lượng: {item['quantity']}")
            print()
        case "2":
            found = False
            user_in_id = input("Nhập mã sản phẩm: ").strip().upper()

            for item in product_list:
                if (item["product_id"] == user_in_id):
                    found = True
                    print("Mã sản phẩm bị trùng")
                    break

            if (not found):
                user_in_name = input("Nhập tên sản phẩm: ").strip()
                user_in_price = input("Nhập giá sản phẩm: ").strip()

                if (not user_in_price.isdigit() or int(user_in_price) <= 0):
                    print("Giá không hợp lệ")
                    break

                user_in_qty = input("Nhập số lượng sản phẩm: ").strip()
                if (not user_in_qty.isdigit() or int(user_in_qty) <= 0):
                    print("Số lượng không hợp lệ")
                    break

                user_in_price = int(user_in_price)
                user_in_qty = int(user_in_qty)
                product_list.append({"product_id": user_in_id, "product_name": user_in_name, "price": user_in_price, "quantity": user_in_qty})
                print("Thêm sản phẩm thành công")

            print()
        case "3":
            found = False
            user_in_id = input("Nhập mã sản phẩm cần cập nhật: ").strip().upper()

            for item in product_list:
                if (item["product_id"] == user_in_id):
                    found = True
                    break

            if (not found):
                print("Không tìm thấy mã sản phẩm cần cập nhật!")
            else:
                user_in_name = input("Nhập tên sản phẩm: ").strip()
                user_in_price = input("Nhập giá sản phẩm: ").strip()

                if (not user_in_price.isdigit() or int(user_in_price) <= 0):
                    print("Giá không hợp lệ")
                else:
                    user_in_qty = input("Nhập số lượng tồn kho: ")

                    if (not user_in_qty.isdigit() or int(user_in_qty) <= 0):
                        print("Số lượng không hợp lệ")
                    else:
                        item["product_name"] = user_in_name
                        item["price"] = int(user_in_price)
                        item["quantity"] = int(user_in_qty)
                        print("Cập nhật sản phẩm thành công")
            print()
        case "4":
            found = False
            user_in_id = input("Nhập mã sản phẩm cần xóa: ").strip().upper()

            for item in product_list:
                if (item["product_id"] == user_in_id):
                    found = True
                    break

            if (not found):
                print("Không tìm thấy mã sản phẩm cần xóa!")
            else:
                product_list.remove(item)
                print("Xóa sản phẩm thành công")
            print()
        case "5":
            print("Thoát chương trình.Sau đó dừng chương trình.")
            break
        case _:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại!")