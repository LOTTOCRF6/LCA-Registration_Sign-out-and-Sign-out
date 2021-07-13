import mysql.connector

mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1', database='LCA',
                               auth_plugin='mysql_native_password')
mycursor = mydb.cursor()

#mycursor.execute("SELECT * FROM Logouts")
mycursor.execute("DESCRIBE Logouts")
#mycursor.execute("CREATE TABLE Logouts(ID_No INT NOT NULL AUTO_INCREMENT, Name VARCHAR(225) NOT NULL, Password VARCHAR(225) NOT NULL, Logout_DateTime VARCHAR(225) NOT NULL, PRIMARY KEY (ID_NO))")
for x in mycursor:
    print(x)