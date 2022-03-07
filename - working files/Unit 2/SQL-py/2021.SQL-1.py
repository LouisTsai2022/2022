import sqlite3

#connect to the database
con = sqlite3.connect("datastore/rockyconcrete.db")

#create a cursor/pointer to navigate the datebase
con.row_factory = sqlite3.Row #enables us to use coluan headings
cur = con.cursor() #is the pointer to use in the database

# sql = """
#         select *
#         from customers
#         where town = 'Brisbane';"""
#
# cur.execute(sql)
# results = cur.fetchall()
#
# print(type(results))
# print(results)
#
# if len(results) > 0:
#     for row in results:
#         print(row['cust_name'], 'lives in', row['street'], 'in', row['town'])
# else:
#     print('NO RECORDS FOUND')


# parameter query
town = input("Enter the town to search for: ")
min_cr = int(input("Enter the minimum credit limit: "))

sql = """
        select * 
        from customers
        where town like ? 
        and cr_limit >= ?;"""

cur.execute(sql,('%'+town+'%',min_cr))
results = cur.fetchall()

if len(results) > 0:
    for row in results:
        print(row['cust_name'], 'lives in', row['street'], 'in', row['town'], 'credit limit:', row['cr_limit'])
else:
    print('NO RECORDS FOUND')