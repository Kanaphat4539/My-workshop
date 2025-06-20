from tkinter import *
from tkinter import IntVar

myWindow = Tk()
myWindow.title('ช่องทางรับข่าวสาร')
myWindow.geometry('1024x720')
myMassage = Label(myWindow, text = 'โปรดป้อนเลขจำนวนเต็ม', font = 'AngsanaNew 16' )
myMassage.place(x = 20, y = 30)
myDataBox1 = Entry(myWindow)
myDataBox1.place(x = 220, y = 38)

def CollectedData():
    dataList = myDataBox1.get()
    if dataList:
        myListBox.insert(END, dataList)
        myDataBox1.delete(0, END)

cmd1 = Button(myWindow, text = 'เพิ่มข้อมูล', command = CollectedData)
cmd1.place(x = 20, y = 70)

myListBox = Listbox(myWindow)
myListBox.place(x = 20, y = 150)

myWindow.mainloop()