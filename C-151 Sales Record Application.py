from tkinter import *
root= Tk()

root.title("Sales Record Appication")
root.geometry("500x500")
root.configure(bg='#89CFF0')

month = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
profits = (20000, 45000, 78000, 97000, 12000, 456000, 65000, 54000, 10000, 30000, 70000, 90000)

label_max = Label(root)
label_max.place(relx = 0.5, rely = 0.3, anchor=CENTER)
label_min = Label(root)
label_min.place(relx = 0.5, rely = 0.5, anchor=CENTER)

max_profits = max(profits)
max_profits_index = profits.index(max_profits)
max_profits_month = month[max_profits_index]
display_max = 'The maximum profit of ' + str(max_profits) + ' was recorded in the month of ' + str(max_profits_month)

min_profits = min(profits)
min_profits_index = profits.index(min_profits)
min_profits_month = month[min_profits_index]
display_min = 'The minimum profit of ' + str(min_profits) + ' was recorded in the month of ' + str(min_profits_month)

def show_max():
    label_max['text'] = str(display_max)
    
def show_min():
    label_min['text'] = str(display_min)

btn1 = Button(root, text='Show Maximum Profit', command=show_max)
btn2 = Button(root, text='Show Minimum Profit', command=show_min)
btn1.place(relx = 0.5, rely = 0.4, anchor=CENTER)
btn2.place(relx = 0.5, rely = 0.6, anchor=CENTER)

root.mainloop()