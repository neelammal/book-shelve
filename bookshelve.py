from tkinter import *
import back

def get_selected_row(event):
    global selected_tuple
    index=lt.curselection()[0]
    selected_tuple=lt.get(index)
    d.delete(0,END)
    d.insert(END,selected_tuple[1])
    d1.delete(0,END)
    d1.insert(END,selected_tuple[2])
    d2.delete(0,END)
    d2.insert(END,selected_tuple[3])
    d3.delete(0,END)
    d3.insert(END,selected_tuple[4])


    
    return(selected_tuple)


def view_command():
    lt.delete(0,END)
    for row in back.view():
        lt.insert(END,row)


def search_command():
      lt.delete(0,END)
      for row in back.search(x.get(),y.get(),z.get(),x1.get()):
          lt.insert(END,row)


def add_entry():
    lt.delete(0,END)
    back.insert(x.get(),y.get(),z.get(),x1.get())
    lt.insert(END,(x.get(),y.get(),z.get(),x1.get()))



def update_selected():
     back.update(selected_tuple[0],x.get(),y.get(),z.get(),x1.get())



def delete_selected():
    back.delete(selected_tuple[0])


    
    
w=Tk()

w.title("book shelve")

l1=Label(w,text="title")
l1.grid(row=0,column=0)

l2=Label(w,text="year")
l2.grid(row=1,column=0)

l3=Label(w,text="author")
l3.grid(row=0,column=2)

l4=Label(w,text="isdn")
l4.grid(row=1,column=2)        

x=StringVar()
d=Entry(w,textvariable=x)
d.grid(row=0,column=1)

y=StringVar()
d1=Entry(w,textvariable=y)
d1.grid(row=0,column=3)

z=StringVar()
d2=Entry(w,textvariable=z)
d2.grid(row=1,column=1)

x1=StringVar()
d3=Entry(w,textvariable=x1)
d3.grid(row=1,column=3)

lt=Listbox(w,height=6,width=35)
lt.grid(row=2,column=0,rowspan=6, columnspan=2)

sc=Scrollbar(w)
sc.grid(row=2,column=2,rowspan=6)
lt.configure(yscrollcommand=sc.set)
sc.configure(command=lt.yview)

lt.bind('<<ListboxSelect>>',get_selected_row)


b1=Button(w,text="view all",width=12,command=view_command)
b1.grid(row=2,column=3)
b2=Button(w,text="search entry",width=12,command=search_command)
b2.grid(row=3,column=3)

b3=Button(w,text="add entry",width=12,command=add_entry)
b3.grid(row=4,column=3)
b4=Button(w,text="update selected",height=1,width=12,command=update_selected)
b4.grid(row=5,column=3)
b5=Button(w,text="delete selected",height=1,width=12,command=delete_selected)
b5.grid(row=6,column=3)
b6=Button(w,text="close",height=1,width=12,command=w.destroy)
b6.grid(row=7,column=3)

w.mainloop()
