import tkinter as tk

win = tk.Tk()
win.title('การส้รางกล่องรับข้อความจากผู้ใช้งาน')
win.geometry('500x300')
#สร้างข้อความ เพื่อบอกข้อมูล
L1 = tk.Label(win, text = 'โปรดป้อนค่าความยาวสี่เหลี่ยม (หน่วยเมตร) : ')
L1.place(x=20, y=20)
W = tk.Label(win,  text = 'โปรดป้อนค่าความกว้างสี่เหลี่ยม (หน่วยเมตร) : ')
W.place(x=20, y=50)
#สร้างกล่องรับข้อความ
Box_L = tk.Entry(win)
Box_L.place(x=250, y=20)
Box_W = tk.Entry(win)
Box_W.place(x=250, y=50)
#ส้รางการทำงานให้กับปุ่ม cmd
def Rectangular_Area():
    value1 = float(Box_L.get())
    value2 = float(Box_W.get())
    Ans = value1*value2
    txt3 = tk.Label(win, text = 'พื้นที่สี่เหลี่ยม = %.2f' %Ans, font = 'AngsanaNew 24')
    txt3.place(x = 20, y = 80)

cmd = tk.Button(win, text = 'คำนวณ กดตรงนี้', command = Rectangular_Area)
cmd.place(x = 20, y = 80)

win.mainloop()