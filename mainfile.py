import BLL
import database_test
import os
def clear():
    input()
    os.system('cls')
def switch(choice):
    if choice=='1':
        BLL.insert()
    elif choice=='2':
        BLL.show_items()
    elif choice=='3':
        BLL.delete_itembyid()
    elif choice=='4':
        BLL.updatebyid()
    elif choice=='5':
        BLL.sellitembyid()
    elif choice=='6':
        BLL.buyitembyid()
    elif choice=='7':
        BLL.show_sale()
    elif choice=='8':
        BLL.show_purchase()
    else:
        print("no choice")

database_test.create()
while(True):
    BLL.show_items()
    choice=BLL.show_menu()
    if choice =="exit":
        clear()
        exit(1)
    switch(choice)
    clear()


