import tkinter as tk

# let create class to create window
class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Hello Tkinter")
        self.label_text = tk.StringVar()
        self.label_text.set("Choose One")

        self.name_text = tk.StringVar()

        # Label in window
        label = tk.Label(self, textvar=self.label_text)
        label.pack(padx=100, pady=50)

        # Entry Field
        self.name_entry = tk.Entry(self, textvar=self.name_text)
        self.name_entry.pack(fill=tk.BOTH, expand=1, padx=20, pady=20)

        # Button
        hello_btn = tk.Button(self, text="Say Hello", command=self.say_hello)
        hello_btn.pack(side=tk.LEFT, padx=(20,0), pady=(0,20))

        goodbye_btn = tk.Button(self, text="Say GoodBye", command=self.say_goodbye)
        goodbye_btn.pack(side=tk.RIGHT, padx=(0,20), pady=(0,20))

    def say_hello(self):
        message = "Hello there " + self.name_entry.get()
        msgbox.showinfo("Hello", message)

    def say_goodbye(self):
        if msgbox.askyesno("Close Window?", "Would you like to close this window?"):
            message = "Window will close in 2 seconds - goodybye " + self.name_entry.get()
            self.label_text.set(message)
            self.after(2000, self.destroy)
        else:
            msgbox.showinfo("Not Closing", "Great! This window will stay open.")

if __name__ == "__main__":
    window = Window()
    window.mainloop()
