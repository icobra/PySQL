# coding: utf8
# version 0.001
# SQL connector + Simple SQL base

import mysql.connector
conn = mysql.connector.connect(database="db", host="localhost",user="user",
    password="youpassword")

#replace some data
cursor = conn.cursor()
cursor.execute("UPDATE Users SET password = 'BAD' WHERE name = 'root'");
conn.commit()
