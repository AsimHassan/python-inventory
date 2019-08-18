import database_test
from tabulate import tabulate


head=['ID','Name','description','cost','quantity','margin','price']
head2=['ID','name','desc','cost','qty','marg','price']

# function to display menu on screen
def show_menu():
	print("1:insert")
	print("2:show")
	print("3:delete")
	print("4:update")
	print("5:Sell")
	print("6:buy")
	print("")
	choice = input("enter your choice:  ")
	return choice


# insert function
def insert():
	print("Insert menu")
	ID = input('enter ID:')
	name=input('enter name:')
	desc=input('enter description:')
	cost = input('enter cost:')
	qty=input('enter quantity:')
	marg=input('enter margin:')
	price=input('enter price:')	
	l=[ID,name,desc,cost,qty,marg,price]
	item=Item(l)
	database_test.insert_newitem(item)

#function to show all items in table
def show_items():
	allitems=database_test.getallitems()
	print(tabulate(allitems,headers=head ))
	print("\n\n")

#function to delete item by id
def delete_itembyid():
	id = input("enter id of item to be deleted")
	database_test.delete_item(id)
	print("item no:{} deleted".format(id))

#function to update an item by id
def	updatebyid():
	id=input('enter id of item to be updated')
	choice=int(input("""select a parameter to update::
1:Name
2:description
3:cost
4:quantity:
5:margin
6:price
	:"""))
	newvalue=input("enter new {}  :  ".format(head[choice]))
	database_test.updateitem(id,head2[choice],newvalue)
	print("data updated")


#function to sell items
def sellitembyid():
	id=input("enter id of sold:")
	units=input("enter unit sold")
	l=database_test.getitem(id)
	itemsold=Item(l)
	itemsold.sell(units)

# function to buy items

def buyitembyid():
	id=input("enter id of item purchased:")
	units=input("enter unit purchased:")
	l=database_test.getitem(id)
	itembuy=Item(l)
	itembuy.buy(units)



#  item class
class 	Item(	):
	"""	class to handle items"""
	def __init__(self,l):
		super(	Item, self).__init__()
		self.ID = int(l[0])
		self.Name = l[1]
		self.desc = l[2]
		self.cost = int(l[3])
		self.qty = int(l[4])
		self.marg =int( l[5])
		self.m_Price = float(l[6])
		if(self.m_Price==0):
			self.price=self.cost+(self.cost*(self.marg/100))	
		else :
			self.price=self.m_Price
		if(self.marg==0):
			self.marg=(self.price-self.cost)*100/self.cost
	def sell(self,units):
		self.qty=self.qty-int(units)
		database_test.updateitem(self.ID,'qty',self.qty)
		print("database updated with sale")

	

	def buy(self,units):
		self.qty=self.qty+int(units)
		database_test.updateitem(self.ID,'qty',self.qty)
		print("database updated with purchase")


			