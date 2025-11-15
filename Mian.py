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



# print("Adding user...")
# add_user("Hicham", "Akil", "AA123", "hicham@mail.com")

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



from Models.Categorie_model import *

# print("Adding category...")
# add_categorie("Electronics", "Electronic devices")
print("\nAll categories:")
categories = show_all_categories()
for cat in categories:
   print(f"ID: {cat[0]}, Name: {cat[1]}, Description: {cat[2]}")
   print("\nUpdating category...")
   modi_categorie(1, category_name="Tech Gadgets")    
   print("\nUpdated category:")
   cat = show_categorie_bId(1)
   print(f"ID: {cat[0]}, Name: {cat[1]}, Description: {cat[2]}")