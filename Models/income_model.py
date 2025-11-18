from dbs.db_config import get_connection

def add_income(user_id, source, amount, income_date, notes):
    """Add a new income record"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO income(user_id, source, amount, income_date, notes) VALUES(:1, :2, :3, :4, :5)",
        (user_id, source, amount, income_date, notes)
    )
    conn.commit()
    cursor.close()
    conn.close()
    return True

def get_all_income(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT income_id, user_id, source, amount, income_date, notes FROM income WHERE user_id = :1 ORDER BY income_date DESC",
        (user_id,)
    )
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    
    income_list = []
    for row in rows:
        income_list.append({
            'income_id': row[0],
            'user_id': row[1],
            'source': row[2],
            'amount': row[3],
            'income_date': row[4],
            'notes': row[5]
        })
    return income_list

def get_income_by_id(income_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT income_id, user_id, source, amount, income_date, notes FROM income WHERE income_id = :1",
        (income_id,)
    )
    row = cursor.fetchone()
    cursor.close()
    conn.close()
    
    if row:
        return {
            'income_id': row[0],
            'user_id': row[1],
            'source': row[2],
            'amount': row[3],
            'income_date': row[4],
            'notes': row[5]
        }
    return None

def update_income(income_id, source, amount, income_date, notes):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE income SET source = :1, amount = :2, income_date = :3, notes = :4 WHERE income_id = :5",
        (source, amount, income_date, notes, income_id)
    )
    rows_affected = cursor.rowcount
    conn.commit()
    cursor.close()
    conn.close()
    return rows_affected > 0

def delete_income(income_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM income WHERE income_id = :1", (income_id,))
    rows_affected = cursor.rowcount
    conn.commit()
    cursor.close()
    conn.close()
    return rows_affected > 0




def get_total_income(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT SUM(amount) FROM income WHERE user_id = :1",
        (user_id,)
    )
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result[0] if result[0] else 0


 