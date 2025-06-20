from tkinter import *
from tkinter import IntVar

myWindow = Tk()
myWindow.title("ช่องทางรับข่าวสาร")
myWindow.geometry("1024x720")
myMessage1 = Label(myWindow, text="โปรดกรุณาป้อน-นามสกุลของคุณ", font="AngsanaNew 16")
myMessage1.place(x=20, y=30)
myDataBox1 = Entry(myWindow)
myDataBox1.place(x=280, y=30)
myMessage2 = Label(myWindow, text="คุณต้องการสมัครสาขาใด?", font="AngsanaNew 16")
myMessage2.place(x=20, y=68)
myDataBox2 = Entry(myWindow)
myDataBox2.place(x=280, y=68)

def DisplayInfo():
    userName = myDataBox1.get()
    text1 = Label(myWindow, text="ชื่อ-นามสกุล ของคุณคือ " + userName, font="Angsana 14")
    text1.place(x=20, y=300)
    userMajor = myDataBox2.get()
    text2 = Label(myWindow, text="สาขาที่คุณเลือกคือ " + userMajor, font="Angsana 14")
    text2.place(x=20, y=330)
    text9 = Label(myWindow, text="คุณสามารถรับเลือกการติดต่อช่องทางต่อไปนี้", font="Angsana 14")
    text9.place(x=20, y=360)
    if (myCheck1.get() == 1):
        text4 = Label(myWindow, text="Facebook")
        text4.place(x=20, y=390)
    if (myCheck2.get() == 1):
        text5 = Label(myWindow, text="Instagram")
        text5.place(x=20, y=420)
    if (myCheck3.get() == 1):
        text6 = Label(myWindow, text="TikTok")
        text6.place(x=20, y=450)
    if (myCheck4.get() == 1):
        text7 = Label(myWindow, text="Website")
        text7.place(x=20, y=480)
    if (myCheck5.get() == 1):
        text8 = Label(myWindow, text="Theacher")
        text8.place(x=20, y=510)

myCheck1 = IntVar();myCheck2 = IntVar();myCheck3 = IntVar();myCheck4 = IntVar();myCheck5 = IntVar()
myMessage3 = Label(myWindow, text="คุณทราบข่าวสารผ่านช่องทางใดบ้าง", font="AngsanaNew 16")
myMessage3.place(x=20, y=110)

myCheckButton1 = Checkbutton(myWindow, text="Facebook", variable=myCheck1, onvalue=1, offvalue=0, command=DisplayInfo)
myCheckButton1.place(x=20, y=150); myCheckButton1.var = myCheck1
myCheckButton2 = Checkbutton(myWindow, text="Instagram", variable=myCheck2, onvalue=1, offvalue=0, command=DisplayInfo)
myCheckButton2.place(x=20, y=180); myCheckButton2.var = myCheck2
myCheckButton3 = Checkbutton(myWindow, text="TikTok", variable=myCheck3, onvalue=1, offvalue=0, command=DisplayInfo)
myCheckButton3.place(x=20, y=210); myCheckButton3.var = myCheck3
myCheckButton4 = Checkbutton(myWindow, text="Website", variable=myCheck4, onvalue=1, offvalue=0, command=DisplayInfo)
myCheckButton4.place(x=20, y=240); myCheckButton4.var = myCheck4
myCheckButton5 = Checkbutton(myWindow, text="Teacher", variable=myCheck5, onvalue=1, offvalue=0, command=DisplayInfo)
myCheckButton5.place(x=20, y=270); myCheckButton5.var = myCheck5

myWindow.mainloop()
