import sqlite3

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to database {db_file} successfully.")
    except sqlite3.Error as e:
        print(e)
    return conn

def create_expense_table(conn):
    try:
        sql_create_expense_table = """ CREATE TABLE IF NOT EXISTS expenses (
            id integer PRIMARY KEY,
            amount real NOT NULL,
            category text NOT NULL,
            description text,
            date text NOT NULL
        ); """
        cursor = conn.cursor()
        cursor.execute(sql_create_expense_table)
        print("Expense table created successfully.")
    except sqlite3.Error as e:
        print(e)

def add_expense_to_db(conn, expense):
    sql = ''' INSERT INTO expenses(amount,category,description,date)
              VALUES(?,?,?,?) '''
    cursor = conn.cursor()
    cursor.execute(sql, (expense['Amount'], expense['Category'], expense['Description'], expense['Date']))
    conn.commit()
    print("Expense added to the database.")

def fetch_expenses(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()
    return rows
