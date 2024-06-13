from database.db import connect_db
import bcrypt
import pymysql

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
            hashedpw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            sql = "INSERT INTO users (username, password) VALUES (%s, %s)"
            cursor.execute(sql,(username, hashedpw.decode('utf-8')))
            conn.commit()
            return True
    finally:
        conn.close()

def user_login(username, password):
    conn = connect_db()
    try:
        with conn.cursor() as cursor:
            sql = "SELECT * FROM users WHERE username = %s"
            cursor.execute(sql, (username,))
            user = cursor.fetchone()
            if user and bcrypt.checkpw(password.encode('utf-8'), user['password'].encode('utf-8')):
                return user
            else:
                return False
            
    except pymysql.MySQLError as e:
        print(f"Database error: {e}")
        return False
    finally:
        conn.close()