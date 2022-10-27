from tkinter import *
from datetime import datetime

root = Tk()

root.title("Age Calculator")
root.geometry("400x300")
root.resizable(False, False)
root.config(bg="#C98686")

name = StringVar()
year = StringVar()
month = StringVar()
day = StringVar()

name_label = Label(root, font=("Roboto 12"), text="Name: ", bg="#C98686", fg="#fff")
name_label.place(x = 10, y = 10)
name_entry = Entry(root, font=("Roboto 12"), textvariable=name)
name_entry.place(x = 100, y = 10)

year_label = Label(root, font=("Roboto 12"), text="Year: ", bg="#C98686", fg="#fff")
year_label.place(x = 10, y = 50)
year_entry = Entry(root, font=("Roboto 12"), textvariable=year)
year_entry.place(x = 100, y = 50) 

month_label = Label(root, font=("Roboto 12"), text="Month: ", bg="#C98686", fg="#fff")
month_label.place(x = 10, y = 90)
month_entry = Entry(root, font=("Roboto 12"), textvariable=month)
month_entry.place(x = 100, y = 90) 

day_label = Label(root, font=("Roboto 12"), text="Day: ", bg="#C98686", fg="#fff")
day_label.place(x = 10, y = 130)
day_entry = Entry(root, font=("Roboto 12"), textvariable=day)
day_entry.place(x = 100, y = 130) 

Button(root, font=("Roboto 15"), bg="#000", fg="#fff", text="Calculate age", command=lambda:get_current_age()).place(x = 200, y = 200, anchor="center")

final_label = Label(root, font=("Roboto 12"), bg="#C98686", fg="#fff")
final_label.place(x=200, y=250,anchor="center")

def get_current_age():
    current_year = datetime.now().year
    current_month = datetime.now().month
    current_day = datetime.now().day

    get_name = name.get()
    get_year = year.get()
    get_month = month.get()
    get_day = day.get()

    if not get_name or not get_year or not get_month or not get_day:
        final_label["text"] = "Values not found"
    elif int(get_year) > current_year:
        final_label["text"] = "That is not possible, you cant born in the future"
    elif int(get_month) < 0 or int(get_month) > 12:
        final_label["text"] = "The number of the month is not possible"
    elif int(get_day) < 0 or int(get_day) > 31:
        final_label["text"] = "The number of the day is not possible"
    else:
        relative_age = current_year - int(get_year)

        if current_month > int(get_month):
            relative_age += 1
            final_label["text"] = f"Hi {get_name}, your age is {relative_age}."

        elif int(get_month) == current_month and current_day < int(get_day):
            relative_age -= 1
            final_label["text"] = f"Hi {get_name}, your age is {relative_age}."

        elif int(get_month) == current_month and current_day >= int(get_day):
            relative_age += 1
            final_label["text"] = f"Hi {get_name}, your age is {relative_age}."
            
        else:
            final_label["text"] = f"Hi {get_name}, your age is {relative_age}."


    

root.mainloop()