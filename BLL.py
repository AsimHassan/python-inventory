import database_test
def show_menu():
	print("insert")
	print("option 2")
	print("option 3")
	print("option 4")
	print("option 5")
	print("option 6")
	choice = input()
	return choice
def create():
	database_test.create()
	print("create menu")
	ID = input('enter ID:')
	name=input('enter name:')
	desc=input('enter description:')
	cost = input('enter cost:')
	qty=input('enter quantity:')
	marg=input('enter margin:')
	price=input('enter price:')	
	item=Item(name,desc,ID,qty,cost,marg,price)
	database_test.insert_newitem(item)



def context():
	print("Name\tdescription\t\tID\tquantity\tcost\tmargin\tprice")





def pretify(data):
	pass


class 	Item(	):
	"""	class to handle items"""
	def __init__(self,Name,description,ID,quantity,cost,margin,m_Price):
		super(	Item, self).__init__()
		self.Name = Name
		self.desc = description
		self.ID = ID
		self.qty = quantity
		self.cost = cost
		self.marg = margin
		self.m_Price = m_Price
		if(m_Price==0):
			self.price=cost+(cost*self.marg)	
		else :
			self.price=self.m_Price

	def 	show_items(self	):
			l=[self.Name,self.desc,str(self.ID),str(self.qty),str(self.cost),str(self.marg),str(self.price)]
			pretify(l)





			