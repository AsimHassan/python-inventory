import BLL
def switch(choice):
    if choice=='1':
        BLL.create()
    else:
        print("no choice")


choice=BLL.show_menu()
switch(choice)