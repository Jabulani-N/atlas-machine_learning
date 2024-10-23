# databases

## MySQL
 * [my first SQL project, featuring some basic setup instructions](https://github.com/Jabulani-N/holbertonschool-higher_level_programming/tree/main/SQL_introduction)

### Install locally MySQL 8.0

```

$  sudo apt-get update
$  sudo apt-get install mysql-server
...
$ mysql -uroot -p
Enter password:
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 21
Server version: 8.0.39-0ubuntu0.20.04.1 (Ubuntu)

Copyright (c) 2000, 2024, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>

```

### How to run MySQL and import a SQL dump

**credentials can be `root/root`**

```

$ service mysql start
 * Starting MySQL database server mysqld                                                                                                                                                                                              [ OK ]
$ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
Enter password: 
$ curl "https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
$ echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
id  name
1   Drama
2   Mystery
3   Adventure
4   Fantasy
5   Comedy
6   Crime
7   Suspense
8   Thriller
$

```
* `hbtn_0d_tvshows` is the name of the example database being used


you can see the fields of table `tablename` inside database `databasename` by using `DESCRIBE tablename;` in mysql. You may need to specify that you want to `USE databasename;` first

### Comments for your SQL file:

```

$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$

```

## MongoDB

### Install locally MongoDB 4.4

[official installation guide](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-ubuntu/)

```

$ wget -qO - https://www.mongodb.org/static/pgp/server-4.4.asc | apt-key add -
$ echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/4.4 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-4.4.list
$ sudo apt-get update
$ sudo apt-get install -y mongodb-org
...
$  sudo service mongod status
mongod start/running, process 3627
$ mongo --version
MongoDB shell version v4.4.29
Build Info: {
    "version": "4.4.29",
    "gitVersion": "f4dda329a99811c707eb06d05ad023599f9be263",
    "openSSLVersion": "OpenSSL 1.1.1f  31 Mar 2020",
    "modules": [],
    "allocator": "tcmalloc",
    "environment": {
        "distmod": "ubuntu2004",
        "distarch": "x86_64",
        "target_arch": "x86_64"
    }
}
$
$ pip3 install pymongo
$ python3
>>> import pymongo
>>> pymongo.__version__
'4.6.2'

```


### How to run MongoDB


```

$ service mongod start
* Starting database mongod                                              [ OK ]
$
$ echo "show dbs" | mongo
MongoDB shell version v4.4.29
connecting to: mongodb://127.0.0.1:27017/?compressors=disabled&gssapiServiceName=mongodb
Implicit session: session { "id" : UUID("e7aec14d-471b-4de2-991b-59c2ae58337f") }
MongoDB server version: 4.4.29
admin   0.000GB
config  0.000GB
local   0.000GB
bye
$

```

### potential errors

Potential issue if documents creation doesn’t work or this error: `Data directory /data/db not found., terminating` ([source](https://bryantson.medium.com/fixing-data-db-not-found-error-in-macos-x-when-starting-mongodb-d7b82abb2479) and [source](https://stackoverflow.com/questions/37702957/mongodb-data-db-not-found))

```
$ sudo mkdir -p /data/db
```

If `mysql -u root -p` results in `ERROR 1698 (28000): Access denied for user 'root'@'localhost'`, try following the steps [here](https://phoenixnap.com/kb/access-denied-for-user-root-localhost)
* for the easiest one, you do
    1. `sudo mysql`
    2. `ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '[password]';`
       * replace `[password]` with your (very secure, please) password

## Task 0. Create a database

Write a script that creates the database `db_0` in your MySQL server.

If the database `db_0` already exists, your script should not fail
You are not allowed to use the SELECT or SHOW statements

File: `1-first_table.sql`


## Task 1. First table

Write a script that creates a table called first_table in the current database in your MySQL server.

first_table description:
id INT
name VARCHAR(256)
The database name will be passed as an argument of the mysql command
If the table first_table already exists, your script should not fail
You are not allowed to use the SELECT or SHOW statements


testing:

```
cat 1-first_table.sql | mysql -hlocalhost -uroot -p db_0; echo "SHOW TABLES;" | mysql -hlocalhost -uroot -p db_0

Enter password:
Enter password:
Tables_in_db_0
first_table

```

## Task 2. List all in table

Write a script that lists all rows of the table first_table in your MySQL server.

All fields should be printed
The database name will be passed as an argument of the mysql command


testing

```
guillaume@ubuntu:~/$ cat 2-list_values.sql | mysql -hlocalhost -uroot -p db_0
Enter password: 
guillaume@ubuntu:~/$ 
```

## Task 3. First add

Write a script that inserts a new row in the table first_table in your MySQL server.

New row:
id = 89
name = Holberton School
The database name will be passed as an argument of the mysql command

testing
```
guillaume@ubuntu:~/$ cat 3-insert_value.sql | mysql -hlocalhost -uroot -p db_0
Enter password: 
guillaume@ubuntu:~/$ cat 2-list_values.sql | mysql -hlocalhost -uroot -p db_0
Enter password: 
id  name
89  Holberton School
guillaume@ubuntu:~/$ cat 3-insert_value.sql | mysql -hlocalhost -uroot -p db_0
Enter password: 
guillaume@ubuntu:~/$ cat 3-insert_value.sql | mysql -hlocalhost -uroot -p db_0
Enter password: 
guillaume@ubuntu:~/$ cat 2-list_values.sql | mysql -hlocalhost -uroot -p db_0
Enter password: 
id  name
89  Holberton School
89  Holberton School
89  Holberton School
guillaume@ubuntu:~/$
```
## Task 4. Select the best

Write a script that lists all records with a score >= 10 in the table second_table in your MySQL server.

Results should display both the score and the name (in this order)
Records should be ordered by score (top first)
The database name will be passed as an argument of the mysql command

## Task 5. Average

Write a script that computes the score average of all records in the table second_table in your MySQL server.

The result column name should be average
The database name will be passed as an argument of the mysql command

testing
```
guillaume@ubuntu:~/$ cat setup.sql
-- Create table and insert data
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);
INSERT INTO second_table (id, name, score) VALUES (1, "Bob", 14);
INSERT INTO second_table (id, name, score) VALUES (2, "Roy", 5);
INSERT INTO second_table (id, name, score) VALUES (3, "John", 10);
INSERT INTO second_table (id, name, score) VALUES (4, "Bryan", 8);

guillaume@ubuntu:~/$ cat setup.sql | mysql -hlocalhost -uroot -p db_0
Enter password: 
guillaume@ubuntu:~/$ cat 5-average.sql | mysql -hlocalhost -uroot -p db_0
Enter password: 
average
9.25
guillaume@ubuntu:~/$ 
```

note to self: essentially, take the average (number) as `average` (column name)

## Task 6. Temperatures #0

[Import](#how-to-run-mysql-and-import-a-sql-dump) in hbtn_0c_0 database [this table dump](./temperatures.sql).

Write a script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).

testing
```
guillaume@ubuntu:~/$ cat 6-avg_temperatures.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
city    avg_temp
Chandler    72.8627
Gilbert 71.8088
Pismo beach 71.5147
San Francisco   71.4804
Sedona  70.7696
Phoenix 70.5882
Oakland 70.5637
Sunnyvale   70.5245
Chicago 70.4461
San Diego   70.1373
Glendale    70.1225
Sonoma  70.0392
Yuma    69.3873
San Jose    69.2990
Tucson  69.0245
Joliet  68.6716
Naperville  68.1029
Tempe   67.0441
Peoria  66.5392
guillaume@ubuntu:~/$
```

~~I did this one assuming the sql script I write should run the provided sql script to create the table in the database~~

### Potential Pitfalls

be sure to actually **do the** [**import**](#how-to-run-mysql-and-import-a-sql-dump) to create the database `hbtn_0c_0` and import the table within.

* in mysql, use `CREATE database IF NOT EXISTS hbtn_0c_0;`, and then in terminal, do `cat temperatures.sql | mysql -hlocalhost -uroot -p hbtn_0c_0`. This will prepare the mysql environment for this task to be completed

descending order

```
ORDER BY [criteria] DESC
```

## Task 7. Temperatures #2
* there is no "Temperatures #1"

Import in `hbtn_0c_0` database this table dump: download (same as Temperatures #0)

Write a script that displays the max temperature of each state (ordered by State name).

testing

```
guillaume@ubuntu:~/$ cat 7-max_state.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
state   max_temp
AZ  110
CA  110
IL  110
guillaume@ubuntu:~/$ 
```
