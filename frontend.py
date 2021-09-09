from tkinter import *
import backend

window = Tk()
window.configure(bg='black')
window.wm_title("BookStore")

p1 = PhotoImage(file = './icon/icon.png')
window.iconphoto(False, p1)


def view_command():
    lb.delete(0,END)
    for row in backend.view():
        lb.insert(END, row)

def search_command():
    lb.delete(0, END)
    for row in backend.search(title=title_text.get(), author=author_text.get(), year=year_text.get(), isbn=isbn_text.get()):
        lb.insert(END, row)

def delete_command():
    backend.delete(lb.get(lb.curselection()[0])[0])
    lb.delete(0,END)
    for row in backend.view():
        lb.insert(END, row)

def insert_command():
    backend.insert(str(title_text.get()), str(author_text.get()), int(year_text.get()), int(isbn_text.get()))
    lb.delete(0,END)
    for row in backend.view():
        lb.insert(END, row)

def update_command():
    row = lb.get(lb.curselection()[0])
    backend.update(row[0],
    title_text.get() if title_text.get() else row[1],
    author_text.get() if author_text.get() else row[2],
    year_text.get() if year_text.get() else row[2],
    isbn_text.get() if isbn_text.get() else row[3])
    lb.delete(0,END)
    for row in backend.view():
        lb.insert(END, row)


#           TITLE

l1 = Label(window, text="Title", width=18, fg='whitesmoke', bg='black')
l1.grid(row=0, column=0)

title_text = StringVar()
e1 = Entry(window, width=18, bg='black', border=1, textvariable=title_text, fg='grey', insertbackground='white')
e1.grid(row=0, column=1)


#        AUTHOR

l2 = Label(window, text="Author", width=18, fg='whitesmoke', bg='black')
l2.grid(row=0, column=2)

author_text = StringVar()
e2 = Entry(window, width=18, bg='black', border=1, textvariable=author_text, fg='grey', insertbackground='white')
e2.grid(row=0, column=3)


#         YEAR 

l3 = Label(window, text="Year", width=18, fg='whitesmoke', bg='black')
l3.grid(row=1, column=0)

year_text = StringVar()
e3 = Entry(window, width=18, bg='black', border=1, textvariable=year_text, fg='grey', insertbackground='white')
e3.grid(row=1, column=1)


#           ISBN

l4 = Label(window, text="ISBN", width=18, fg='whitesmoke', bg='black')
l4.grid(row=1, column=2)

isbn_text = StringVar()
e4 = Entry(window, width=18, bg='black', border=1, textvariable=isbn_text, fg='grey', insertbackground='white')
e4.grid(row=1, column=3)


#        LIST BOX

lb = Listbox(window, width=30, height=6)
lb.grid(row=2, column=0, columnspan=2, rowspan=6)


#    SCROLL BAR

sb = Scrollbar(window, bg='black')
sb.grid(row=2, column=2, rowspan=6)


#     VIEW ALL

b1 = Button(window, width=13, text="View All", bg='black', fg='grey', border=0, command=view_command)
b1.grid(row=2, column=3)

#     search entry

b2 = Button(window, width=13, text="Search Entry", bg='black', fg='grey', border=0, command=search_command)
b2.grid(row=3, column=3)


#    ADD ENTRY

b3 = Button(window, width=13, text="Add Entry", bg='black', fg='grey', border=0, command=insert_command)
b3.grid(row=4, column=3)


#     UPDATE
b4 = Button(window, width=13, text="Update", bg='black', fg='grey', border=0, command=update_command)
b4.grid(row=5, column=3)


#     DELETE

b5 = Button(window, width=13, text="Delete", bg='black', fg='grey', border=0, command=delete_command)
b5.grid(row=6, column=3)

#     CLOSE

b6 = Button(window, width=13, text="Close", bg='black', fg='grey', border=0, command=window.destroy)
b6.grid(row=7, column=3)

window.mainloop()