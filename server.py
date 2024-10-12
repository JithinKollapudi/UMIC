import socket

def start_server():
    port_num = 57657  # Define the port number on which the server will listen
    # Create a socket object using the Internet address family and TCP protocol
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to a public host and the specified port
    server_socket.bind(('localhost', port_num))

    # Set the server to listen for incoming connections, allowing a maximum of 5 clients
    server_socket.listen(5)

    print(f"Server is listening on port {port_num}..")  # Print message to indicate the server is running

    while True:
        # Accept a client connection and store the client socket and address
        client_socket, addr = server_socket.accept()
        print(f"Got a connection from {addr}")  # Print the address of the connected client

        # Receive data sent by the client and decode it to a string
        data = client_socket.recv(1024).decode('utf-8')

        # Check if data was received; if not, close the connection
        if not data:
            print("No data received. Closing the connection.")
            client_socket.close()  # Close the client connection
            continue  # Go back to waiting for another connection

        print(f"Received {data} from client")  # Print the received data for debugging

        # Process the received data for unique prime factorization
        try:
            number = int(data)  # Convert the received data to an integer
            factors = prime_factors(number)  # Call the function to get the prime factors
            response = str(factors)  # Convert the list of factors to a string for sending
        except ValueError:
            response = "Error: Please send a valid integer."  # Handle invalid input (non-integer)

        # Send the processed data (unique prime factors) back to the client
        client_socket.send(response.encode('utf-8'))

        # Close the client connection after sending the response
        client_socket.close()

def prime_factors(n):
    i = 2  # Start checking for factors from 2
    factors = []  # Initialize an empty list to store factors
    while i * i <= n:  # Loop until i squared is greater than n
        if n % i:  # If n is not divisible by i
            i += 1  # Increment i to check the next potential factor
        else:
            n //= i  # Divide n by i to reduce it
            factors.append(i)  # Add the factor to the list
    if n > 1:  # If n is greater than 1, it means it's a prime factor
        factors.append(n)  # Add the remaining prime factor

    # Use a set to filter out duplicate factors
    list_set = set(factors)  # Create a set from the factors list to get unique factors
    unique_factors = list(list_set)  # Convert the set back to a list for returning
    return unique_factors  # Return the list of unique prime factors

# Start the server to accept incoming connections
start_server()  
