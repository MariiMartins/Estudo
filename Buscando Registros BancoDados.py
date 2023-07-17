# pip install mysql-connector-python

import mysql.connectar

mydb = mysql.connectar.connect(host="localhost", user="root", password="1234",database="pycodebr")

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM clientes")
clientes = mycursor.fetchall()

for clientes in clientes:
    print (clientes)
