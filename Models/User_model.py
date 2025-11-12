from dbs.db_config import get_connection

def add_user(name,prenom,cin,email):
    conn=get_connection()
    cursor =conn.cursor()
    cursor.execute("""
     Insert into users(name,prenom,cin,email)
                   values(:1,:2,:3,:4)
""",(name,prenom,cin,email))
    conn.commit()
    cursor.close()
    conn.close
def get_all_users():
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("select * From users Order by created_at")
    users=cursor.fetchall()
    cursor.close()
    conn.close()
    return users