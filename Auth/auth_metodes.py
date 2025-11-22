from dbs.db_config import get_connection
from Models.User_model import add_user
import bcrypt

def signin(email,password):
    conn=get_connection()
    cursor=conn.cursor()
    
    cursor.execute("select user_id,name,password_hash from users where email=:1",(email,))
    data=cursor.fetchone()

    if not data:
        return False,"email dosent existe"
    user_id,name,password_hash=data
    if not bcrypt.checkpw(password.encode(),password_hash.encode()):
        cursor.close()
        conn.close()
        return False ,"password incorrect"
    cursor.close()
    conn.close()
    return True, f"Welcome {name}"

def signup(name, prenom, cin, email, password):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("select user_id from users where email=:1",(email,))
    data=cursor.fetchone()
    if  data:
        return False,"User existe with this data"
    hashed_pass=bcrypt.hashpw(password.encode(),bcrypt.gensalt()).decode()
    cursor.execute("""INSERT INTO users (name, prenom, cin, email, password_hash)
        VALUES (:1, :2, :3, :4, :5)""",(name,prenom,cin,email,hashed_pass))
    conn.commit()
    cursor.close()
    conn.close()
    return True,f"user register succesfully{name}"



    
    
        