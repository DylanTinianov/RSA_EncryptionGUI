from Tkinter import *
from rsa_encryption_gui.client import network_client


class Application(Frame):
    def run_encryption(self):
        network_client.run()
        self.run["state"] = DISABLED

    def create_widgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"] = "red"
        self.QUIT["command"] = self.quit

        self.run = Button(self)
        self.run["text"] = "Establish Connection"
        self.run["command"] = self.run_encryption

        self.QUIT.pack({"side": "left"})
        self.run.pack({"side": "left"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.create_widgets()

root = Tk()
root.title("Dylan Tinianov RSA Software: client")
app = Application(master=root)
app.mainloop()
root.destroy()
