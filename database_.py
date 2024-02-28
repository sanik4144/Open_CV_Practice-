import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="s@ifull@# @nik",
    database="office"
)
def insertIntoDatabase():
    n = int(input("Enter the number of rows to insert: "))

    while n>0:
        n -= 1
        sqlFormula = "INSERT INTO payment(customer_id, customar, mode, city) VALUES (%s, %s, %s, %s)"

        c_id = input("Enter the id of the customer: ")
        c_name = input("Enter the name of the customer: ")
        c_mode = input("Enter transaction mode: ")
        c_city = input("Enter the city: ")

        cust = (c_id, c_name, c_mode, c_city)

        mycursor.execute(sqlFormula, cust)
        mydb.commit()

        print("Inserted Successfully...")

def showListofTable():
    mycursor.execute("SHOW TABLES")
    for tb in mycursor:
        print(tb)

def showTheWholeTable():
    mycursor.execute("SELECT * FROM payment")
    myresult = mycursor.fetchall()

    for row in myresult:
        print(row)

def searchForIndividualDataset():
    query = int(input("Enter the ID you want to search: "))
    mycursor.execute("SELECT * FROM payment")
    myresult = mycursor.fetchall()

    for row in myresult:
        if row[0] == query:
            print(row)

def searchForIndividualDatasetusingWhere():
    query = input("Enter the mode list you want to see: ")
    sqlFormula2 = "SELECT * FROM payment WHERE mode = %s"
    mycursor.execute(sqlFormula2, (query,))

    myresult = mycursor.fetchall()

    for row in myresult:
        print(row)

def updateAnyDataByTheCustomerID():
    id = int(input("Enter the ID you want to update: "))
    column = input("Enter which column you want to update: ")
    what = input("Enter the updated data: ")

    if column.lower() not in ['customer_id', 'customar', 'mode', 'city']:
        print("Invalid column name!")
    else:
        sqlFormula3 = "UPDATE payment SET {} = %s WHERE customer_id = %s".format(column)
        mycursor.execute(sqlFormula3, (what, id))

        mydb.commit()

def deleteAnyRowByCustomerID():
    id = int(input("Enter the ID you want to delete: "))
    mycursor.execute("SELECT * FROM payment WHERE customer_id = %s", (id,))
    result = mycursor.fetchone()

    if result:
        sqlFormula4 = "DELETE FROM payment WHERE customer_id = %s"
        mycursor.execute(sqlFormula4, (id,))
        mydb.commit()
        print("Record deleted successfully.")
    else:
        print("ID not found in the database.")

mycursor = mydb.cursor()