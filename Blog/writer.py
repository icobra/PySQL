# coding: utf8
# version 0.001
# SQL connector + Simple SQL base

import mysql.connector
conn = mysql.connector.connect(database="PySQL", host="localhost",user="Bloger",
    password="NoPass2140")

#write some data
cursor = conn.cursor()
query = "INSERT INTO Posts(id,postdate,name,information) VALUES(%s,%s,%s,%s)"
cursor.execute(query,[1, "01.06.2018", "Admin", "Very intresting message"])
cursor.execute(query,[2, "02.06.2018", "Admin", "Hello into our Blog"])
conn.commit()