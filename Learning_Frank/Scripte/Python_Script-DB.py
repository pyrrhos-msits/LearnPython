# Connect to mySQL and create a Database

#importiert die Funktionen zur Verbindung mit der Datenbank
import pymysql.connector  
# definiert die Variable 'mydb' die dann in der Folge benutzt wird | Ordnet der Variable 
# mydb die Datennbankverbindung zu.
mydb = mysql.connector.connect(
  host="localhost",
  user="menzel",
  passwd="menzelfrank"
)

print ("connect successfull !!")

#Definiert die Variable 'Cursor' als eine Verbindung aus der Variablen mydb 
#und der Funktion 'Cursor'
cursor = mydb.cursor()

cursor.execute("CREATE DATABASE TestDB")
cursor.close

#create Table

#variable 'mydb'definiert die Verbindungsdaten zur DB 
mydb = mysql.connector.connect(
  host="localhost",
  user="menzel",
  passwd="menzelfrank",
  database="TestDB"
)
#Create Table erzeugt die Tabelle Address mit Spalten und setzt die
#ID als Primary Key mit Autoingrement
cursor = mydb.cursor()
cursor.execute("CREATE Table Address (id INT AUTO_INCREMENT PRIMARY KEY,PLZ int(5),City varchar(255),Street varchar(255), house_number varchar(255))")
cursor.close()

#Create Table Customer
cursor = mydb.cursor()
cursor.execute("CREATE Table Customer (Customer_ID INT AUTO_INCREMENT PRIMARY KEY,ForeignID int(3),Salutation varchar(255),Surname varchar(255),Last_Name varchar(255),PLZ int(5),City varchar(255),Street varchar(255), house_number varchar(255))")
cursor.close

#Insert into Customer Table
cursor = mydb.cursor()
sql = "INSERT INTO Customer (Salutation, Surname, Last_Name) VALUES (%s, %s,%s)"
val = ("Herr", "Harry", "Hirsch" )
cursor.execute (sql, val)
mydb.commit()
print(cursor.rowcount,"record inserted")

 

#Löscht die Tabelle Address
cursor = mydb.cursor()
cursor.execute("DROP Table Address")
cursor.close()

#Import einer CSV Datei
import csv
with open("C:\scripts\Customer.csv", newline='') as csvfile:
	reader = csv.reader(csvfile,delimiter=' ',quotechar=';')
	for row in reader:
		print(', '.join(row))