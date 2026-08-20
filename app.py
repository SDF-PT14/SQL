# In this file Python will now be responsible for sending the SQL commands 
import sqlite3
import pandas as pd 

#connect to database
connection=sqlite3.connect("shop.db")
# create a cursor: execute the SQL commands
cursor=connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS products(id INTEGER PRIMARY KEY,
name TEXT,
category TEXT, 
price REAL)
""")
connection.commit()

# cursor.execute("""
# INSERT INTO products(name,category,price)
# VALUES('Laptop','Electronics',850)
# """)

# cursor.execute("""
# INSERT INTO products(name,category,price)
# VALUES('Keyboard','Accessories',200)
# """)
# cursor.execute("""
# INSERT INTO products(name,category,price)
# VALUES('USB','Accessories',20)
# """)
# cursor.execute("""
# INSERT INTO products(name,category,price)
# VALUES('Desk','Furniture',150)
# """)
# connection.commit()

# cursor.execute("SELECT * FROM products WHERE category='Accessories'")


# cursor.execute("""
# ALTER TABLE products ADD COLUMN stock INTEGER
# """)
# connection.commit()
# cursor.execute("""
# UPDATE products SET stock=10 where id=1
# """)
# cursor.execute("""
# UPDATE products SET stock=25 where id=2
# """)
# cursor.execute("""
# UPDATE products SET stock=30 where id=3
# """)
# cursor.execute("""
# UPDATE products SET stock=15 where id=4
# """)
# connection.commit()

# cursor.execute("SELECT * FROM products")
# products=cursor.fetchall()

# # print(products)
# for product in products:
# 	print(product)
#PAndas
#DataFrame=table in SQL

# query="""
# SELECT * FROM products
# """
# df=pd.read_sql_query(query,connection)
# print(df)
# # GROUP BY = PUT rows with the same value together 

# query="""
# SELECT category, COUNT(*) AS total_products
#  FROM products GROUP BY category

# """
# df=pd.read_sql_query(query,connection)
# print(df)

# query="""
# SELECT category,AVG(price) AS average_price
#  FROM products GROUP BY category

# """
# df=pd.read_sql_query(query,connection)
# print(df)

# query="""
# SELECT category, SUM(stock) AS total_stock
#  FROM products GROUP BY category

# """
# df=pd.read_sql_query(query,connection)
# print(df)

#Having
# query="""
# SELECT category, COUNT(*) AS total_products
#  FROM products GROUP BY category
#  HAVING COUNT(*)>=3

# """
# df=pd.read_sql_query(query,connection)
# print(df)

# query="""
# SELECT category,AVG(price) AS average_price
#  FROM products GROUP BY category
#  HAVING AVG(price)>100
#  """
# df=pd.read_sql_query(query,connection)
# print(df)

query="""
SELECT name,price FROM products 
ORDER BY price ASC
"""
df=pd.read_sql_query(query,connection)
print(df)

query="""
SELECT name,price FROM products 
ORDER BY price DESC
"""
df=pd.read_sql_query(query,connection)
print(df)

query="""
SELECT category,AVG(price) AS average_price
 FROM products GROUP BY category
 ORDER BY average_price DESC
 """
df=pd.read_sql_query(query,connection)
print(df)

query="""
SELECT category,AVG(price) AS average_price
 FROM products GROUP BY category
 HAVING AVG(price)>100
 ORDER BY average_price ASC
 """
df=pd.read_sql_query(query,connection)
print(df)


#LIMIT
q="""
SELECT * FROM products 
LIMIT 2

"""
df=pd.read_sql_query(q,connection)
print(df)

query="""
SELECT name,price FROM products 
ORDER BY price DESC
LIMIT 4

"""
df=pd.read_sql_query(query,connection)
print(df)

query="""
SELECT name,price,category FROM products 
WHERE category='Accessories'
ORDER BY price DESC
LIMIT 2

"""
df=pd.read_sql_query(query,connection)
print(df)