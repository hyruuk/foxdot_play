# Dummy osc signal sender
import random
import time
from pythonosc.udp_client import SimpleUDPClient

def osc_sender(address, port):
    # Set up the OSC client
    client = SimpleUDPClient(address, port)
    # Send random OSC messages at 10Hz
    print(f'Sending to {address}:{port}')
    while True:
        # Generate some random data
        data = [random.random() for _ in range(4)]
        # Send an OSC message with the random data
        client.send_message("/random_data", [*data])
        # Wait for 0.1 seconds (10Hz)
        time.sleep(0.1)
osc_sender('127.0.0.1',8000)