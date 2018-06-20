from tkinter import *

window = Tk()

window.wm_title("OverTime Keeper")

import OT_BE

def get_selected_row(event):
    global selected_tuple
    index=list1.curselection()[0]
    selected_tuple=list1.get(index)
    e1.delete(0,END)
    e1.insert(END,selected_tuple[1])
    e2.delete(0,END)
    e2.insert(END,selected_tuple[2])
    e3.delete(0,END)
    e3.insert(END,selected_tuple[3])


def Add_command():
    OT_BE.Add(WorkedHours_text.get(),date_text.get(),Duration_Text.get())
    list1.delete(0,END)
    list1.insert(END,(WorkedHours_text.get(),date_text.get(),Duration_Text.get()))

def Remove_command():
    OT_BE.Remove(selected_tuple[0])

def Search_command():
    list1.delete(0,END)
    for row in OT_BE.Search(WorkedHours_text.get(),date_text.get(),Duration_Text.get()):
        list1.insert(END,row)

def Update_command():
    OT_BE.Update(selected_tuple[0],WorkedHours_text.get(),date_text.get(),Duration_Text.get())

def View_command():
    list1.delete(0,END)
    for row in OT_BE.view():
        list1.insert(END,row)


l1 = Label(window,text = "Worked Hours")
l1.grid(row=0,column=0)

l2 = Label(window,text = "Date")
l2.grid(row=0,column=2)

l3 = Label(window,text = "Time")
l3.grid(row=0,column=4)

WorkedHours_text = StringVar()
e1= Entry(window,textvariable=WorkedHours_text)
e1.grid(row = 0, column = 1)

date_text = StringVar()
e2 = Entry(window,textvariable=date_text)
e2.grid(row = 0, column = 3)

Duration_Text = StringVar()
e3 = Entry(window,textvariable = Duration_Text)
e3.grid(row = 0, column = 5)

list1 = Listbox(window, height = 10, width = 40)
list1.grid(row = 1, column = 0, rowspan = 10, columnspan = 3)

sb1 = Scrollbar(window)
sb1.grid(row = 1, column = 3, rowspan = 10)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>', get_selected_row)

b1 = Button(window, text = "     Add      ", command = Add_command)
b1.grid(row = 1, column = 4)

b2 = Button(window, text = "   Remove    ", command = Remove_command)
b2.grid(row = 2, column = 4)

b3 = Button(window, text = "  Update  ",command= Update_command)
b3.grid(row = 3, column = 4)

b4 = Button(window, text = "  Search  ", command = Search_command)
b4.grid(row = 4, column = 4)

b5 = Button(window, text = "  View All  ", command = View_command)
b5.grid(row = 5, column = 4)

b6 = Button(window, text = "   Close   ", command = window.destroy)
b6.grid(row = 6, column = 4)


window.mainloop()
