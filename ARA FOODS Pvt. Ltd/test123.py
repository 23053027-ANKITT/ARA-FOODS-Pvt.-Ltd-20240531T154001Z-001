from tkinter import *

root = Tk()
root.geometry("400x400")

def update(data):
    my_list.delete(0, END)
    
    for item in data:
        my_list.insert(END, item)

def fillout(e):
    my_entry.delete(0, END)

    my_entry.insert(0, my_list.get(ACTIVE))

def check(e):
    typed = my_entry.get()

    if typed == '':
        data = toppings
    else:
        data = []
        for item in toppings:
            if typed.lower() in item.lower():
                data.append(item)
                
    update(data)
    
my_label = Label(root, text = "Start typing...", fg = 'grey')
my_label.pack(pady=20)

my_entry = Entry(root)
my_entry.pack()

my_list = Listbox(root, width = 50)
my_list.pack(pady=40)


toppings = ["Pepperoni", "Peppers", "Mushrooms", "Cheese", "Onions", "Ham", "Taco"]

update(toppings)


my_list.bind("<<ListboxSelect>>", fillout)

my_entry.bind("<KeyRelease>", check)

root.mainloop()
