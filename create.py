# coding: utf8
# version 0.001
# SQL connector + Simple SQL base

import mysql.connector

# connect to bd
conn = mysql.connector.connect(database="db", host="localhost",user="user",
    password="youpassword")

#create some table
cursor = conn.cursor()
cursor.execute("CREATE TABLE Users (id int, name varchar(16), password \
    varchar(16) );")
conn.commit() 
