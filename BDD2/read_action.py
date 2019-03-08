#!/usr/bin/python3
import mysql.connector


def read():
    mydb = mysql.connector.connect(
        host="localhost",
        user="phpmyadmin",
        passwd="Campusdavid07.",
        database="Herboristerie"
    )

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM Plante")

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

# print(mydb)

