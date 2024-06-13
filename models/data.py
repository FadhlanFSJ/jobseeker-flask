from database.db import connect_db
import json

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

def get_by_user_id(data_id):
    conn = connect_db()
    try:
        with conn.cursor() as cursor:
            sql = "SELECT * FROM data WHERE created_by = %s"
            cursor.execute(sql,(data_id,))
            result = cursor.fetchall()
            return result
    finally:
        conn.close()

def add_data(new_data):
    conn = connect_db()
    try:
        with conn.cursor() as cursor:
            sql = """
                INSERT INTO data (
                    created_by,
                    employer_name,
                    employer_logo,
                    employer_website,
                    employer_company_type,
                    job_publisher,
                    job_id,
                    job_employment_type,
                    job_title,
                    job_apply_link,
                    job_apply_is_direct,
                    job_apply_quality_score,
                    job_description,
                    job_is_remote,
                    job_posted_at_timestamp,
                    job_posted_at_datetime_utc,
                    job_city,
                    job_state,
                    job_country,
                    job_latitude,
                    job_longitude,
                    job_benefits,
                    job_google_link,
                    job_offer_expiration_datetime_utc,
                    job_offer_expiration_timestamp,
                    job_required_experience,
                    job_required_skills,
                    job_required_education,
                    job_experience_in_place_of_education,
                    job_min_salary,
                    job_max_salary,
                    job_salary_currency,
                    job_salary_period,
                    job_highlights,
                    job_job_title,
                    job_posting_language,
                    job_onet_soc,
                    job_onet_job_zone,
                    job_naics_code,
                    job_naics_name
                ) VALUES (
                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s, %s, %s, %s
                )
            """
            cursor.execute(sql, (
                new_data.get('created_by', None),
                new_data.get('employer_name', None),
                new_data.get('employer_logo', None),
                new_data.get('employer_website', None),
                new_data.get('employer_company_type', None),
                new_data.get('job_publisher', None),
                new_data.get('job_id', None),
                new_data.get('job_employment_type', None),
                new_data.get('job_title', None),
                new_data.get('job_apply_link', None),
                new_data.get('job_apply_is_direct', None),
                new_data.get('job_apply_quality_score', None),
                new_data.get('job_description', None),
                new_data.get('job_is_remote', None),
                new_data.get('job_posted_at_timestamp', None),
                new_data.get('job_posted_at_datetime_utc', None),
                new_data.get('job_city', None),
                new_data.get('job_state', None),
                new_data.get('job_country', None),
                new_data.get('job_latitude', None),
                new_data.get('job_longitude', None),
                json.dumps(new_data.get('job_benefits', None)),
                new_data.get('job_google_link', None),
                new_data.get('job_offer_expiration_datetime_utc', None),
                new_data.get('job_offer_expiration_timestamp', None),
                json.dumps(new_data.get('job_required_experience', None)),
                json.dumps(new_data.get('job_required_skills', None)),
                json.dumps(new_data.get('job_required_education', None)),
                new_data.get('job_experience_in_place_of_education', None),
                new_data.get('job_min_salary', None),
                new_data.get('job_max_salary', None),
                new_data.get('job_salary_currency', None),
                new_data.get('job_salary_period', None),
                json.dumps(new_data.get('job_highlights', None)),
                new_data.get('job_job_title', None),
                new_data.get('job_posting_language', None),
                new_data.get('job_onet_soc', None),
                new_data.get('job_onet_job_zone', None),
                new_data.get('job_naics_code', None),
                new_data.get('job_naics_name', None)
            ))
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