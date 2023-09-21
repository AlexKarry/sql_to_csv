import sqlite3
import csv

db_filename = "../session_2.db"

table_name = 'revenue'

csv_filename = "../revenue_from_db.csv"

def sql_to_csv(db_filename, table_name, csv_filename):

    conn = sqlite3.connect(db_filename)
    cursor = conn.cursor()

    query = f'SELECT * FROM {table_name}'
    cursor.execute(query)

    header = [description[0] for description in cursor.description]
    
    wfh = open(csv_filename, 'w', newline='')
    writer = csv.writer(wfh)
    writer.writerow(header)

    for row in cursor:
        writer.writerow(row)
    
    wfh.close()
    conn.close()

sql_to_csv(db_filename, table_name, csv_filename)



