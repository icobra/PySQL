# coding: utf8
# version 0.001
# SQL connector + Simple SQL base

import mysql.connector
conn = mysql.connector.connect(database="PySQL", host="localhost",user="Bloger",
    password="NoPass2140")

#deleting some data
cursor = conn.cursor()
cursor.execute("DROP TABLE Posts");
conn.commit()
