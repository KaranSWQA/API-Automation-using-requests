import mysql.connector

from Utilities.configuration import *

conn = getConnection()
print(conn.is_connected())  # will show whether it is connected or not in bool
cursor = conn.cursor()  # it will help to coonect with sql
cursor.execute('use APIDevelop')
cursor.execute('select * from CustomerInfo')  # It will execute the sql command
row = cursor.fetchall()  # Return list of tuples
print(row)
# Note: when using .fetchone() it will grab the first data from table and then if u used .fetchall() it will grab from 2nd row
# That's because the cursor has moved to second row

# WAP to sum all the amt
sums = 0
for s in row:
    sums = sums + s[2]
print(sums)

query = "update customerInfo set Location =%s where CourseName =%s"
data = ("Aus", "Jmeter")
cursor.execute(query, data)
conn.commit()  # to execute the query
conn.close()
