from db import get_cursor


# CREATE
def create_user(name: str, email: str, age: int = None) -> dict:
    with get_cursor() as cursor:
        cursor.execute(
            "INSERT INTO users (name, email, age) VALUES (%s, %s, %s) RETURNING *",
            (name, email, age),
        )
        return dict(cursor.fetchone())


# READ ALL
def get_all_users() -> list[dict]:
    with get_cursor() as cursor:
        cursor.execute("SELECT * FROM users ORDER BY id")
        return [dict(row) for row in cursor.fetchall()]


# READ ONE
def get_user_by_id(user_id: int) -> dict | None:
    with get_cursor() as cursor:
        cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
        row = cursor.fetchone()
        return dict(row) if row else None


# UPDATE
def update_user(user_id: int, name: str = None, email: str = None, age: int = None) -> dict | None:
    fields = []
    values = []

    if name is not None:
        fields.append("name = %s")
        values.append(name)
    if email is not None:
        fields.append("email = %s")
        values.append(email)
    if age is not None:
        fields.append("age = %s")
        values.append(age)

    if not fields:
        return get_user_by_id(user_id)

    values.append(user_id)
    query = f"UPDATE users SET {', '.join(fields)} WHERE id = %s RETURNING *"

    with get_cursor() as cursor:
        cursor.execute(query, values)
        row = cursor.fetchone()
        return dict(row) if row else None


# DELETE
def delete_user(user_id: int) -> bool:
    with get_cursor() as cursor:
        cursor.execute("DELETE FROM users WHERE id = %s RETURNING id", (user_id,))
        return cursor.fetchone() is not None
