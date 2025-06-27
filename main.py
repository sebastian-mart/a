from  tkinter import *
from tkinter import ttk
import json


class a:
    def __init__(self,m):
        self.a=Label(m, text='Company').grid(row=0)
        self.b=Label(m, text='Departament').grid(row=1)
        self.c=Label(m, text='Name').grid(row=2)
        self.d=Label(m, text='Function').grid(row=3)
        self.e=Label(m, text='Salary').grid(row=4)
        self.f=Label(m, text='Birth date').grid(row=5)
        self.e1 = Entry(m)
        self.e2 = Entry(m)
        self.e3 = Entry(m)
        self.e4 = Entry(m)
        self.e5 = Entry(m)
        self.combo_box = ttk.Combobox(m,
                                 values=["Ianuarie", "Februarie", "Martie", "Aprlie", "Mai", "Iunie", "Iulie", "August",
                                         "Septembrie", "Octombrie", "Noiembrie", "Decembrie"])
        self.combo_box.set("Month")
        self.combo_box.grid(row=5, column=1)
        self.combo_box.bind("<<ComboboxSelected>>", self.select)
        self.e1.grid(row=0, column=1)
        self.e2.grid(row=1, column=1)
        self.e3.grid(row=2, column=1)
        self.e4.grid(row=3, column=1)
        self.e5.grid(row=4, column=1)

        self.menu = Menu(m)
        m.config(menu=self.menu)
        self.filemenu = Menu(self.menu)
        self.menu.add_cascade(label='File', menu=self.filemenu)
        self.filemenu.add_command(label='Save', command=self.save)
        self.filemenu.add_separator()
        self.filemenu.add_command(label='Exit', command=m.quit)


    def select(self,event):
        selected_item = self.combo_box.get()


    def save(self):
        a = self.e1.get()
        b = self.e2.get()
        c = self.e3.get()
        d = self.e4.get()
        e = self.e5.get()
        f = self.combo_box.get()
        data={
            "company":a,
            "department":b,
            "name":c,
            "function":d,
            "salary":e,
            "birth":f
        }
        f=open("data.json",'w')
        json.dump(data,f,indent=4)





if __name__ == '__main__':
    m=Tk()
    a(m)
    m.mainloop()


