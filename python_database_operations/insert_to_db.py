__author__ = 'Avinash'

import pymysql

# Open database connection
db = pymysql.connect("localhost", "root", "", "python_tutorials")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = """INSERT INTO PERSON(ID, FIRST_NAME,
   LAST_NAME, AGE, SEX )
   VALUES (1, 'ABC', 'ABCD', 20, 'M')"""
try:
    # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    db.commit()
except pymysql.Error:
    # Rollback in case there is any error
    db.rollback()

# disconnect from server
db.close()
