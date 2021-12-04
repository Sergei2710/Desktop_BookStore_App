"""
A program that stores this book information:
Title, Author
Year, ISBN

User can:
View all records
Search and entry
Add entry
Update entry
Delete
Close
"""

from tkinter import *
import backend

#Commands:
def get_selected_row(event):
    try:
        global selected_tuple
        index=display_window.curselection()[0]
        selected_tuple=display_window.get(index)
        e_title.delete(0,END)
        e_title.insert(END,selected_tuple[1])
        e_author.delete(0,END)
        e_author.insert(END,selected_tuple[2])
        e_year.delete(0,END)
        e_year.insert(END,selected_tuple[3])
        e_isbn.delete(0,END)
        e_isbn.insert(END,selected_tuple[4])
    except IndexError:
        pass

def view_command():
    display_window.delete(0,END)
    for row in backend.view():
        display_window.insert(END, row)

def search_command():
    display_window.delete(0,END)
    for row in backend.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        display_window.insert(END,row)

def add_command():
    backend.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    display_window.delete(0,END)
    display_window.insert(END,(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))

def delete_command():
    backend.delete(selected_tuple[0])

def update_command():
    backend.update(selected_tuple[0],title_text.get(), author_text.get(), year_text.get(), isbn_text.get())


window=Tk()

window.wm_title("BookStore")

#Labels
l_title=Label(window, text="Title")
l_title.grid(row=0,column=0)

l_author=Label(window, text="Author")
l_author.grid(row=0,column=2)

l_year=Label(window, text="Year")
l_year.grid(row=1,column=0)

l_isbn=Label(window, text="ISBN")
l_isbn.grid(row=1,column=2)

#Entries
title_text=StringVar()
e_title=Entry(window,textvariable=title_text)
e_title.grid(row=0,column=1)

author_text=StringVar()
e_author=Entry(window,textvariable=author_text)
e_author.grid(row=0,column=3)

year_text=StringVar()
e_year=Entry(window,textvariable=year_text)
e_year.grid(row=1,column=1)

isbn_text=StringVar()
e_isbn=Entry(window,textvariable=isbn_text)
e_isbn.grid(row=1,column=3)

#Display window
display_window=Listbox(window, height=6, width=35)
display_window.grid(row=2,column=0,rowspan=6,columnspan=2)

scroll_bar=Scrollbar(window)
scroll_bar.grid(row=2,column=2,rowspan=6)

display_window.configure(yscrollcommand=scroll_bar.set)
scroll_bar.configure(command=display_window.yview)

display_window.bind('<<ListboxSelect>>', get_selected_row)

#Buttons
b_view=Button(window,text="View all", width=12, command=view_command)
b_view.grid(row=2,column=3)

b_search=Button(window,text="Search entry", width=12, command=search_command)
b_search.grid(row=3,column=3)

b_add=Button(window,text="Add entry", width=12, command=add_command)
b_add.grid(row=4,column=3)

b_update=Button(window,text="Update", width=12, command=update_command)
b_update.grid(row=5,column=3)

b_delete=Button(window,text="Delete", width=12, command=delete_command)
b_delete.grid(row=6,column=3)

b_close=Button(window,text="Close", width=12, command=window.destroy)
b_close.grid(row=7,column=3)


window.mainloop()