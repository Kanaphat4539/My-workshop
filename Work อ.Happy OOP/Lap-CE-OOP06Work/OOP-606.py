from tkinter import *
from tkinter import IntVar
import statistics

# สร้างฟังก์ชันสำหรับเพิ่มข้อมูล (Function to add data)
def add_data():
    data = myBox1.get()
    if data:
        value = float(data)
        items.append(value)
        displayBox.insert(END, data)
        myBox1.delete(0, END)
        mySummation()
        myAverage()
        myMaximum()
        myMinimum()
        myVariance()
        myStdev()

# สร้างฟังก์ชันสำหรับคำนวณผลรวม (Function to summation display)
def mySummation():
    total_sum = sum(items)
    sum_label.config(text=f'Summation = {total_sum}')

def myAverage():
    total_Avg = sum(items)/len(items)
    Avg_label.config(text=f'Average = {total_Avg}')

def myMaximum():
    total_Max = max(items)
    Max_label.config(text=f'Maximum = {total_Max}')

def myMinimum():
    total_Min = min(items)
    Min_label.config(text=f'Minimum = {total_Min}')

def myVariance():
    if len(items) > 1:  # ต้องมีข้อมูลอย่างน้อย 2 ค่า
        total_Var = statistics.variance(items)
        Var_label.config(text=f'Variance = {total_Var}')
    else:
        Var_label.config(text='Variance = Not enough data')  # แสดงข้อความแจ้งเตือน ว่าข้อมูลยังไม่พอ

def myStdev():
    if len(items) > 1:  # ต้องมีข้อมูลอย่างน้อย 2 ค่า
        total_Stdev = statistics.stdev(items)
        Stdev_label.config(text=f'Standard Deviation = {total_Stdev}')
    else:
        Stdev_label.config(text='Standard Deviation = Not enough data')  # แสดงข้อความแจ้งเตือน ว่าข้อมูลยังไม่พอ
    

# สร้างหน้าต่างหลักสำหรับทำงาน (Create the main window)
win = Tk()
win.title('การทำงานเกี่ยวกับสถิติ')
win.geometry('1024x720')

# สร้างข้อความเพื่อแสดงที่ต้องการ (Create the message for information)
myText1 = Label(win, text='กรุณาป้อนข้อมูลเป็นตัวเลข : ', font='AngsanaNew 16')
myText1.place(x=20, y=20)

# สร้างกล่องป้อนข้อมูล (Create an entry widget for input)
myBox1 = Entry(win)
myBox1.place(x=270, y=30)

# สร้างปุ่มสำหรับป้อนข้อมูล (Create a button to add data)
myButton1 = Button(win, text='ป้อนข้อมูล', command=add_data)
myButton1.place(x=20, y=60)

# สร้างกล่องแสดงข้อมูลของ list (Create a listbox to display the data)
displayBox = Listbox(win)
displayBox.place(x=20, y=400)

# สร้างข้อความสำหรับแสดงผลรวม (Create a label to display summation)
sum_label = Label(win, text='Summation = 0.00')
sum_label.place(x=20, y=200)
Avg_label = Label(win, text='Average = 0.00')
Avg_label.place(x=20, y=220)
Max_label = Label(win, text='Maximum = 0.00')
Max_label.place(x=20, y=240)
Min_label = Label(win, text='Minimum = 0.00')
Min_label.place(x=20, y=260)
Var_label = Label(win, text='Variance = 0.00')
Var_label.place(x=20, y=280)
Stdev_label = Label(win, text='Standard Deviation = 0.00')
Stdev_label.place(x=20, y=300)

# สร้างตัวแปร list เพื่อเก็บค่าข้อมูล (Initialize an empty list to store data)
items = []

# เริ่มการทำงาน (Run the application)
win.mainloop()