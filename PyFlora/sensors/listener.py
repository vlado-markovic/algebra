import socket

# Set up the server socket
HOST = '127.0.0.1'
PORT = 5001

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    print (conn, addr)

    # Receive data from the client and print it to the console
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            print (data)
            if not data:
                break
            print(data.decode())
