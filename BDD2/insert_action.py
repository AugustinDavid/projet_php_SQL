#!/usr/bin/python3

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="phpmyadmin",
    passwd="Campusdavid07.",
    database="Herboristerie"
)

mycursor = mydb.cursor()

# sql = "INSERT INTO Plante (nom, indication, partie_utilise, prix )" \
#       "VALUES (%s, %s, %s, %s)"
# val = (input('entrez le Nom de la plante'), input('entrez les indications'
#                                                   ' sur son entretien'),
#        input('entrez la partie utilisé'), float(input('entrez le prix de la plante')))

sql = "INSERT INTO Plante(nom, indication, partie_utilise, prix) VALUES (%s, %s, %s, %s)"
val = [("Menthe poivrée", "Anesthésiant", "feuiles", 3),
       ( "Absinthe", "Antiseptique", "feuiles", 4),
       ("Ail", "Antiseptique", "feuiles", 1),
       ("Basilic", "Antiseptique", "feuiles", 5),
       ("Carotte", "Digestion", "feuiles", 2.2),
       ("Aigremoine", "Digestion", "feuiles", 5.4),
       ( "Ronce", "Digestion", "feuiles", 3.21),
       ("Linaire commune", "Diurétique", "feuiles", 1.12),
       ("Mélilot officinal", "Diurétique", "feuiles", 13.22)
       ]


mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")

mycursor.close()
mydb.close()




# print(mydb)