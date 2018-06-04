# coding: utf8
# version 0.001
# SQL connector + Simple SQL base

import mysql.connector

# connect to bd
conn = mysql.connector.connect(database="PySQL", host="localhost",user="Bloger",
    password="NoPass2140")

#create some table
cursor = conn.cursor()
cursor.execute("CREATE TABLE Posts (id int, postdate varchar(16), name \
	varchar(16), information varchar(1024) );")
conn.commit() 
