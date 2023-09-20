import sqlite3
import csv

db_filename = "/Users/alexkarry/Desktop/FOLDERS/Programming/Python/Advanced_Python_NYU/python_data_apy/session_02_working_files/session_2.db"

table_name = 'revenue'

csv_filename = "/Users/alexkarry/Desktop/FOLDERS/Programming/Python/Advanced_Python_NYU/python_data_apy/session_02_working_files/revenue_from_db.csv"

def sql_to_csv(db_filename, table_name, csv_filename):

    conn = sqlite3.connect(db_filename)
    cursor = conn.cursor()

    table_name = 'SELECT * FROM revenue'

    cursor.execute(table_name)

    header = [description[0] for description in cursor.description]
    print(header)
    
    wfh = open(csv_filename, 'w', newline='')
    writer = csv.writer(wfh)
    writer.writerow(header)

    for row in cursor:
        writer.writerow(row)
    
    wfh.close()
    conn.close()

sql_to_csv(db_filename, table_name, csv_filename)

