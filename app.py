

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        root = tk.Tk()
        self.master = tk.Canvas(root, width=800, height=600, bg="white")
        self.pack()
        root.geometry('800x600')
        root.mainloop()


