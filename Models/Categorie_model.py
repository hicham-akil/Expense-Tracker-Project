from dbs.db_config import get_connection

def add_categorie(category_name,description):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("""
    Insert Into  categories(category_name,description) values(:1,:2)
""",(category_name,description))
    conn.commit()
    cursor.close()
    conn.close()
    return True

def show_all_categories():
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("Select * from categories")
    categories=cursor.fetchall()
    cursor.close()
    conn.close()
    return categories



def show_categorie_bId(category_id):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("Select * from categories where category_id =:1",(category_id,))
    categorie=cursor.fetchone()
    cursor.close()
    conn.close()
    return categorie






def modi_categorie(category_id,category_name=None,description=None):
    conn=get_connection()
    cursor=conn.cursor()
    values={}
    fields=[]
    
    if category_name:
        values["category_name"]=category_name
        fields.append("category_name=:category_name")
    
    if description:
        values["description"]=description
        fields.append("description=:description")
    if not fields:
        return False
    query=f"Update categories set {', '.join(fields)} where category_id=:category_id"
    values["category_id"]=category_id
    cursor.execute(query,values)
    conn.commit()
    cursor.close()
    conn.close()
    return True


def Delete_categories(category_id):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("Delete from categories where  category_id=:1 ",(category_id,))
    conn.commit()
    cursor.close()
    conn.close()
