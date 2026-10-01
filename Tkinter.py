import tkinter as tk


def answer():
    print("answer")

def callback():
    print("callback")


def clickHandler(first:StringVar,last:StringVar,phone:StringVar,major:StringVar):
    print(first,last,phone,major)

root = Tk()

frm = tk.Frame(root, padding = 10)
frm.grid()

tk.Label(frm, text = "First Name").grid(column = 0, row = 0)
strFirst = StringVar()
tk.Entry(frm, textvariable=strFirst).grid(column = 1, row = 0)

tk.Label(frm, text = "Last Name").grid(column = 0, row = 1)
strLast = StringVar()
tk.Entry(frm, textvariable=strLast).grid(column = 1, row = 1)

tk.Label(frm, text = "Phone").grid(column = 0, row = 2)
strPhone = StringVar()
tk.Entry(frm, textvariable=strPhone).grid(column = 1, row = 2)

tk.Label(frm, text = "Major").grid(column = 0, row = 3)
strMajor = StringVar()
tk.Entry(frm, textvariable=strMajor).grid(column = 1, row = 3)

tk.Label(frm, text = "Comments").grid(column = 0, row = 3)
strComments = StringVar()
tk.Text(frm, textvariable=strComments).grid(column = 1, row = 3)



tk.Button(frm, text = "Add Student", command = lambda :clickHandler(strFirst,strLast,strPhone,strMajor,strComments)).grid(column = 0, row = 5)
tk.Button(frm, text = "Cancel", command = quit).grid(column = 1, row = 5)



# tk.Button(text = 'Button1', command = callback).pack(fill = tk.X)
# tk.Button(text = 'Button2', command = answer).pack(fill = tk.X)
# tk.Entry(text = "Hello").grid(column = 3, row = 0)
tk.mainloop()




