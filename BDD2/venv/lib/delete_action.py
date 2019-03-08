#!/usr/bin/python3

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="phpmyadmin",
    passwd="Campusdavid07.",
    database="Herboristerie"
)

mycursor = mydb.cursor()

del_id = (int(input("Entrez ID à supprimer")))

sql = "DELETE FROM Plante WHERE id = '%s'" %del_id


mycursor.execute(sql, del_id)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")
