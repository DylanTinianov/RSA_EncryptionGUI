from Tkinter import *
from RSA_EncryptionGUI.Client import Network_Client


class Application(Frame):
    def run_encryption(self):
        Network_Client.run()
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
root.title("Dylan Tinianov RSA Software: Client")
app = Application(master=root)
app.mainloop()
root.destroy()
