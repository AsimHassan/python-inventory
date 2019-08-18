import sqlite3
conn=sqlite3.connect('Item.db')
c=conn.cursor()
def create():   
    c.execute("""CREATE TABLE IF NOT EXISTS items(
        ID integer PRIMARY KEY,
        name text,
        desc text,
        cost real,
        qty integer,
        marg integer,
        price real
        )""")

##insertion
def insert_newitem(item):
    with conn:
        c.execute("INSERT INTO items (ID,name, desc, cost, qty, marg, price) VALUES(?,?,?,?,?,?,?)",(item.ID,item.Name,item.desc,item.cost,item.qty,item.marg,item.price))

## deletion
def delete_item(id):
    with conn:
        c.execute("DELETE FROM items WHERE ID = ?",(id,))    


## return all items
def getallitems():
    l=[]
    with conn:
        c.execute("SELECT * FROM items")
        raw=c.fetchall()
        for row in raw :
            l.append(list(row))
    return l
#update data
def updateitem(id,choice,newdata):
    with conn:
        c.execute("UPDATE items SET {} = :newdata WHERE ID = :id".format(choice),{'newdata':newdata,'id':id})


#get data by id
def getitem(id):
    with conn:
        c.execute("SELECT * FROM items WHERE ID=?",(id,))
        raw=c.fetchone()
        l=[]
        for elements in raw:
            l.append(elements)
    return l
