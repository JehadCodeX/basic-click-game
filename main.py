from tkinter import *
import threading
import time

count = 0
timer_count = 60


def timer():
    global timer_count
    while True:
        time.sleep(1)
        timer_count -= 1
        timer_label.config(text=f"timer {timer_count}")
        if timer_count == 0:
            count_button.config(state=DISABLED)
            timer_label.config(fg="darkgreen", bg="green")
            break
        if timer_count <= 5:
            timer_label.config(fg="darkred", bg="red")


active_timer = threading.Thread(target=timer, daemon=True)
active_timer.start()


def click():
    global count
    count += 1
    count_label.config(text=f"count {count}")


window = Tk()
count_label = Label(text="count: 0", font=("arial", 30, "bold"), fg="darkgreen", bg="green", relief=SUNKEN, bd=10)
timer_label = Label(text="timer: 60", font=("arial", 30, "bold"), fg="darkgreen", bg="green", relief=SUNKEN, bd=10)
count_button = Button(text="Click Me!", command=click, font=("arial", 50, "bold"), relief=RAISED, bd=20, fg="darkgreen", bg="green", activeforeground="darkgreen", activebackground="green")
window.geometry("500x500")
window.title("click")
window.config(background="lime")
timer_label.place(x=250 - timer_label.winfo_reqwidth() // 2, y=20)
count_button.place(x=250 - count_button.winfo_reqwidth() // 2, y=250 - count_button.winfo_reqheight() // 2)
count_label.place(x=250 - count_label.winfo_reqwidth() // 2, y=480 - count_label.winfo_reqheight())
window.mainloop()
