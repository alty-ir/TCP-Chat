from socket import AF_INET, socket, SOCK_STREAM, SOCK_DGRAM, IPPROTO_UDP, SOL_SOCKET, SO_BROADCAST
from threading import Thread
import tkinter


def find_free_port():
    tcp = socket(AF_INET, SOCK_STREAM)
    tcp.bind(('', 0))
    addr, port = tcp.getsockname()
    tcp.close()
    return port


def send_port():
    """Handles receiving of messages."""
    print("tcp port sent")
    Thread(target=receive_first_tcp).start()
    while True:
        # print(message)
        udp_client_socket.sendto(
            bytes(str(message), encoding="utf8"), ('<broadcast>', 34000))


def receive_udp():
    msg = udp_listen.recv(BUFSIZ).decode("utf8")
    #     udpbroadcastreviced = True
    #     servertcpport = msg
    #     ADDR = ("",msg)
    #     client_socket.connect(ADDR)
    #msg_list.insert(tkinter.END, msg)
    udp_listen.close()
    Thread(target=send_port).start()
    # print(msg)


def receive_first_tcp():
    """Handles receiving of messages."""
    # tkinter.mainloop()  # Starts GUI execution.
    print("im listening for first tcp in this port: " + str(message))

    client, client_address = client_socket.accept()
    #ADDR = add
    msg = str(client.recv(4).decode("utf8"))
    print(msg, " that's it")
    a = int(msg)
    client_socket2.connect(("localhost", a))
    Thread(target=receive, args=(client,)).start()
    #msg_list.insert(tkinter.END, msg)


def receive(client):
    """Handles receiving of messages."""
    print("im here")
    while True:
        try:
            msg = client.recv(BUFSIZ).decode("utf8")
            print(msg)
            msg_list.insert(tkinter.END, msg)
        except OSError:  # Possibly client has left the chat.
            break


def send(event=None):  # event is passed by binders.
    """Handles sending of messages."""
    msg = my_msg.get()
    my_msg.set("")  # Clears input field.
    client_socket2.send(bytes(msg, "utf8"))
    if msg == "{quit}":
        client_socket2.close()
        top.quit()


def on_closing(event=None):
    """This function is to be called when the window is closed."""
    my_msg.set("{quit}")
    send()


# ---------------gui-------------
top = tkinter.Tk()
top.title("TCP Chat")

messages_frame = tkinter.Frame(top)
my_msg = tkinter.StringVar()  # For the messages to be sent.
my_msg.set("Type ...")
# To navigate through past messages.
scrollbar = tkinter.Scrollbar(messages_frame)
# Following will contain the messages.
msg_list = tkinter.Listbox(messages_frame, height=15,
                           width=50, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
msg_list.pack()
messages_frame.pack()

entry_field = tkinter.Entry(top, textvariable=my_msg)
entry_field.bind("<Return>", send)
entry_field.pack()
send_button = tkinter.Button(top, text="Send", command=send)
send_button.pack()

top.protocol("WM_DELETE_WINDOW", on_closing)
# ---------------gui-------------

# ----sockets part----

message = find_free_port()
print(message, " this was the free port ")
udpbroadcastreviced = False
servertcpport = 76324

BUFSIZ = 1024
ADDR = ("", servertcpport)

# udp_client_socket = socket(AF_INET, SOCK_DGRAM)
# udp_client_socket.settimeout(1.0)
# udp_client_socket.bind(("", 4445))

udp_client_socket = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP)
udp_client_socket.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
udp_client_socket.settimeout(2)
udp_client_socket.bind(("", 0))

udp_listen = socket(AF_INET, SOCK_DGRAM)
udd = ("", 37020)
udp_listen.bind(udd)
addr = ('<broadcast>', 34000)


client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.bind(('localhost', message))
client_socket.listen(5)

client_socket2 = socket(AF_INET, SOCK_STREAM)

receive_thread = Thread(target=receive_udp)
receive_thread.start()
tkinter.mainloop()  # Starts GUI execution.
