from Tkinter import *
from Host import Network_Socket


class Application(Frame):
    def create_network_socket(self):
        Network_Socket.create_socket()
        self.createSocket["state"] = DISABLED
        self.keyGen["state"] = NORMAL

    def generate_key_pair(self):
        Network_Socket.key_gen()
        self.sendReceiveData["state"] = NORMAL

    def send_receive_data(self):
        Network_Socket.send_receive_data()
        self.keyGen["state"] = DISABLED
        self.sendReceiveData["state"] = DISABLED

    def create_widgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"] = "red"
        self.QUIT["command"] = self.quit

        self.createSocket = Button(self)
        self.createSocket["text"] = "Set up Socket"
        self.createSocket["fg"] = "red"
        self.createSocket["command"] = self.create_network_socket

        self.keyGen = Button(self)
        self.keyGen["text"] = "Generate Key Pair"
        self.keyGen["command"] = self.generate_key_pair
        self.keyGen["state"] = DISABLED

        self.sendReceiveData = Button(self)
        self.sendReceiveData["text"] = "Establish connection; send and receive data"
        self.sendReceiveData["command"] = self.send_receive_data
        self.sendReceiveData["state"] = DISABLED

        self.QUIT.pack({"side": "left"})
        self.createSocket.pack({"side": "left"})
        self.keyGen.pack({"side": "left"})
        self.sendReceiveData.pack({"side": "left"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.create_widgets()

root = Tk()
root.title("Dylan Tinianov RSA Software: Host")
app = Application(master=root)
app.mainloop()
root.destroy()
