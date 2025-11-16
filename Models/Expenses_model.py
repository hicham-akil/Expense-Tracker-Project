import datetime
from dbs.db_config import get_connection

def add_expenses(user_id,category_id,amount,expense_date,description):

    conn=get_connection()
    cursor=conn.cursor()
    if isinstance(expense_date,str):
        expense_date=datetime.datetime.strptime(expense_date,"%Y-%m-%d" )
    cursor.execute("Insert into expenses(user_id,category_id,amount,expense_date,description) values(:1,:2,:3,:4,:5)",(user_id,category_id,amount,expense_date,description))
    conn.commit()
    cursor.close()
    conn.close()
    return True


def showallexpense_byUserId(user_id):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("Select * from expenses where user_id=:1",(user_id,))
    expenses_of_user=cursor.fetchall()
    cursor.close()
    conn.close()
    return expenses_of_user

def show_specExp_byUserId(user_id,expense_id):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("Select * from expenses where user_id=:1 and expense_id=:2",(user_id,expense_id))
    expense_of_user=cursor.fetchone()
    cursor.close()
    conn.close()
    return expense_of_user

def modifie_expenses(expense_id,user_id=None,category_id=None,amount=None,expense_date=None,description=None):
    conn=get_connection()
    cursor=conn.cursor()
    values={}
    fieldes=[]
    if user_id is not None:
        values["user_id"]=user_id
        fieldes.append("user_id=:user_id")
        
    if category_id is not None:
        values["category_id"]=category_id
        fieldes.append("category_id=:category_id")
    if amount is not None:
        values["amount"]=amount
        fieldes.append("amount=:amount")
    if expense_date is not None:
        values["expense_date"]=expense_date
        fieldes.append("expense_date=:expense_date")
    if description is not None:
        values["description"]=description
        fieldes.append("description=:description")
    if not fieldes:
        return False
        
    query=f"Update expenses set {', '.join(fieldes)} where expense_id=:expense_id"
    values["expense_id"]=expense_id
    cursor.execute(query,values)
    conn.commit()
    cursor.close()
    conn.close()
    return True

def delete_expense(expense_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM expenses WHERE expense_id=:1", (expense_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return True
      
        
    