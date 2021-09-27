from tkinter import Label, Button, Tk, Text, Scrollbar

import self as self

root = Tk()

class MainGui:
    def __init__(self, nickname):
        root.title("ChatBox v1. Client: {}".format(nickname))
        root.geometry("340x450")
        Message()
        Btn('Отправить', 'send_msg')
        MessageLabel()
        Scroll()
    def startApp(self):
        root.mainloop()


class Message:
    entry_message_field = Text()
    def __init__(self):
        self.entry_message_field.place(x=10, y=330, width=200, height=100)
        self.entry_message_field.size()

class Btn:
    def __init__(self, text, commands):
        button_send = Button(text=text, command=commands)
        button_send.place(x=220, y=330, width=100, height=100)

    def send_msg(self, nickname, client, encryption):
        message = Message().entry_message_field
        message = '{}: {}'.format(nickname, message.get(1.0, 'END'))
        client.send(message.encode(encryption))


class MessageLabel:
    text = Label()
    def __init__(self):
        self.text.place(x=10, y=0, width=300, height=300)
        #self.text.config(yscrollcommand=scroll.set)


class Scroll:
    scroll = Scrollbar()
    def __init__(self):
        self.scroll.place(x=310, y=0, width=10, height=300)
        #self.scroll['command'] = text








def main():
    MainGui('nda').startApp()

if __name__ == '__main__':
    main()