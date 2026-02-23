import json
import os

USERS_FILE = "users.json"

# Load danh sách user từ file
def load_users():
    if not os.path.exists(USERS_FILE):
        return []

    with open(USERS_FILE, "r") as f:
        return json.load(f)

# Lưu danh sách user vào file
def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=4)

# Hàm tạo user mới
def create_user():
    print("=== Create New User ===")
    username = input("Enter username: ")
    email = input("Enter email: ")

    user = {
        "username": username,
        "email": email
    }

    users = load_users()
    users.append(user)
    save_users(users)

    print(f"User created successfully: {user}")

# Hiển thị tất cả user
def list_users():
    users = load_users()
    print("=== List of Users ===")
    for user in users:
        print(f"- {user['username']} | {user['email']}")