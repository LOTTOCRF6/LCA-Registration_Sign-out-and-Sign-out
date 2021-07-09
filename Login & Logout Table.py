import mysql.connector

mydb = mysql.connector.connect(user='sql4423138', password='dwD2bh8UpN', host='sql4.freesqldatabase.com',
                               database='sql4423138', auth_plugin='mysql_native_password')
mycursor = mydb.cursor()

#mycursor.execute("ALTER TABLE Logins ADD (Login_DateTime VARCHAR(225) NOT NULL)")
#mycursor.execute("DESCRIBE Logins")
mycursor.execute("SELECT * FROM Logins")
for x in mycursor:
    print(x)
#mycursor.execute("CREATE TABLE Logins(ID_No INT NOT NULL AUTO_INCREMENT, Name VARCHAR(225) NOT NULL, Password VARCHAR(225) NOT NULL, PRIMARY KEY (ID_NO))")
