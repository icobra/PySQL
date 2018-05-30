# coding: utf8
# version 0.001
# SQL connector + Simple SQL base

import mysql.connector
conn = mysql.connector.connect(database="db", host="localhost",user="user",
    password="youpassword")

#deleting some data
cursor = conn.cursor()
cursor.execute("DELETE FROM  Users WHERE id > 2");
conn.commit()
