lshinkuro@lshinkuro-Aspire-E5-551G:~$ sudo mysql_secure_installation
[sudo] password for lshinkuro: 

NOTE: RUNNING ALL PARTS OF THIS SCRIPT IS RECOMMENDED FOR ALL MariaDB
      SERVERS IN PRODUCTION USE!  PLEASE READ EACH STEP CAREFULLY!

In order to log into MariaDB to secure it, we'll need the current
password for the root user.  If you've just installed MariaDB, and
you haven't set the root password yet, the password will be blank,
so you should just press enter here.

Enter current password for root (enter for none): 
OK, successfully used password, moving on...

Setting the root password ensures that nobody can log into the MariaDB
root user without the proper authorisation.

Set root password? [Y/n] y
New password: 
Re-enter new password: 
Password updated successfully!
Reloading privilege tables..
 ... Success!


By default, a MariaDB installation has an anonymous user, allowing anyone
to log into MariaDB without having to have a user account created for
them.  This is intended only for testing, and to make the installation
go a bit smoother.  You should remove them before moving into a
production environment.

Remove anonymous users? [Y/n] y
 ... Success!

Normally, root should only be allowed to connect from 'localhost'.  This
ensures that someone cannot guess at the root password from the network.

Disallow root login remotely? [Y/n] y
 ... Success!

By default, MariaDB comes with a database named 'test' that anyone can
access.  This is also intended only for testing, and should be removed
before moving into a production environment.

Remove test database and access to it? [Y/n] y
 - Dropping test database...
 ... Success!
 - Removing privileges on test database...
 ... Success!

Reloading the privilege tables will ensure that all changes made so far
will take effect immediately.

Reload privilege tables now? [Y/n] y
 ... Success!

Cleaning up...

All done!  If you've completed all of the above steps, your MariaDB
installation should now be secure.

Thanks for using MariaDB!
lshinkuro@lshinkuro-Aspire-E5-551G:~$ sudo mariadb
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 10
Server version: 10.1.41-MariaDB-0ubuntu0.18.04.1 Ubuntu 18.04

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
+--------------------+
3 rows in set (0.00 sec)

MariaDB [(none)]> CREATE DATABASE testDB;
Query OK, 1 row affected (0.00 sec)

MariaDB [(none)]> SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| testDB             |
+--------------------+
4 rows in set (0.00 sec)

MariaDB [(none)]> DROP DATABASE testDB;
Query OK, 0 rows affected (0.03 sec)

MariaDB [(none)]> SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
+--------------------+
3 rows in set (0.00 sec)

MariaDB [(none)]> CREATE DATABASE testDB;
Query OK, 1 row affected (0.00 sec)

MariaDB [(none)]> INSERT INTO CUSTOMERS (ID,NAME,AGE,ADDRESS,SALARY)
    -> Ctrl-C -- exit!
Aborted
lshinkuro@lshinkuro-Aspire-E5-551G:~$ sudo mariadb
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 11
Server version: 10.1.41-MariaDB-0ubuntu0.18.04.1 Ubuntu 18.04

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| testDB             |
+--------------------+
4 rows in set (0.00 sec)

MariaDB [(none)]> USE testDB;
Database changed
MariaDB [testDB]> CREATE TABLE CUSTOMERS(
    -> ID INT NOTNULL,
    -> NAMA VARCHAR (20) NOT NULL,
    -> AGE INT NOT NULL,
    -> ADDRESS CHAR (25),
    -> SALARY DECIMAL(18,20),
    -> PRIMARY KEY (ID) 
    -> );
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near '
NAMA VARCHAR (20) NOT NULL,
AGE INT NOT NULL,
ADDRESS CHAR (25),
SALARY DECIMAL' at line 2
MariaDB [testDB]> CREATE TABLE CUSTOMERS(
    ->    ID   INT              NOT NULL,
    ->    NAME VARCHAR (20)     NOT NULL,
    ->    AGE  INT              NOT NULL,
    ->    ADDRESS  CHAR (25) ,
    ->    SALARY   DECIMAL (18, 2),       
    ->    PRIMARY KEY (ID)
    -> );
Query OK, 0 rows affected (0.31 sec)

