#This Project is to Est. connection with DB, create tables and Add data in postgresDB through python:

#1. Import Package and its dependencies and Check Connection:
import psycopg2
from psycopg2 import extensions
print("Hi!! Welcome to Managing PostgresDb using python Project.\n")

#Check Connection:
def check_conn(name):
    print("Checking Connection...\n")
    connect = psycopg2.connect(dbname=name, user="postgres", password="admin", host="localhost", port="5432")
    print("DB Connection Successful and Working!!\n")

#2. Defining Functions:

#a) CREATE DATABASE:
def create_db():

# 1.Establishing Connection::
    connect = psycopg2.connect(dbname="postgres", user="postgres", password="admin", host="localhost", port="5432")
# 2. Set Autocommit using extension module in psycopg2(2.9.x):
    connect.set_isolation_level(extensions.ISOLATION_LEVEL_AUTOCOMMIT)
# 3. Create cursor object:
    cursor = connect.cursor()
    name=input("Enter name of DB to create: ")
    print("Creating DB....\n")
    cursor.execute(f'''CREATE DATABASE {name};''')
    print("DATABASE with name '{}' Create Successfully\n".format(name))
    connect.close()
    return name

#b) Create TABLE inside created DB:
def create_table(name):
    print("Creating Table.....")
# 1.Establishing Connection::
    connect = psycopg2.connect(dbname=name, user="postgres", password="admin", host="localhost", port="5432")

# 2. Set Autocommit using extension module in psycopg2(2.9.x):
    connect.set_isolation_level(extensions.ISOLATION_LEVEL_AUTOCOMMIT)
# 3. Create cursor object:
    cursor = connect.cursor()
# 4. Create table named employees with multiple column:
    cursor.execute('''create table employee(Name text, ID_num int, Age int);''')
    print("Table Created Successfully with name Employee in DB {}\n".format(name))
    connect.close()

#c) Insert Contents inside created TABLE:
def insert_table(name):
# 1.Establishing Connection::
    connect = psycopg2.connect(dbname=name, user="postgres", password="admin", host="localhost", port="5432")

# 2. Set Autocommit using extension module in psycopg2(2.9.x):
    connect.set_isolation_level(extensions.ISOLATION_LEVEL_AUTOCOMMIT)
# 3. Create cursor object:
    cursor = connect.cursor()
# 4. Add multiple elements:
    num=input("How many employee data details you want to Enter: ")
    for i in range(0,int(num)):
        emp_name=input("Enter Name of employee: ")
        emp_id=input("Enter ID Number of employee: ")
        emp_age=input("Enter Age of employee: ")
        query='''insert into employee(Name, ID_num, Age) values(%s, %s, %s);'''
        cursor.execute(query,(emp_name,emp_id,emp_age))
        print("\n")
    print("Inserting Elements...\n")
    print("Elements Inserted Successfully in Table Employee associated with DB {}\n".format(name))
    connect.close()
#d). Delete DB:
def delete_db(name):
    print("Deleting DB....\n")
# 1.Establishing Connection::
    connect = psycopg2.connect(dbname="postgres", user="postgres", password="admin", host="localhost", port="5432")
# 2. Set Autocommit using extension module in psycopg2(2.9.x):
    connect.set_isolation_level(extensions.ISOLATION_LEVEL_AUTOCOMMIT)
# 3. Create cursor object:
    cursor = connect.cursor()
    cursor.execute(f'''drop database {name};''')
    print("DATABASE with name '{}' Deleted Successfully\n".format(name))
    connect.close()

#6. CALL FUNCTION:
choice=input("If you want to create new DB, if so write 'Yes' else write 'No': ")
if choice=="No":
    name_db=input("Enter DB name you want to Connect: ")
else:
    db_name=create_db()
    name_db=db_name
check_conn(name_db)
create_table(name_db)
insert_table(name_db)
choice=input("Do you want to delete the DB,'Yes'/'No': ")
if choice=="Yes":
    del_db=input("Enter the name DB to delete: ")
    delete_db(del_db)
    print("Thanks for Participating!!BYE!!")
else:
    print("Thanks for Participating!!BYE!!")

