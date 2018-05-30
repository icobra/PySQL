# coding: utf8
# version 0.001
# SQL connector + Simple SQL base

import mysql.connector
conn = mysql.connector.connect(database="db", host="localhost",user="user",
    password="youpassword")

#read some data
cursor = conn.cursor()
cursor.execute("SELECT * FROM Users");
rows = cursor.fetchall()
print (rows)
