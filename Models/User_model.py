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
    conn.close()


def get_all_users():
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("select * From users Order by created_at")
    users=cursor.fetchall()
    cursor.close()
    conn.close()
    return users


def get_user_bid(id):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("select * from users where user_id=:1",(id,))
    user=cursor.fetchone()
    cursor.close()
    conn.close()
    return user


def update_user_info(user_id, new_name=None, new_prenom=None, new_cin=None, new_email=None):
    conn = get_connection()
    cursor = conn.cursor()

    fields = []
    values = {}

    if new_name:
        fields.append("name = :name")
        values["name"] = new_name

    if new_prenom:
        fields.append("prenom = :prenom")
        values["prenom"] = new_prenom

    if new_cin:
        fields.append("cin = :cin")
        values["cin"] = new_cin

    if new_email:
        fields.append("email = :email")
        values["email"] = new_email

    if not fields:
        return False 

    query = f"UPDATE users SET {', '.join(fields)} WHERE user_id = :user_id"
    values["user_id"] = user_id

    cursor.execute(query, values)
    conn.commit()

    cursor.close()
    conn.close()
    return True

def delete_user(user_id):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("delete from users where user_id=:1",(user_id,))
    conn.commit()
    cursor.close()
    conn.close()