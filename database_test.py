import sqlite3
conn=sqlite3.connect('Item.db')
c=conn.cursor()
def create():   
    with conn:
        c.execute("""CREATE TABLE IF NOT EXISTS items(
            ID integer PRIMARY KEY,
            name text,
            desc text,
            cost real,
            qty integer,
            marg integer,
            price real
            )""")
        c.execute("""CREATE TABLE IF NOT EXISTS sale_report(
            ID INTEGER PRIMARY KEY,
            date TEXT,
            time TEXT,
            action TEXT
            )""")

        c.execute("""CREATE TABLE IF NOT EXISTS purchase_report(
            ID INTEGER PRIMARY KEY,
            date TEXT,
            time TEXT,
            action TEXT
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
def getallitems(ref):
    l=[]
    with conn:
        c.execute("SELECT * FROM {}".format(ref))
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
#sale report--------
def updatesale(id,units,name):
        with conn:
            c.execute("INSERT INTO sale_report (date,time,action) VALUES(DATE('now'),TIME('now'),?)",("sold {} units of {} with item id {}".format(units,name,id),))
#purchase report------
def updatepurchase(id,units,name):
        with conn:
            c.execute("INSERT INTO purchase_report (date,time,action) VALUES(DATE('now'),TIME('now'),?)",("purchased {} units of {} with item id {}".format(units,name,id),))


