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
	print("option 5")
	print("option 6")
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
	item=Item(name,desc,ID,qty,cost,marg,price)
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

#  item class
class 	Item(	):
	"""	class to handle items"""
	def __init__(self,Name,description,ID,quantity,cost,margin,m_Price):
		super(	Item, self).__init__()
		self.Name = Name
		self.desc = description
		self.ID = int(ID)
		self.qty = int(quantity)
		self.cost = int(cost)
		self.marg = int(margin)
		self.m_Price = int(m_Price)
		if(self.m_Price==0):
			self.price=self.cost+(self.cost*(self.marg/100))	
		else :
			self.price=self.m_Price





			