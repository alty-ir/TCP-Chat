# TCP Chat

Final Project of AUT Computer Network Course - Dr. Sabaei

A Python-based chat application implementing both TCP and UDP protocols for network communication. The application features a graphical user interface built with tkinter and supports multiple concurrent users.

## Features

- Real-time chat functionality using TCP for reliable message delivery
- UDP broadcast for server discovery
- Graphical user interface using tkinter
- Multi-threaded server supporting multiple concurrent connections
- Automatic port assignment for clients
- Broadcast messaging system

## Requirements

- Python 3.x
- tkinter (usually comes with Python installation)

## Structure

- `final_server.py` - Server implementation with UDP broadcasting and TCP connection handling
- `final_client.py` - Client implementation with GUI and network communication logic

## How to Run

1. Start the server:
   ```bash
   python final_server.py
   ```

2. Start one or more clients:
   ```bash
   python final_client.py
   ```

The client will automatically discover the server through UDP broadcast and establish a TCP connection.

## Technical Details

- The server uses UDP broadcasting to advertise its presence
- Clients automatically find a free TCP port for communication
- Multi-threaded design allows handling multiple client connections simultaneously
- Reliable message delivery is ensured through TCP protocol
- GUI provides an intuitive interface for sending and receiving messages

## License

See the [LICENSE](LICENSE) file for details.
