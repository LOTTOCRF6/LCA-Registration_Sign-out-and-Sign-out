import mysql.connector

mydb = mysql.connector.connect(user='sql4423138', password='dwD2bh8UpN', host='sql4.freesqldatabase.com',
                               database='sql4423138', auth_plugin='mysql_native_password')
mycursor = mydb.cursor()

#mycursor.execute("ALTER TABLE Register ADD (Register_DateTime VARCHAR(225) NOT NULL)")
#mycursor.execute("ALTER TABLE Register DROP COLUMN Register_DateTime")
#mycursor.execute("DELETE FROM Register WHERE  ")
#mycursor.execute("SELECT * FROM Register")
mycursor.execute("DESCRIBE Register")
#mycursor.execute("TRUNCATE TABLE Register")
for x in mycursor:
    print(x)