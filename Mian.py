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
# delete_user(1)

print("USERS AFTER DELETE:")
print(get_all_users())



from Models.Categorie_model import *

print("Adding category...")
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










import datetime
from Models.Expenses_model import *

# print("=== Test 1: Adding expense ===")
# result = add_expenses(
#     user_id=1,
#     category_id=2,
#     amount=50.75,
#     expense_date="2025-11-16",
#     description="Lunch at restaurant"
# )
# print(f"Add expense result: {result}")

# print("\n=== Test 2: Adding expense with datetime ===")
# result = add_expenses(
#     user_id=1,
#     category_id=3,
#     amount=100.00,
#     expense_date=datetime.datetime.now(),
#     description="Shopping"
# )
# print(f"Add expense result: {result}")

print("\n=== Test 3: Show all expenses for user 1 ===")
expenses = showallexpense_byUserId(1)
for expense in expenses:
    print(expense)

print("\n=== Test 4: Show specific expense ===")
expense = show_specExp_byUserId(user_id=1, expense_id=1)
print(expense)

print("\n=== Test 5: Modify expense ===")
result = modifie_expenses(
    expense_id=1,
    amount=60.00,
    description="Updated: Lunch at restaurant"
)
print(f"Modify result: {result}")

# print("\n=== Test 6: Delete expense ===")
# # result = delete_expense(expense_id=2)
# print(f"Delete result: {result}")

print("\n=== Test 7: Check remaining expenses ===")
expenses = showallexpense_byUserId(1)
print(f"Total expenses remaining: {len(expenses)}")
for expense in expenses:
    print(expense)




from Models.income_model import *

# add_income(
#     user_id=1,
#     source="Job Salary",
#     amount=3500.00,
#     income_date="2025-11-18",
#     notes="Monthly salary"
# )

# add_income(
#     user_id=1,
#     source="Freelance Project",
#     amount=800.00,
#     income_date="2025-11-19",
#     notes="Web app development"
# )

# Test 3 — Fetch all incomes
print("\n2️⃣ All incomes for user 1:")
incomes = get_all_income(1)
for inc in incomes:
    print(inc)

# Test 4 — Get one income by ID
print("\n3️⃣ Get income with ID 1:")
income = get_income_by_id(1)
print(income)

# Test 5 — Update income
print("\n4️⃣ Updating income ID 1...")
updated = update_income(
    income_id=1,
    source="Updated Salary",
    amount=3600.00,
    income_date="2025-11-20",
    notes="Adjusted salary"
)
print("Update status:", updated)

# Test 6 — Show updated income
print("\n5️⃣ After update:")
print(get_income_by_id(1))

# print("\n6️⃣ Deleting income ID 2...")
# deleted = delete_income(2)
# print("Delete status:", deleted)

# Test 8 — Total income
print("\n7️⃣ Total income for user 1:")
total = get_total_income(1)
print("Total:", total)


print("\nAdding income...")
# add_income(
#     user_id=1,
#     source="Test Job",
#     amount=1200.50,
#     income_date="2025-11-20",
#     notes="First test income"
# )
print("Income added!")

print("\nAll incomes for user 1:")
incomes = get_all_income(1)
print(incomes)

print("\nIncome ID 1:")
print(get_income_by_id(1))

print("\nUpdating income ID 1...")
update_income(
    income_id=1,
    source="Updated Job",
    amount=1500.00,
    income_date="2025-11-21",
    notes="Updated notes"
)
print("Updated!")
print(get_income_by_id(1))

print("\nTotal income for user 1:")
print(get_total_income(1))

# ➤ Delete income (optional)
# print("\nDeleting income ID 1...")
# delete_income(1)
# print("Deleted!")
