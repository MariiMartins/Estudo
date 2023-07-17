import mysql.connectar

mydb = mysql.connectar.connect(host="localhost", user="root", password="1234",database="pycodebr")

mycursor = mydb.cursor()
sql = "INSERT INTO clientes (nome,idade,email) VALUES (%s,%s,%s)"
val = [
    ("Felipe",23,"felipe@sql.co"),
    ("Pietro",60,"etropi@gchat.co")
]
mycursor.executemany(sql,val)
mydb.commit()

print(mycursor.rowcont, "Registros Inseridos")