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
       
def Find_sum():
    mySummation()
def Find_Avg():
    myAverage()
def Find_Max():
    myMaximum()
def Find_Min():
    myMinimum()
def Find_Var():
    myVariance()
def Find_Stdev():
    myStdev()


# สร้างฟังก์ชันสำหรับคำนวณผลรวม (Function to summation display)
def mySummation():
    if len(items) >= 1:
        total_sum = sum(items)
        sum_label.config(text=f'Summation = {total_sum}')
    else:
        sum_label.config(text = 'Summation = Not enough data')
    
def myAverage():
    if len(items) >= 1:
        total_Avg = sum(items)/len(items)
        Avg_label.config(text=f'Average = {total_Avg}')
    else:
        Avg_label.config(text = 'Average = Not enough data')
    

def myMaximum():
     if len(items) >= 1:
        total_Max = max(items)
        Max_label.config(text=f'Maximum = {total_Max}')
     else:
        Max_label.config(text = 'Maximum = Not enough data')
    

def myMinimum():
    if len(items) >= 1:
        total_Min = min(items)
        Min_label.config(text=f'Minimum = {total_Min}')
    else:
        Min_label.config(text = 'Minimum = Not enough data')

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

myButton2 = Button(win, text='หาผลรวม "กดตรงนี้"', command=Find_sum, font = 'Thaisaraban 8')
myButton2.place(x=20, y=90)

myButton3 = Button(win, text='หาค่าเฉลี่ย "กดตรงนี้"', command=Find_Avg, font = 'Thaisaraban 8')
myButton3.place(x=20, y=120)

myButton4 = Button(win, text='หาค่ามากสุด "กดตรงนี้"', command=Find_Max, font = 'Thaisaraban 8')
myButton4.place(x=20, y=150)

myButton5 = Button(win, text='หาค่าน้อยสุด "กดตรงนี้"', command=Find_Min, font = 'Thaisaraban 8')
myButton5.place(x=20, y=180)

myButton6 = Button(win, text='หาค่าแปรปรวน "กดตรงนี้"', command=Find_Var, font = 'Thaisaraban 8')
myButton6.place(x=20, y=210)

myButton7 = Button(win, text='หาค่าเบี่ยงเบน "กดตรงนี้"', command=Find_Stdev, font = 'Thaisaraban 8')
myButton7.place(x=20, y=240)



# สร้างกล่องแสดงข้อมูลของ list (Create a listbox to display the data)
displayBox = Listbox(win)
displayBox.place(x=20, y=300)

# สร้างข้อความสำหรับแสดงผลรวม (Create a label to display summation)
sum_label = Label(win, text='Summation = 0.00', font = 'AnsanaNew 8')
sum_label.place(x=150, y=90)
Avg_label = Label(win, text='Average = 0.00', font = 'AnsanaNew 8')
Avg_label.place(x=150, y=120)
Max_label = Label(win, text='Maximum = 0.00', font = 'AnsanaNew 8')
Max_label.place(x=150, y=150)
Min_label = Label(win, text='Minimum = 0.00', font = 'AnsanaNew 8')
Min_label.place(x=150, y=180)
Var_label = Label(win, text='Variance = 0.00', font = 'AnsanaNew 8')
Var_label.place(x=150, y=210)
Stdev_label = Label(win, text='Standard Deviation = 0.00', font = 'AnsanaNew 8')
Stdev_label.place(x=150, y=240)

# สร้างตัวแปร list เพื่อเก็บค่าข้อมูล (Initialize an empty list to store data)
items = []

# เริ่มการทำงาน (Run the application)
win.mainloop()