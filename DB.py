import sqlite3


"""
Create a new sqlite database 
"""
database = sqlite3.connect('our_data.db')
print("Table created")
print("Database opened.")
"""
We use Cursor because it's so faster
"""
cursor = database.cursor()
print("Cursor created")


""" 
'CREATE TABLE' command will create a table in database using SQL language
'IF NOT EXISTS' command will refuse table error exist error
"""


cursor.execute(""" CREATE TABLE IF NOT EXISTS employee_records(
    ID INT PRIMARY KEY NOT NULL,
    NAME TEXT NOT NULL,
    DIVISION TEXT NOT NULL,
    STARS INT NOT NULL
) """)


def insert_record(id, name, division, stars):
    cursor.execute(""" INSERT INTO employee_records(ID,NAME,DIVISION,STARS)
        VALUES(?,?,?,?)""", (id, name, division, stars))
    database.commit()
    print("Record inserted")


"""
SELECT ID, NAME, DIVISION, STARS FROM employee_records 
is equal to 
SELECT *  FROM employee_records
* means all
"""


def read_data():
    data = cursor.execute(""" SELECT * FROM employee_records ORDER BY NAME""")
    x = cursor.fetchall()
    for record in data:
        print('ID : ', record[0])
        print('NAME : ', record[1])
        print('DIVISION : ', record[2])
        print('STARTS : ', record[3])
        print()
    print("==================")
    print(x)

"""
We MUST use build in modules after inserting and updating in order to
import them into database
"""


def update_record():
    cursor.execute(""" UPDATE employee_records SET DIVISION = 'Engineer'  WHERE ID = 4 """)
    database.commit()
    print("Record updated")


def delete_record():
    cursor.execute(""" DELETE FROM  employee_records WHERE ID = 3 """)
    database.commit()
    print("Record deleted")


# insert_record(5, "John", "Lawyer", 3)

delete_record()
update_record()
read_data()
database.close()
print("Database closed.")

