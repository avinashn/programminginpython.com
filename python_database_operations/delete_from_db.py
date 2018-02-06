__author__ = 'Avinash'
import pymysql

# Open database connection
db = pymysql.connect("localhost", "root", "", "python_tutorials")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to DELETE required records
sql = "DELETE FROM PERSON WHERE AGE > '%d'" % (24)
try:
    # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    db.commit()
except pymysql.error:
    # Rollback in case there is any error
    db.rollback()

# disconnect from server
db.close()
