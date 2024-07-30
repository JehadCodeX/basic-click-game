from tkinter import *
import threading
import time

count = 0
timer_count = 10


def timer():
    global timer_count
    while timer_count > 0:
        restart_button.config(state=DISABLED)
        time.sleep(1)
        timer_count -= 1
        window.after(0, update_timer_label)
        if timer_count <= 5:
            window.after(0, update_timer_color)
        if timer_count == 0:
            restart_button.config(state=ACTIVE)
    window.after(0, end_timer)


def update_timer_label():
    timer_label.config(text=f"Timer: {timer_count}")


def update_timer_color():
    timer_label.config(fg="darkred", bg="red")


def end_timer():
    count_button.config(state=DISABLED)
    CPS_label.config(text=f"{count / 10:.1f} clicks per second")
    CPS_label.pack()


def click():
    global count
    count += 1
    count_label.config(text=f"Count: {count}")


def restart():
    global count, timer_count, timer_thread
    count = 0
    timer_count = 10
    count_button.config(state=ACTIVE)
    count_label.config(text="Count: 0")
    timer_label.config(text="Timer: 10", fg="darkgreen", bg="green")
    CPS_label.pack_forget()
    if timer_thread is not None and timer_thread.is_alive():
        timer_thread.join(timeout=1)

    timer_thread = threading.Thread(target=timer, daemon=True)
    timer_thread.start()


timer_thread = None

window = Tk()
count_label = Label(text="Count: 0", font=("arial", 30, "bold"), fg="darkgreen", bg="green", relief=SUNKEN, bd=10)
timer_label = Label(text="Timer: 10", font=("arial", 30, "bold"), fg="darkgreen", bg="green", relief=SUNKEN, bd=10)
count_button = Button(text="Click Me!", command=click, font=("arial", 50, "bold"), relief=RAISED, bd=20, fg="darkgreen",
                      bg="green", activeforeground="darkgreen", activebackground="green")
restart_button = Button(text="Restart", command=restart, font=("arial", 20, "bold"), relief=RAISED, bd=10,
                        fg="darkgreen", bg="green", activeforeground="darkgreen", activebackground="green")
CPS_label = Label(font=("arial", 30, "bold"), fg="darkgreen", bg="green", relief=SUNKEN, bd=10)
window.geometry("500x500")
window.title("Click Game")
window.config(background="lime")

timer_label.place(x=250 - timer_label.winfo_reqwidth() // 2, y=20)
count_button.place(x=250 - count_button.winfo_reqwidth() // 2, y=250 - count_button.winfo_reqheight() // 2)
count_label.place(x=250 - count_label.winfo_reqwidth() // 2, y=480 - count_label.winfo_reqheight())
restart_button.place(x=10, y=410)

restart()

window.mainloop()

