import sqlite3

#connect to the database
con = sqlite3.connect("datastore/rockyconcrete.db")

#create a cursor/pointer to navigate the database
con.row_factory = sqlite3.Row #enables us to use column headings
cur = con.cursor() #is the pointer to use in the database

name = input("Enter customer name: ")

sql = """
        select cust_name, cust_no, cr_limit-curr_bal as 'available'
        from customers
        where cust_name like ?;"""

cur.execute(sql,('%'+name+'%',))
results = cur.fetchall()

for row in results:

    sql = """
            select max(order_no) as 'order_no', max(order_date) as 'order_date'
            from orders
            where cust_no = ?;"""

    cur.execute(sql,(row['cust_no'],))
    result = cur.fetchone()

    if not result:
        result = 'No Orders Made'
    else:
        result = "last order number " + str(result['order_no'])
    print(row['cust_no'], '-', row['cust_name'], 'has available', row['available'], result)
