import pyodbc

pyodbc.drivers()

conx_string = "Driver={SQL Server}; Server=DESKTOP-0B1B77F; Database=TestDB; Trusted_Connection=yes;"

query = "SELECT FirstName, LastName, AGE FROM TestDB.dbo.Person"

with pyodbc.connect(conx_string) as conx:
    cursor = conx.cursor()
    cursor.execute(query)
    data = cursor.fetchall()

print(data)

print("Your adress book is now ready to start.")

while 1:
    user_input = input("You can choose from the following commands:\n"
                       "'show_contacts' to show all contacts\n"
                       "'search_contact' to search for a specific contact\n"
                       "'update_contact' to update a specific contact\n")
    if user_input == "show_contacts":
        query = "SELECT FirstName, LastName, Age FROM TestDB.dbo.Person"
        with pyodbc.connect(conx_string) as conx:
            cursor = conx.cursor()
            cursor.execute(query)
            data = cursor.fetchall()
        print("There you go:\n")
        for row in data:
            print(f"FIRST NAME: {row.FirstName} LAST NAME: {row.LastName} AGE: {row.Age}")
    if user_input == "search_contact":
        searched_name = input("What person do you search?\n")
        query = "SELECT FirstName FROM TestDB.dbo.Person WHERE FirstName = '%Martin%'"
        with pyodbc.connect(conx_string) as conx:
            cursor = conx.cursor()
            cursor.execute(query)
            data = cursor.fetchall()
        print("There you go:\n")
        for row in data:
            print(f"FIRST NAME: {row.FirstName}")
    else:
        print("hello")



    break