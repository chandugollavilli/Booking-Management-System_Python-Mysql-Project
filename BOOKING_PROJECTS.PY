import mysql.connector
booking_project = mysql.connector.connect(

    host = "localhost",
    user = "root",
    password = "Chandu@123",
    database = "booking_project"

)

# print(booking_project) 
# booking_data = booking_project.cursor()

# booking_data.execute("CREATE DATABASE booking_project")
# booking_data.execute("CREATE TABLE CHECK_IN (Days VARCHAR(200), Name VARCHAR(200), Aadhaar VARCHAR(200), Date VARCHAR(200), TypeNumber VARCHAR(200))")
# booking_data.execute("CREATE TABLE CHECK_OUT(TypeNumber VARCHAR(200), Guests INT, Fare INT, Days INT, Tbill INT, Date VARCHAR(200))")
# booking_project.commit()


#----------------------------------------Programming-------------------------------------------#

def checkin():
    d = input("Days: ")
    n = input("Name: ")
    a = input("Aadhaar: ")
    dt = input("Date: ")
    rn = input("Room Number: ")
    data = (d,n,a,dt,rn)
    sql = "INSERT INTO check_in values(%s,%s,%s,%s,%s)"
    book_data = booking_project.cursor()
    book_data.execute(sql,data)
    booking_project.commit()
    print("Data Entered Sucessfully")
    main()

def checkout():
    rn = input("Room Number: ")
    g = int(input("Guests: "))
    p = int(input("price: "))
    d = int(input("Days: "))
    bl = p*d*g
    dt = input("Date: ")
    data = (rn,g,p,d,bl,dt)
    sql = "INSERT INTO check_out values(%s,%s,%s,%s,%s,%s)"
    book_data = booking_project.cursor()
    book_data.execute(sql,data)
    booking_project.commit()
    print("Data Entered Sucessfully")
    main()

def bill():
    bill = input("Room No: ")
    tbill = (bill,)
    sql = "SELECT Tbill From check_out WHERE RoomNumber = %s"
    book_data = booking_project.cursor()
    book_data.execute(sql,tbill)
    data = book_data.fetchone()
    for i in data:
        print('\nTbill to pay:',i)
    main()

def rooms():
    print("Executive -5000/d/g")
    print(" ")
    print("""Facilities - Wifi , TV , AC , Bathroom With Tub and Geyser, Breakfast, lunch , dinner""")
    print(" ")
    print("Deluxe - 2500/d/g")
    print(" ")
    print("""Facilities - Wifi , TV , AC , Bathroom With Tub and Geyser""")
    print(" ")
    print("Simple - 1000/d/g")
    print(" ")
    main()

def main():
    print("""
    1.Check In
    2.Check Out
    3.Bill to pay
    4.Avaliable Rooms & Packages
    """)
    select = int(input("Choice: "))
    if select == 1:
        checkin()
    elif select == 2:
        checkout()
    elif select == 3:
        bill()
    elif select == 4:
        rooms()
    else:
        print("Enter Correct Chocie")
    main()
main()




