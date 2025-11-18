from dbs.db_config import get_connection

def add_budget(user_id, category_id, amount_limit, month_year):
    """Add a new budget record"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO budgets(user_id, category_id, amount_limit, month_year) VALUES(:1, :2, :3, :4)",
        (user_id, category_id, amount_limit, month_year)
    )
    conn.commit()
    cursor.close()
    conn.close()
    return True

def get_all_budgets(user_id):
    """Retrieve all budget records for a specific user"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT budget_id, user_id, category_id, amount_limit, month_year FROM budgets WHERE user_id = :1 ORDER BY month_year DESC",
        (user_id,)
    )
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    
    budget_list = []
    for row in rows:
        budget_list.append({
            'budget_id': row[0],
            'user_id': row[1],
            'category_id': row[2],
            'amount_limit': row[3],
            'month_year': row[4]
        })
    return budget_list

def get_budget_by_id(budget_id):
    """Retrieve a specific budget record by ID"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT budget_id, user_id, category_id, amount_limit, month_year FROM budgets WHERE budget_id = :1",
        (budget_id,)
    )
    row = cursor.fetchone()
    cursor.close()
    conn.close()
    
    if row:
        return {
            'budget_id': row[0],
            'user_id': row[1],
            'category_id': row[2],
            'amount_limit': row[3],
            'month_year': row[4]
        }
    return None

def update_budget(budget_id, category_id, amount_limit, month_year):
    """Update an existing budget record"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE budgets SET category_id = :1, amount_limit = :2, month_year = :3 WHERE budget_id = :4",
        (category_id, amount_limit, month_year, budget_id)
    )
    rows_affected = cursor.rowcount
    conn.commit()
    cursor.close()
    conn.close()
    return rows_affected > 0

def delete_budget(budget_id):
    """Delete a budget record"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM budgets WHERE budget_id = :1", (budget_id,))
    rows_affected = cursor.rowcount
    conn.commit()
    cursor.close()
    conn.close()
    return rows_affected > 0