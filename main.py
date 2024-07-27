#To activate the counter, press Restart

from tkinter import *
import threading
import time

count = 0
timer_count = 60
timer_running = False


def timer():
    global timer_count, timer_running
    while timer_running:
        time.sleep(1)
        timer_count -= 1
        timer_label.config(text=f"timer {timer_count}")
        if timer_count == 0:
            count_button.config(state=DISABLED)
            timer_label.config(fg="darkgreen", bg="green")
            timer_running = False
        elif timer_count <= 5:
            timer_label.config(fg="darkred", bg="red")


def start_timer():
    global timer_count, timer_running
    timer_count = 60
    timer_running = True
    active_timer = threading.Thread(target=timer, daemon=True)
    active_timer.start()


def click():
    global count
    count += 1
    count_label.config(text=f"count {count}")


def restart():
    global count, timer_running
    count = 0
    count_label.config(text="Count: 0")
    timer_label.config(text="Timer: 60", fg="darkgreen", bg="green")
    count_button.config(state=ACTIVE)
    timer_running = False
    start_timer()


window = Tk()
count_label = Label(text="Count: 0", font=("arial", 30, "bold"), fg="darkgreen", bg="green", relief=SUNKEN, bd=10)
timer_label = Label(text="Timer: 60", font=("arial", 30, "bold"), fg="darkgreen", bg="green", relief=SUNKEN, bd=10)
count_button = Button(text="Click Me!", command=click, font=("arial", 50, "bold"), relief=RAISED, bd=20, fg="darkgreen", bg="green", activeforeground="darkgreen", activebackground="green")
restart_button = Button(text="Restart", command=restart, font=("arial", 20, "bold"), relief=RAISED, bd=10, fg="darkgreen", bg="green", activeforeground="darkgreen", activebackground="green")
window.geometry("500x500")
window.title("click")
window.config(background="lime")
timer_label.place(x=250 - timer_label.winfo_reqwidth() // 2, y=20)
count_button.place(x=250 - count_button.winfo_reqwidth() // 2, y=250 - count_button.winfo_reqheight() // 2)
count_label.place(x=250 - count_label.winfo_reqwidth() // 2, y=480 - count_label.winfo_reqheight())
restart_button.place(x=10, y=410)
window.mainloop()

