import BLL
import database_test
import os
def clear():
    input()
    os.system('cls')
def switch(choice):
    if choice=='1':
        BLL.insert()
        clear()

    elif choice=='2':
        BLL.show_items()
    elif choice=='3':
        BLL.delete_itembyid()
        clear()
    elif choice=='4':
        BLL.updatebyid()
        clear()

    else:
        print("no choice")

database_test.create()
while(True):
    choice=BLL.show_menu()
    if choice =="exit":
        exit(1)
    switch(choice)