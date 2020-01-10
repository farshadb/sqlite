import sqlite3


"""
Create a new sqlite database 
"""
database = sqlite3.connect('our_data.db')
print("Database opened.")

""" 
'CREATE TABLE' command will create a table in database using SQL language
'IF NOT EXISTS' command will refuse table error exist error
"""


database.execute(""" CREATE TABLE IF NOT EXISTS employee_records(
    ID INT PRIMARY KEY NOT NULL,
    NAME TEXT NOT NULL,
    DIVISION TEXT NOT NULL,
    STARS INT NOT NULL
) """)


def insert_record(id, name, division, stars):
    database.execute(""" INSERT INTO employee_records(ID,NAME,DIVISION,STARS)
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
    data = database.execute(""" SELECT * FROM employee_records
""")
    for record in data:
        print('ID : ', record[0])
        print('NAME : ', record[1])
        print('DIVISION : ', record[2])
        print('STARTS : ', record[3])
        print()

# insert_record(5, "John", "Lawyer", 3)


read_data()
print("Table created")
database.close()
print("Database closed.")

