from tkinter import *
from tkinter import ttk
import mysql.connector  as mysql
root = Tk()

def stat():
    if(listBox2.get_children()!=1):
        for item in listBox2.get_children():
            listBox2.delete(item)
    name=nameBox.get()
    if(name==""):
        print('nothing')
    else:
        mysqldb =mysql.connect(host="127.0.0.1",user="root",password="E@^KT3Qn!Cf:(}3Y",database="laboratory")
        cursor=mysqldb.cursor()
        query="call laboratory.GetAllProducts(+\""+name+"\");"
        cursor.execute(query)
        records = cursor.fetchall()
        for i, (nums, mins, avg,max) in enumerate(records, start=1):
            listBox2.insert("", "end", values=(nums, mins, avg,max))
            mysqldb.close()
        
def get():
    if(listBox.get_children()!=1):
        for item in listBox.get_children():
            listBox.delete(item)
    loc=locBox.get()
    if(loc==""):
        print('nothing')
    else:
        mysqldb =mysql.connect(host="127.0.0.1",user="root",password="E@^KT3Qn!Cf:(}3Y",database="laboratory")
        cursor=mysqldb.cursor()
        query="SELECT l.lname,t.tno,t.tname,t.tjob,t.tmgr,t.thiredate,t.tsalary, t.tbonus FROM lab l, Technician t Where l.llocation=\""+loc+"\" AND t.tlno=l.lno"
        cursor.execute(query)
        records = cursor.fetchall()
        for i, (lname, tno, tname,tjob,tmgr,thiredate,tsalary,tbonus) in enumerate(records, start=1):
            listBox.insert("", "end", values=(lname, tno, tname,tjob,tmgr,thiredate,tsalary,tbonus))
            mysqldb.close()


root.geometry("1000x1000")
root.title("Laboratory Database")
n4= Label(root,text="Exercise number 4")
n4.place(x=40,y=20)
locLabel =Label(root,text='Enter Laboratory location')
locLabel.place(x=20,y=50)
locBox= Entry()
locBox.place(x=200, y=50)
n4Button= Button(root,text="Retrieve", command=get)
n4Button.place(x=350,y=45)

n5= Label(root,text="Exercise number 5")
n5.place(x=40,y=20)
nameLabel =Label(root,text='Enter Laboratory name')
nameLabel.place(x=20,y=500)
nameBox= Entry()
nameBox.place(x=200, y=500)
n5Button= Button(root,text="Retrieve", command=stat)
n5Button.place(x=350,y=495)


cols = ('lname', 'tno', 'tname','tjob','tmgr','thiredate','tsalary','tbonus')
listBox = ttk.Treeview(root, columns=cols, show='headings')

for col in cols:
    listBox.heading(col, text=col)
    listBox.grid(row=1, column=0, columnspan=1)
    listBox.place(x=10, y=200)
listBox.column('#1', width=120)
listBox.column('#2', width=120)
listBox.column('#3', width=120)
listBox.column('#4', width=120)
listBox.column('#5', width=120)
listBox.column('#6', width=120)
listBox.column('#7', width=120)
listBox.column('#8', width=120) 


cols = ('Number of technicians', 'Minimum Salary', 'Average Salary','Maximum Salary')
listBox2 = ttk.Treeview(root, columns=cols, show='headings')

for col in cols:
    listBox2.heading(col, text=col)
    listBox2.grid(row=1, column=0, columnspan=1)
    listBox2.place(x=10, y=550)
listBox2.column('#1', width=120)
listBox2.column('#2', width=120)
listBox2.column('#3', width=120)
listBox2.column('#4', width=120)






listBox.pack_forget()

root.mainloop()