import socket
import time
import numpy as np

# Set the time delay between each reading in seconds
time_delay = 1

# Set up the client socket
HOST = '127.0.0.1'
PORT = 5001

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    # Generate readings at regular intervals indefinitely
    i = 1
    while True:
        # Generate a random value for the current reading
        # Use a normal distribution with mean 0 and standard deviation 2
        # Add a small chance of generating an outlier value outside the range [-10, 10]
        if np.random.rand() < 0.05:
            reading = np.random.uniform(low=18, high=20)
        else:
            reading = np.random.normal(loc=0, scale=2)

        # Send the current reading to the server
        message = f"Light sensor Reading {i}: {reading} ({time.ctime()})"
        s.sendall(message.encode())

        # Print the current reading and the current time
        print(message + "blabla")

        # increment
        i += 1

        # Delay for the specified time between readings
        time.sleep(time_delay)
