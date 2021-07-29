import mysql.connector

mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1', database='mydb',
                               auth_plugin='mysql_native_password')
mycursor = mydb.cursor()

#mycursor.execute("CREATE TABLE Register(ID_No INT NOT NULL AUTO_INCREMENT, Name VARCHAR(225) NOT NULL,Surname VARCHAR(225),Phone_No VARCHAR(225) NOT NULL, Password VARCHAR(225) NOT NULL,Next_of_kin_Fullname VARCHAR(225) NOT NULL,Next_of_kin_Phone_No VARCHAR(225) NOT NULL,ID_number VARCHAR(225) NOT NULL,Register_DateTime VARCHAR(225) NOT NULL, PRIMARY KEY (ID_No))")
#mycursor.execute("ALTER TABLE Register ADD (Register_DateTime VARCHAR(225) NOT NULL)")
#mycursor.execute("ALTER TABLE Register DROP COLUMN Register_DateTime")
#mycursor.execute("DELETE FROM Register WHERE  ")
mycursor.execute("SELECT * FROM Register")
#mycursor.execute("DESCRIBE Register")
#mycursor.execute("TRUNCATE TABLE Register")
for x in mycursor:
    print(x)