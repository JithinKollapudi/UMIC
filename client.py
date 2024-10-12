import socket

def connect_to_server():
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect(('localhost', 57657))

    # Prompt the user to enter a number
    number = input("Enter a number to factorize: ")

    # Send the number to the server
    client_socket.send(number.encode('utf-8'))

    # Receive the prime factors from the server
    data = client_socket.recv(1024).decode('utf-8')
    print(f"Response from server: {data}")  # Print the server's response

    # Close the connection
    client_socket.close()


connect_to_server()  # Start the client