MariaDB [testDB]> DESC CUSTOMERS;
+---------+---------------+------+-----+---------+-------+
| Field   | Type          | Null | Key | Default | Extra |
+---------+---------------+------+-----+---------+-------+
| ID      | int(11)       | NO   | PRI | NULL    |       |
| NAME    | varchar(20)   | NO   |     | NULL    |       |
| AGE     | int(11)       | NO   |     | NULL    |       |
| ADDRESS | char(25)      | YES  |     | NULL    |       |
| SALARY  | decimal(18,2) | YES  |     | NULL    |       |
+---------+---------------+------+-----+---------+-------+
5 rows in set (0.03 sec)

MariaDB [testDB]> INSERT INTO CUSTOMERS (ID,NAME,AGE,ADDRESS,SALARY)
    -> VALUES (1, 'Ramesh', 32, 'Ahmedabad', 2000.00 );
Query OK, 1 row affected (0.05 sec)

MariaDB [testDB]> DESC CUSTOMERS;
+---------+---------------+------+-----+---------+-------+
| Field   | Type          | Null | Key | Default | Extra |
+---------+---------------+------+-----+---------+-------+
| ID      | int(11)       | NO   | PRI | NULL    |       |
| NAME    | varchar(20)   | NO   |     | NULL    |       |
| AGE     | int(11)       | NO   |     | NULL    |       |
| ADDRESS | char(25)      | YES  |     | NULL    |       |
| SALARY  | decimal(18,2) | YES  |     | NULL    |       |
+---------+---------------+------+-----+---------+-------+
5 rows in set (0.01 sec)

