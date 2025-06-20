from tkinter import *

myWindow = Tk()  #สร้างหน้าต่างสำหรับทำงาน (สร้างหน้า GUI)
myWindow.title('GUI for Studying')   #ข้อความทีุ่มมซ้ายบน เพื่อบอกว่าหน้าต่างนี้แสดงอะไร
myWindow.geometry('800x800')   #กำหนดขนาดของหน้าต่างสำหรับทำงาน หน่วยเป็นพิกเซล

myMassagel1 = Label(myWindow, text='โปรดระบุ Username ของคุณ', font='AngsanaNew 18')
myMassagel1.place(x = 20, y = 20)
myBox1 = Entry(myWindow)
myBox1.place(x = 320, y = 30)

myWindow.mainloop()   #สั่งให้หน้าต่างสำหรับทำงาน ที่ชื่อ myWindow ทำงานจนกว่าผู้ใช้งานจะกดปิดเอง