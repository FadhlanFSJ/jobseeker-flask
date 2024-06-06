from database.db import connect_db

def get_all_user():
    conn = connect_db()
    try:
        with conn.cursor() as cursor:
            sql = "SELECT * FROM users"
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    finally:
        conn.close()

def get_user_by_id(id):
    conn = connect_db()
    try:
        with conn.cursor() as cursor:
            sql = "SELECT * FROM users WHERE ID = %s"
            cursor.execute(sql, (id,))
            result = cursor.fetchone()
            return result
    finally:
        conn.close()

def user_register(username, password):
    conn = connect_db()
    try:
        with conn.cursor() as cursor:
            sql = "INSERT INTO users (username, password) VALUES (%s, %s)"
            cursor.execute(sql,(username, password))
            conn.commit()
            return True
    finally:
        conn.close()

def user_login(username, password):
    conn = connect_db()
    try:
        with conn.cursor() as cursor:
            sql = "SELECT * FROM users WHERE username = %s AND password = %s"
            cursor.execute(sql, (username, password))
            user = cursor.fetchone()
            if user:
                return True
            else:
                return False
    finally:
        conn.close()