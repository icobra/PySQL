# coding: utf8
# version 0.001
# SQL connector + Simple SQL base

import mysql.connector
conn = mysql.connector.connect(database="db", host="localhost",user="user",
    password="youpassword")

#find some data
cursor = conn.cursor()
cursor.execute("SELECT password FROM Users WHERE name = 'lol'");
rows = cursor.fetchall()
print (rows)
