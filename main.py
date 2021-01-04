import pyodbc

pyodbc.drivers()

conx_string = "Driver={SQL Server}; Server=DESKTOP-0B1B77F; Database=TestDB; Trusted_Connection=yes;"

query = "SELECT FirstName, LastName FROM TestDB.dbo.Person"

with pyodbc.connect(conx_string) as conx:
    cursor = conx.cursor()
    cursor.execute(query)
    data = cursor.fetchall()

print(data[:5])

print("Your adress book is now ready to start.")

while 1:
    user_input = input("You can choose from the following commands:\n"
                       "'show_contacts' to show all contacts\n"
                       "'search_contact' to search for a specific contact\n"
                       "'update_contact' to update a specific contact\n")
    if user_input == "show_contacts":
        query = "SELECT FirstName FROM TestDB.dbo.Person"
        with pyodbc.connect(conx_string) as conx:
            cursor = conx.cursor()
            cursor.execute(query)
            data = cursor.fetchall()
        print("There you go:\n")
        print(data)
    else:
        print("hello")



    break