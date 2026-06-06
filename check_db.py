import sqlite3
import os

db_path = r'c:\Users\HP\Desktop\4-2_Project\Printed Circuit Board Defect Detection Methods Based on Image Processing, Machine Learning and Deep Learning_ A Survey\signup.db'

if os.path.exists(db_path):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cur.fetchall()
    print(f"Tables: {tables}")
    for table in tables:
        cur.execute(f"PRAGMA table_info({table[0]});")
        print(f"Table {table[0]} info: {cur.fetchall()}")
    conn.close()
else:
    print(f"Database not found at {db_path}")
