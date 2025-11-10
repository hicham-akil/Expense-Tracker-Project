from db_config import get_connection


try :
    conn=get_connection()
    print("connected to oracle successfully")
except Exception as e:
    print("connection failed ")
    print(e)
finally:
    if conn in locals() and conn:
        conn.close()