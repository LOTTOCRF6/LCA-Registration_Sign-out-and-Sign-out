import mysql.connector

mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1', database='LCA',
                               auth_plugin='mysql_native_password')
mycursor = mydb.cursor()

#mycursor.execute("ALTER TABLE Administration ADD (Admin_Login_DateTime VARCHAR(225) NOT NULL)")
#mycursor.execute("ALTER TABLE Administration DROP COLUMN Admin_Login_DateTime")
#mycursor.execute(("DROP TABLE Admin_Registers"))
#mycursor.execute("DELETE FROM Administration WHERE ID_No 4 ")
mycursor.execute("SELECT * FROM Admin_Register")
#mycursor.execute("DESCRIBE Admin_Register")
#mycursor.execute("TRUNCATE TABLE Register")
#mycursor.execute("CREATE DATABASE LCA ")
#mycursor.execute("USE LCA")
#mycursor.execute("CREATE TABLE Admin_Register(ID_No INT NOT NULL AUTO_INCREMENT, Name VARCHAR(225) NOT NULL,Surname VARCHAR(225),Phone_No VARCHAR(225) NOT NULL, Password VARCHAR(225) NOT NULL,Next_of_kin_Fullname VARCHAR(225) NOT NULL,Next_of_kin_Phone_No VARCHAR(225) NOT NULL,ID_number VARCHAR(225) NOT NULL,Register_DateTime VARCHAR(225) NOT NULL, PRIMARY KEY (ID_No))")
for x in mycursor:
    print(x)