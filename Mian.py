from dbs.db_config import get_connection
from Models.User_model import *


try :
    conn=get_connection()
    print("connected to oracle successfully")
except Exception as e:
    print("connection failed ")
    print(e)
finally:
    if conn in locals() and conn:
        conn.close()



print("Adding user...")
add_user("Hicham", "Akil", "AA123", "hicham@mail.com")

print("ALL USERS:")
print(get_all_users())

print("GET USER ID 1:")
print(get_user_bid(1))

print("UPDATING...")
update_user_info(1, new_email="new@test.com")

print("AFTER UPDATE:")
print(get_user_bid(1))

print("DELETING...")
delete_user(1)

print("USERS AFTER DELETE:")
print(get_all_users())
