import sqlite3

#connect to the database
con = sqlite3.connect("datastore/rockyconcrete.db")

#create a cursor/pointer to navigate the database
con.row_factory = sqlite3.Row #enables us to use column headings
cur = con.cursor() #is the pointer to use in the database

def menu():
#present the menu
    print("Enter the number from the following options:")
    print("1 - Get Customer Details")
    print("2 - Get Order Details")
    print("3 - Get Product Details")
    print("4 - Quit")
    print()
    c = int(input("Enter your choice"))
    return c

choice = menu()

while choice not in (1, 5): # choice 1 to 5
    print("Error: Enter a number from 1 to 4!")
    choice = menu()

while choice != 4:
    if choice == 1:
        sql = """
                select *
                from customers
                where cust_name like = ?
                order by cust_name asc;"""

        name = input("Enter a customers name: ")
        cur.execute(sql,('%'+name+'%',))
        results = cur.fetchall()
        for row in results:
            print(row['cust_no'], row['cust_name'], row['town'], row['cr_limit'])

    elif choice == 2:
        sql = """
                        select *
                        from orders
                        where order_no like = ?
                        order by order_no asc;"""

        orders = input("Enter an order number: ")
        cur.execute(sql, ('%'+orders+'%',))
        results = cur.fetchall()
        for row in results:
            print(row['order_no'], row['order_date'], row['cust_no'])

    elif choice == 3:
        sql = """
                        select *
                        from products
                        where description like = ?;"""

        product = input("Enter a customers name: ")
        cur.execute(sql, ('%' + product + '%',))
        results = cur.fetchall()
        for row in results:
            print(row['prod_code'], row['description'], row['qty_on_hand'], row['list_prise'])


    choice = menu()

print("Goodbye")