MariaDB [testDB]> NSERT INTO CUSTOMERS (ID,NAME,AGE,ADDRESS,SALARY)
    -> VALUES (2, 'Khilan', 25, 'Delhi', 1500.00 );
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near 'NSERT INTO CUSTOMERS (ID,NAME,AGE,ADDRESS,SALARY)
VALUES (2, 'Khilan', 25, 'Delh' at line 1
MariaDB [testDB]> INSERT INTO CUSTOMERS (ID,NAME,AGE,ADDRESS,SALARY) VALUES (2, 'Khilan', 25, 'Delhi', 1500.00 );
Query OK, 1 row affected (0.07 sec)

MariaDB [testDB]> SHOW CUSTOMERS;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near 'CUSTOMERS' at line 1
MariaDB [testDB]> SHOW TABLE CUSTOMERS;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near 'CUSTOMERS' at line 1
MariaDB [testDB]> DESC CUTOMERS;
ERROR 1146 (42S02): Table 'testDB.CUTOMERS' doesn't exist
MariaDB [testDB]> SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| testDB             |
+--------------------+
4 rows in set (0.00 sec)

MariaDB [testDB]> USE testDB;
Database changed
MariaDB [testDB]> SHOW testDB;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near 'testDB' at line 1
MariaDB [testDB]> DESC CUSTOMERS;
+---------+---------------+------+-----+---------+-------+
| Field   | Type          | Null | Key | Default | Extra |
+---------+---------------+------+-----+---------+-------+
| ID      | int(11)       | NO   | PRI | NULL    |       |
| NAME    | varchar(20)   | NO   |     | NULL    |       |
| AGE     | int(11)       | NO   |     | NULL    |       |
| ADDRESS | char(25)      | YES  |     | NULL    |       |
| SALARY  | decimal(18,2) | YES  |     | NULL    |       |
+---------+---------------+------+-----+---------+-------+
5 rows in set (0.00 sec)

MariaDB [testDB]> HELP()
    -> Ctrl-C -- exit!
Aborted
lshinkuro@lshinkuro-Aspire-E5-551G:~$ sudo mariadb
[sudo] password for lshinkuro: 
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 12
Server version: 10.1.41-MariaDB-0ubuntu0.18.04.1 Ubuntu 18.04

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| testDB             |
+--------------------+
4 rows in set (0.00 sec)

MariaDB [(none)]> USE testDB;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
MariaDB [testDB]> DESC CUSTOMERS;
+---------+---------------+------+-----+---------+-------+
| Field   | Type          | Null | Key | Default | Extra |
+---------+---------------+------+-----+---------+-------+
| ID      | int(11)       | NO   | PRI | NULL    |       |
| NAME    | varchar(20)   | NO   |     | NULL    |       |
| AGE     | int(11)       | NO   |     | NULL    |       |
| ADDRESS | char(25)      | YES  |     | NULL    |       |
| SALARY  | decimal(18,2) | YES  |     | NULL    |       |
+---------+---------------+------+-----+---------+-------+
5 rows in set (0.00 sec)

MariaDB [testDB]> INSERT INTO CUSTOMERS (ID,NAME,AGE,ADDRESS,SALARY)
    -> VALUES (3, 'kaushik', 23, 'Kota', 2000.00 );
Query OK, 1 row affected (0.06 sec)

MariaDB [testDB]> SHOW TABLE
    -> SHOW TABLE;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near 'SHOW TABLE' at line 2
MariaDB [testDB]> INSERT INTO CUSTOMERS (ID,NAME,AGE,ADDRESS,SALARY)
    -> VALUES (4, 'Chaitali', 25, 'Mumbai', 6500.00 );
Query OK, 1 row affected (0.07 sec)

MariaDB [testDB]> SELECT * FROM CUSTOMERS;
+----+----------+-----+-----------+---------+
| ID | NAME     | AGE | ADDRESS   | SALARY  |
+----+----------+-----+-----------+---------+
|  1 | Ramesh   |  32 | Ahmedabad | 2000.00 |
|  2 | Khilan   |  25 | Delhi     | 1500.00 |
|  3 | kaushik  |  23 | Kota      | 2000.00 |
|  4 | Chaitali |  25 | Mumbai    | 6500.00 |
+----+----------+-----+-----------+---------+
4 rows in set (0.00 sec)

MariaDB [testDB]> SELECT ID,NAME FROM CUSTOMERS;
+----+----------+
| ID | NAME     |
+----+----------+
|  1 | Ramesh   |
|  2 | Khilan   |
|  3 | kaushik  |
|  4 | Chaitali |
+----+----------+
4 rows in set (0.00 sec)

MariaDB [testDB]> INSERT INTO CUSTOMERS (ID,NAME,AGE,ADDRESS,SALARY)
    -> VALUES (5, 'Hardik', 27, 'Bhopal', 8500.00 );
Query OK, 1 row affected (0.12 sec)

MariaDB [testDB]> INSERT INTO CUSTOMERS (ID,NAME,AGE,ADDRESS,SALARY)
    -> VALUES (6, 'Komal', 22, 'MP', 4500.00 );
Query OK, 1 row affected (0.05 sec)

MariaDB [testDB]> INSERT INTO CUSTOMERS 
    -> VALUES (7, 'Muffy', 24, 'Indore', 10000.00 );
Query OK, 1 row affected (0.05 sec)

MariaDB [testDB]> SELECT * FROM CUSTOMERS;
+----+----------+-----+-----------+----------+
| ID | NAME     | AGE | ADDRESS   | SALARY   |
+----+----------+-----+-----------+----------+
|  1 | Ramesh   |  32 | Ahmedabad |  2000.00 |
|  2 | Khilan   |  25 | Delhi     |  1500.00 |
|  3 | kaushik  |  23 | Kota      |  2000.00 |
|  4 | Chaitali |  25 | Mumbai    |  6500.00 |
|  5 | Hardik   |  27 | Bhopal    |  8500.00 |
|  6 | Komal    |  22 | MP        |  4500.00 |
|  7 | Muffy    |  24 | Indore    | 10000.00 |
+----+----------+-----+-----------+----------+
7 rows in set (0.00 sec)

MariaDB [testDB]> SELECT NAME FROM CUSTOMERS WHERE ID:7;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near ':7' at line 1
MariaDB [testDB]> SELECT NAME FROM CUSTOMERS WHERE ID=7;
+-------+
| NAME  |
+-------+
| Muffy |
+-------+
1 row in set (0.00 sec)

MariaDB [testDB]> SELECT * FROM CUSTOMERS WHERE ID=7;
+----+-------+-----+---------+----------+
| ID | NAME  | AGE | ADDRESS | SALARY   |
+----+-------+-----+---------+----------+
|  7 | Muffy |  24 | Indore  | 10000.00 |
+----+-------+-----+---------+----------+
1 row in set (0.01 sec)

MariaDB [testDB]> SELECT ID ,NAME ,SALARY FROM CUSTOMERS WHERE SALARY>2000;
+----+----------+----------+
| ID | NAME     | SALARY   |
+----+----------+----------+
|  4 | Chaitali |  6500.00 |
|  5 | Hardik   |  8500.00 |
|  6 | Komal    |  4500.00 |
|  7 | Muffy    | 10000.00 |
+----+----------+----------+
4 rows in set (0.00 sec)

MariaDB [testDB]> SELECT ID ,NAME ,SALARY FROM CUSTOMERS WHERE NAME = 'Komal';
+----+-------+---------+
| ID | NAME  | SALARY  |
+----+-------+---------+
|  6 | Komal | 4500.00 |
+----+-------+---------+
1 row in set (0.00 sec)

MariaDB [testDB]> select * from customers;
ERROR 1146 (42S02): Table 'testDB.customers' doesn't exist
MariaDB [testDB]> SELECT * FROM CUSTOMERS;
+----+----------+-----+-----------+----------+
| ID | NAME     | AGE | ADDRESS   | SALARY   |
+----+----------+-----+-----------+----------+
|  1 | Ramesh   |  32 | Ahmedabad |  2000.00 |
|  2 | Khilan   |  25 | Delhi     |  1500.00 |
|  3 | kaushik  |  23 | Kota      |  2000.00 |
|  4 | Chaitali |  25 | Mumbai    |  6500.00 |
|  5 | Hardik   |  27 | Bhopal    |  8500.00 |
|  6 | Komal    |  22 | MP        |  4500.00 |
|  7 | Muffy    |  24 | Indore    | 10000.00 |
+----+----------+-----+-----------+----------+
7 rows in set (0.00 sec)

MariaDB [testDB]> SELECT * FROM CUSTOMERS WHERE SALARY > 2000 AND AGE <25;
+----+-------+-----+---------+----------+
| ID | NAME  | AGE | ADDRESS | SALARY   |
+----+-------+-----+---------+----------+
|  6 | Komal |  22 | MP      |  4500.00 |
|  7 | Muffy |  24 | Indore  | 10000.00 |
+----+-------+-----+---------+----------+
2 rows in set (0.00 sec)

MariaDB [testDB]> UPDATE CUSTOMERS 
    -> SET ADDRESS = 'PUNE'
    -> WHERE ID = 6;
Query OK, 1 row affected (0.07 sec)
Rows matched: 1  Changed: 1  Warnings: 0

MariaDB [testDB]> SELECT * FROM CUSTOMERS;
+----+----------+-----+-----------+----------+
| ID | NAME     | AGE | ADDRESS   | SALARY   |
+----+----------+-----+-----------+----------+
|  1 | Ramesh   |  32 | Ahmedabad |  2000.00 |
|  2 | Khilan   |  25 | Delhi     |  1500.00 |
|  3 | kaushik  |  23 | Kota      |  2000.00 |
|  4 | Chaitali |  25 | Mumbai    |  6500.00 |
|  5 | Hardik   |  27 | Bhopal    |  8500.00 |
|  6 | Komal    |  22 | PUNE      |  4500.00 |
|  7 | Muffy    |  24 | Indore    | 10000.00 |
+----+----------+-----+-----------+----------+
7 rows in set (0.00 sec)

MariaDB [testDB]> SELECT * FROM CUSTOMERS
    -> LIMIT 3;
+----+---------+-----+-----------+---------+
| ID | NAME    | AGE | ADDRESS   | SALARY  |
+----+---------+-----+-----------+---------+
|  1 | Ramesh  |  32 | Ahmedabad | 2000.00 |
|  2 | Khilan  |  25 | Delhi     | 1500.00 |
|  3 | kaushik |  23 | Kota      | 2000.00 |
+----+---------+-----+-----------+---------+
3 rows in set (0.00 sec)

MariaDB [testDB]> SELECT * FROM CUSTOMERS
    ->    ORDER BY SALARY;
+----+----------+-----+-----------+----------+
| ID | NAME     | AGE | ADDRESS   | SALARY   |
+----+----------+-----+-----------+----------+
|  2 | Khilan   |  25 | Delhi     |  1500.00 |
|  1 | Ramesh   |  32 | Ahmedabad |  2000.00 |
|  3 | kaushik  |  23 | Kota      |  2000.00 |
|  6 | Komal    |  22 | PUNE      |  4500.00 |
|  4 | Chaitali |  25 | Mumbai    |  6500.00 |
|  5 | Hardik   |  27 | Bhopal    |  8500.00 |
|  7 | Muffy    |  24 | Indore    | 10000.00 |
+----+----------+-----+-----------+----------+
7 rows in set (0.00 sec)

MariaDB [testDB]> SELECT * FROM CUSTOMERS    ORDER BY SALARY DESC;
+----+----------+-----+-----------+----------+
| ID | NAME     | AGE | ADDRESS   | SALARY   |
+----+----------+-----+-----------+----------+
|  7 | Muffy    |  24 | Indore    | 10000.00 |
|  5 | Hardik   |  27 | Bhopal    |  8500.00 |
|  4 | Chaitali |  25 | Mumbai    |  6500.00 |
|  6 | Komal    |  22 | PUNE      |  4500.00 |
|  1 | Ramesh   |  32 | Ahmedabad |  2000.00 |
|  3 | kaushik  |  23 | Kota      |  2000.00 |
|  2 | Khilan   |  25 | Delhi     |  1500.00 |
+----+----------+-----+-----------+----------+
7 rows in set (0.00 sec)

MariaDB [testDB]> SELECT * FROM CUSTOMERS    ORDER BY NAME,SALARY DESC;
+----+----------+-----+-----------+----------+
| ID | NAME     | AGE | ADDRESS   | SALARY   |
+----+----------+-----+-----------+----------+
|  4 | Chaitali |  25 | Mumbai    |  6500.00 |
|  5 | Hardik   |  27 | Bhopal    |  8500.00 |
|  3 | kaushik  |  23 | Kota      |  2000.00 |
|  2 | Khilan   |  25 | Delhi     |  1500.00 |
|  6 | Komal    |  22 | PUNE      |  4500.00 |
|  7 | Muffy    |  24 | Indore    | 10000.00 |
|  1 | Ramesh   |  32 | Ahmedabad |  2000.00 |
+----+----------+-----+-----------+----------+
7 rows in set (0.00 sec)

MariaDB [testDB]> SELECT NAME, SUM(SALARY) FROM CUSTOMERS
    ->    GROUP BY NAME;
+----------+-------------+
| NAME     | SUM(SALARY) |
+----------+-------------+
| Chaitali |     6500.00 |
| Hardik   |     8500.00 |
| kaushik  |     2000.00 |
| Khilan   |     1500.00 |
| Komal    |     4500.00 |
| Muffy    |    10000.00 |
| Ramesh   |     2000.00 |
+----------+-------------+
7 rows in set (0.03 sec)

MariaDB [testDB]> UPDATE CUSTOMERS  SET NAME = 'Kaushik' WHERE ID = 4;
Query OK, 1 row affected (0.09 sec)
Rows matched: 1  Changed: 1  Warnings: 0

MariaDB [testDB]> SELECT NAME, SUM(SALARY) FROM CUSTOMERS
    ->    GROUP BY NAME;
+---------+-------------+
| NAME    | SUM(SALARY) |
+---------+-------------+
| Hardik  |     8500.00 |
| kaushik |     8500.00 |
| Khilan  |     1500.00 |
| Komal   |     4500.00 |
| Muffy   |    10000.00 |
| Ramesh  |     2000.00 |
+---------+-------------+
6 rows in set (0.00 sec)

MariaDB [testDB]> 
MariaDB [testDB]> SELECT SALARY FROM CUSTOMERS
    ->    ORDER BY SALARY;
+----------+
| SALARY   |
+----------+
|  1500.00 |
|  2000.00 |
|  2000.00 |
|  4500.00 |
|  6500.00 |
|  8500.00 |
| 10000.00 |
+----------+
7 rows in set (0.00 sec)

MariaDB [testDB]> SELECT DISTINCT SALARY FROM CUSTOMERS    ORDER BY SALARY;
+----------+
| SALARY   |
+----------+
|  1500.00 |
|  2000.00 |
|  4500.00 |
|  6500.00 |
|  8500.00 |
| 10000.00 |
+----------+
6 rows in set (0.00 sec)

MariaDB [testDB]> SELECT * FROM CUSTOMERS
    ->    ORDER BY (CASE ADDRESS
    ->    WHEN 'DELHI'  THEN 1
    ->    WHEN 'BHOPAL'  THEN 2
    ->    WHEN 'KOTA'  THEN 3
    ->    WHEN 'AHMADABAD' THEN 4
    ->    WHEN 'MP' THEN 5
    ->    ELSE 100 END) ASC, ADDRESS DESC;
+----+---------+-----+-----------+----------+
| ID | NAME    | AGE | ADDRESS   | SALARY   |
+----+---------+-----+-----------+----------+
|  2 | Khilan  |  25 | Delhi     |  1500.00 |
|  5 | Hardik  |  27 | Bhopal    |  8500.00 |
|  3 | kaushik |  23 | Kota      |  2000.00 |
|  6 | Komal   |  22 | PUNE      |  4500.00 |
|  4 | Kaushik |  25 | Mumbai    |  6500.00 |
|  7 | Muffy   |  24 | Indore    | 10000.00 |
|  1 | Ramesh  |  32 | Ahmedabad |  2000.00 |
+----+---------+-----+-----------+----------+
7 rows in set (0.00 sec)

MariaDB [testDB]> 