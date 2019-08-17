import sqlite3
conn=sqlite3.connect(':memory:')
c=conn.cursor()
def create():   
    c.execute("""CREATE TABLE IF NOT EXISTS items(
        ID integer PRIMARY KEY,
        name text,
        desc text,
        cost real,
        qty integer,
        marg integer,
        price reals
        )""")
def insert_newitem(item):
    with conn:
        c.execute("INSERT INTO items (ID,name, desc, cost, qty, marg, price) VALUES(?,?,?,?,?,?,?)",(item.ID,item.Name,item.desc,item.cost,item.qty,item.marg,item.price))
