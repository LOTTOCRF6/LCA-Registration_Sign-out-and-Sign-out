import mysql.connector

mydb = mysql.connector.connect(user='sql4423138', password='dwD2bh8UpN', host='sql4.freesqldatabase.com',
                               database='sql4423138', auth_plugin='mysql_native_password')
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM Register")
for x in mycursor:
    print(x)
#mycursor.execute("CREATE TABLE Register(ID_No INT NOT NULL AUTO_INCREMENT, Name VARCHAR(225) NOT NULL, surname VARCHAR(225) NOT NULL,Phone_No VARCHAR(225) NOT NULL, Password VARCHAR(225) NOT NULL, Next_of_kin_Fullname VARCHAR(225) NOT NULL,Next_of_kin_Phone_No VARCHAR(225) NOT NULL, PRIMARY KEY (ID_NO))")
