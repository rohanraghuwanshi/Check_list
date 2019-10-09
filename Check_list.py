from tkinter import *
# importing tkinter
window=Tk()
#window is root window
def get_selected_row(event):
    global selected
    index=check_list.curselection()[0]
    selected=check_list.get(index)
    e2.delete(0,END)
    e2.insert(END,selected)

def add_item():
    task=add_item_text.get()
    with open ("Task.txt",'a+') as t:
        t.write(task)
        t.write('\n')

def show_all_items():
    with open("Task.txt",'r') as t:
        task=t.readlines()
    check_list.delete(0,END)
    for i in task:
        check_list.insert(END,i)


def delete_item():
    td = delete_item_text.get()
    with open("Task.txt",'r') as d:
        x=d.read()
        y=x.splitlines()
        for i in y:
            if i == td:
                y.remove(i)

    with open("Task.txt",'w') as d:
        for i in y:
            d.write(i+'\n')

title=Label(window,text="Check List Application")
title.grid(row=0,column=1)

b1=Button(window,text="Add Item",width=13,command=add_item)
b1.grid(row=1,column=0)

b2=Button(window,text="Delete Item",width=13,command=delete_item)
b2.grid(row=2,column=0)

b3=Button(window,text="Show All Items",width=13,command=show_all_items)
b3.grid(row=3,column=0)

check_list=Listbox(window,height=7,width=92)
check_list.grid(row=6,column=0,rowspan=7,columnspan=4)

check_list.bind('<<ListboxSelect>>',get_selected_row)

sb=Scrollbar(window)
sb.grid(row=4,column=5,rowspan=7)

check_list.configure(yscrollcommand=sb.set)
sb.configure(command=check_list.yview)

add_item_text=StringVar()
e1=Entry(window,textvariable=add_item_text,width=80)
e1.grid(row=1,column=1)

delete_item_text=StringVar()
e2=Entry(window,textvariable=delete_item_text,width=80)
e2.grid(row=2,column=1)

l=Label(window,text="Check List",width=10)
l.grid(row=5,column=1)

window.mainloop()
