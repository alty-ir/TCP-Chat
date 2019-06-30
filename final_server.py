from socket import AF_INET, socket, SOCK_STREAM, SOCK_DGRAM, IPPROTO_UDP, SOL_SOCKET, SO_BROADCAST
from threading import Thread


def send_udp_invitation():
    """Sets up handling for incoming clients."""
    Thread(target=accept_incoming_connections).start()
    # Thread(target=tempfunc).start()

    while True:
        message = b"Send me ur free tcp port"
        udp_server_socket.sendto(message, ('<broadcast>', 37020))
        #print("invitation sent!")


# def tempfunc():
#    while True:
#         client, client_address = SERVER.accept()
#         Thread(target=handle_client, args=(client,)).start()


def accept_incoming_connections():
    """Sets up handling for incoming clients."""
    while True:
        port, client_address = udp_listen.recvfrom(BUFSIZ)
        if(port in addresses):
            continue  # duplicate
        newport = int(port.decode("utf8"))
        newaddr = ("localhost", newport)

        print("%s:%d has connected." % newaddr)

        addresses[port] = newaddr
        client_socket2 = socket(AF_INET, SOCK_STREAM)
        client_socket2.connect(newaddr)
        clients[client_socket2] = newport
        client_socket2.send(bytes(str(my_port), "utf8"))
        client_socket2.send(bytes("Hi! Type your name and press enter", "utf8"))

        # ------------

        client, client_address2 = SERVER.accept()
        Thread(target=handle_client, args=(client,)).start()


def handle_client(client):

    name = client.recv(BUFSIZ).decode("utf8")
#     welcome = 'Welcome %s! If you ever want to quit, type {quit} to exit.' % name
#     client.send(bytes("{quit}", "utf8"))
    msg = "%s has joined the chat!" % name
    broadcast(bytes(msg, "utf8"))

    while True:
        msg = client.recv(BUFSIZ)
        if msg != bytes("{quit}", "utf8"):
            broadcast(msg, name+": ")
        else:
            client.send(bytes("{quit}", "utf8"))
            client.close()
            broadcast(bytes("%s has left the chat." % name, "utf8"))
            break


def broadcast(msg, prefix=""):  # prefix is for name identification.
    """Broadcasts a message to all the clients."""
    for sock in clients:
        sock.send(bytes(prefix, "utf8")+msg)


clients = {}
addresses = {}

# tcp
BUFSIZ = 1024
ADDR = ('', 33000)
my_port = 2100
SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(("localhost", my_port))
SERVER.listen(20)

if __name__ == "__main__":
    udp_listen = socket(AF_INET, SOCK_DGRAM)
    udp_listen.bind(('', 34000))

    udp_server_socket = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP)
    udp_server_socket.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
    udp_server_socket.settimeout(2)
    udp_server_socket.bind(("", 33000))

    print("Sending udp invitation & Waiting for tcp connection...")
    ACCEPT_THREAD = Thread(target=send_udp_invitation)

    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()

    SERVER.close()
