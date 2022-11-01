import tkinter as tk
import tkinter.messagebox
import time

class Application(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        self.running = False
        self.time = 0
        self.hours = 0
        self.mins = 0
        self.secs = 0
        self.structures()

    def structures(self):
        self.time_entry = tk.Entry(self)
        self.time_entry.grid(row=0, column=1)
        self.clock = tk.Label(self, text="00:00:00", font=("Courier", 15),bg="yellow", width=15)
        self.clock.grid(row=1, column=1)
        self.time_label = tk.Label(self, text="hour   min   sec", font=("Courier", 15), fg="red", width=15)
        self.time_label.grid(row=2, column=1)
        self.power_button = tk.Button(self, text="START", bg="white", command=lambda: self.start())
        self.power_button.grid(row=4, column=0)
        self.reset_button = tk.Button(self, text="RESET", bg="purple", command=lambda: self.reset())
        self.reset_button.grid(row=4, column=1)
        self.quit_button = tk.Button(self, text="QUIT", bg="red", command=lambda: self.quit())
        self.quit_button.grid(row=5, column=1)
        self.pause_button = tk.Button(self, text="PAUSE", bg="blue", command=lambda: self.pause())
        self.pause_button.grid(row =4 ,column=2)

    def calculate(self):
        self.hours = self.time // 3600
        self.mins = (self.time // 60) % 60
        self.secs = self.time % 60
        return "{:02d}:{:02d}:{:02d}".format(self.hours, self.mins, self.secs)

    def update(self):
        self.time = int(self.time_entry.get(),)
        try:
            self.clock.configure(text=self.calculate())
        except:
            self.clock.configure(text="00:00:00")

    def timer(self):
        if self.running:
            if self.time <= 0:
                self.clock.configure(text="Time Expired!")
            else:
                self.clock.configure(text=self.calculate())
                self.time = self.time-1
                self.after(1000, self.timer)

    def start(self):
        self.time = int(self.time_entry.get())
        self.time_entry.delete(0, 'end')
        self.running = True
        self.timer()

    def reset(self):
        self.power_button.configure(text="Start", command=lambda: self.start())
        self.running = False
        self.time = 0
        self.clock["text"] = "00:00:00"

    def quit(self):
        root.destroy()

    def pause(self):
        """Pause timer"""
        self.pause_button.configure(text="Resume", command=lambda: self.resume())
        if self.running == True:
            self.running = False
        self.timer()

    def resume(self):
        self.pause_button.configure(text="Pause", command=lambda: self.pause())
        self.master.bind("<Return>", lambda x: self.pause())
        if self.running == False:
            self.running = True
        self.timer()

root = tk.Tk()
root.title("COUNTDOWN")
Application(root).pack(side="top", fill="both", expand=True)
root.mainloop()
