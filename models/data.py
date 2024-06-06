from database.db import connect_db

def get_all_data():
    conn = connect_db()
    try:
        with conn.cursor() as cursor:
            sql = "SELECT * FROM data"
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    finally:
        conn.close()

def get_by_id(data_id):
    conn = connect_db()
    try:
        with conn.cursor() as cursor:
            sql = "SELECT * FROM data WHERE id = %s"
            cursor.execute(sql,(data_id,))
            result = cursor.fetchone()
            return result
    finally:
        conn.close()

def create_data(new_data):
    conn = connect_db()
    try:
        with conn.cursor() as cursor:
            sql = "INSERT INTO data (nama_perusahaan, deskripsi, tanggal) VALUES (%s,%s,%s)"
            cursor.execute(sql, (new_data['nama_perusahaan'], new_data['deskripsi'], new_data['tanggal']))
            conn.commit()
            return cursor.lastrowid
    finally:
        conn.close()

def update_data(data_id, new_data):
    pass

def delete_data(data_id):
    conn = connect_db()
    try:
        with conn.cursor() as cursor:
            sql = "DELETE FROM data WHERE id = %s"
            cursor.execute(sql, (data_id,))
            conn.commit()
            return cursor.rowcount
    finally:
        conn.close()