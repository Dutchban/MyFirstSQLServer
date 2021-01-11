import pyodbc

pyodbc.drivers()

conx_string = "Driver={SQL Server}; Server=DESKTOP-0B1B77F; Database=TestDB; Trusted_Connection=yes;"

query = "SELECT FirstName, LastName, AGE FROM TestDB.dbo.Person"

with pyodbc.connect(conx_string) as conx:
    cursor = conx.cursor()
    cursor.execute(query)
    data = cursor.fetchall()

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
            print(f"FIRST NAME: {row.FirstName} LAST NAME: {row.LastName} AGE: {row.Age}\n")
    if user_input == "search_contact":
        searched_name = input("What person do you search?\n")
        query = "SELECT FirstName, LastName FROM TestDB.dbo.Person WHERE FirstName LIKE ?"
        with pyodbc.connect(conx_string) as conx:
            cursor = conx.cursor()
            cursor.execute(query, searched_name)
            data = cursor.fetchall()
        print("There you go:")
        for row in data:
            print(f"FIRST NAME: {row.FirstName} {row.LastName}\n")
    if user_input == "update_contact":
        searched_name = input("What person do you want to update?\n")
        query = "SELECT FirstName, LastName FROM TestDB.dbo.Person WHERE FirstName LIKE ?"
        with pyodbc.connect(conx_string) as conx:
            cursor = conx.cursor()
            cursor.execute(query, searched_name)
            data = cursor.fetchall()
        print("Okay, you update the following contact")
        for row in data:
            print(f"FIRST NAME: {row.FirstName} {row.LastName}\n")
        updated_info = input("What do you want to update? Enter: FirstName, LastName or Age\n").lower()
        if updated_info == "lastname":
            new_info = input("Okay, what should the new LastName be?\n")
            with pyodbc.connect(conx_string) as conx:
                cursor = conx.cursor()
                cursor.execute("UPDATE TestDB.dbo.Person SET LastName = ? WHERE FirstName = ?", (new_info, searched_name))
                conx.commit()
            print("Okay, done")
        if updated_info == "firstname":
            new_info = input("Okay, what should the new FirstName be?\n")
            with pyodbc.connect(conx_string) as conx:
                cursor = conx.cursor()
                cursor.execute("UPDATE TestDB.dbo.Person SET FirstName = ? WHERE FirstName = ?", (new_info, searched_name))
                conx.commit()
            print("Okay, done")
        if updated_info == "age":
            new_info = input("Okay, what should the new Age be?\n")
            with pyodbc.connect(conx_string) as conx:
                cursor = conx.cursor()
                cursor.execute("UPDATE TestDB.dbo.Person SET Age = ? WHERE FirstName = ?", (new_info, searched_name))
                conx.commit()
            print("Okay, done")

