import datetime

LOG_FILE = "activity.log"

def write_log(action, product_name=""):
    time_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(f"[{time_now}] {action} - {product_name}\n")


# Ví dụ tích hợp vào chương trình
def log_add_product(product):
    write_log("ADD PRODUCT", product.get("name", ""))


def log_delete_product(product):
    write_log("DELETE PRODUCT", product.get("name", ""))


def log_update_product(product):
    write_log("UPDATE PRODUCT", product.get("name", ""))


def log_custom(message):
    write_log("CUSTOM ACTION", message)