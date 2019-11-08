import mysql.connector  as mariadb


mariadb_connection = mariadb.connect(
    user='root',
    password='123456',
    database='testdb')
cursor = mariadb_connection.cursor()

cursor.execute("SELECT name ,age,address FROM CUSTOMERS WHERE ID<=5;")

for (name,age,address) in cursor:
  print("{}  \t{}\t {}".format(name ,age,address))