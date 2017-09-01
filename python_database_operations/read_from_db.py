__author__ = 'Avinash'
import pymysql

# Open database connection
db = pymysql.connect("localhost", "root", "", "python_tutorials")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = "SELECT * FROM PERSON"
try:
    # Execute the SQL command
    cursor.execute(sql)
    # Fetch all the rows in a list of lists.
    results = cursor.fetchall()
    for row in results:
        fname = row[1]
        lname = row[2]
        age = row[3]
        sex = row[4]
        # Now print fetched result
        print("fname = %s, lname = %s, age = %d, sex = %s" % \
        (fname, lname, age, sex, ))
except:
   print("Error: unable to fetch data")

# disconnect from server
db.close()
