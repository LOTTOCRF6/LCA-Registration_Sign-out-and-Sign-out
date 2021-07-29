import mysql.connector

mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1', database='mydb',
                               auth_plugin='mysql_native_password')
mycursor = mydb.cursor()

#mycursor.execute("ALTER TABLE Logins ADD (Login_DateTime VARCHAR(225) NOT NULL)")
#mycursor.execute("DESCRIBE Logins")
mycursor.execute("SELECT * FROM Logins")
#mycursor.execute("CREATE TABLE Logins(ID_No INT NOT NULL AUTO_INCREMENT, Name VARCHAR(225) NOT NULL, Password VARCHAR(225) NOT NULL, PRIMARY KEY (ID_NO))")
for x in mycursor:
    print(x)