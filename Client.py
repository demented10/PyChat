import socket, threading
from tkinter import *

encryption = 'utf-8'

nickname = input('Your nickname: ')

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 5555))

messages = []


def gui():
    root = Tk()
    root.title("ChatBox v1. Client: {}".format(nickname))
    root.geometry("320x640")

    entry_message_field = Text()
    entry_message_field.place(x=10, y=530, width=200, height=100)
    entry_message_field.size()

    def send_msg():
        message = '{}: {}'.format(nickname, entry_message_field.get(1.0, END))
        client.send(message.encode(encryption))

    button_send = Button(text="Send", command=send_msg)
    button_send.place(x=220, y=530, width=100, height=100)

    text = Text()
    text.place(x=10, y=0, width=300, height=500)
    scroll = Scrollbar(command=text.yview)
    scroll.place(x=310, y=0, width=10, height=500)

    text.config(yscrollcommand=scroll.set)

    def updateLabel():
        txt = str()
        for msg in messages:
            txt += msg
        text.delete("1.0","end")
        text.insert(1.0, txt)

    def receive():
        while True:
            try:
                message = client.recv(1024).decode(encryption)
                if message == 'NICKNAME':
                    client.send(nickname.encode(encryption))
                else:
                    messages.append(message)
                updateLabel()
            except:
                messages.append("An error occured!")
                client.close()
                break

    receive_thread = threading.Thread(target=receive)
    receive_thread.start()

    root.mainloop()


gui_thread = threading.Thread(target=gui)
gui_thread.start()
