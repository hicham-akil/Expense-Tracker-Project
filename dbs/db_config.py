import oracledb

DB_USER = "expense_user"
DB_PASSWORD = "expense123"
DB_DSN = "localhost/XEPDB1"  

def get_connection():
    """Return a connection to Oracle database."""
    return oracledb.connect(
        user=DB_USER,
        password=DB_PASSWORD,
        dsn=DB_DSN
    )
