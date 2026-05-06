from db import init_db
from crud import create_user, get_all_users, get_user_by_id, update_user, delete_user

init_db()
print("Таблица создана\n")

# CREATE
user1 = create_user("Айгерим", "aigеrim@example.com", 25)
user2 = create_user("Берик", "berik@example.com", 30)
user3 = create_user("Дана", "dana@example.com", 22)
print(f"Создано: {user1}")
print(f"Создано: {user2}")
print(f"Создано: {user3}\n")

# READ ALL
print("Все пользователи:")
for user in get_all_users():
    print(f"  {user}")
print()

# READ ONE
user = get_user_by_id(user1["id"])
print(f"Поиск по id={user1['id']}: {user}\n")

# UPDATE
updated = update_user(user1["id"], name="Айгерим Акбар", age=26)
print(f"Обновлено: {updated}\n")

# DELETE
deleted = delete_user(user3["id"])
print(f"Удалён пользователь id={user3['id']}: {deleted}")

print("\nПользователи после удаления:")
for user in get_all_users():
    print(f"  {user}")
