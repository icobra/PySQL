# coding: utf8
# version 0.001
# SQL connector + Simple SQL base

import mysql.connector
conn = mysql.connector.connect(database="db", host="localhost",user="user",
    password="youpassword")

#write some data
cursor = conn.cursor()
query = "INSERT INTO Users(id,name,password) VALUES(%s,%s,%s)"
cursor.execute(query,[1, "root", "root"])
cursor.execute(query,[2, "user", "password"])
cursor.execute(query,[301, "lol", "w00t"])
conn.commit()
