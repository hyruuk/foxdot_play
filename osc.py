from pythonosc.dispatcher import Dispatcher
from pythonosc.osc_server import BlockingOSCUDPServer
# Define a global variable to store the OSC message data
osc_data = None
def handle_osc(address, *args):
    global osc_data
    osc_data = args
    print(f"Received OSC message: {address} {args}")
    # Do something with the OSC message data here
def osc_listener(address, port, oscpath="/.*"):
    # Set up the OSC server and dispatcher
    dispatcher = Dispatcher()
    dispatcher.map(oscpath, handle_osc)
    server = BlockingOSCUDPServer((address, port), dispatcher)
    # Start the OSC server and handle a single incoming message
    print(f"Listening for OSC messages on {address}:{port}...")
    server.handle_request()
    # Return the OSC message data
    return osc_data
osc_data = osc_listener("127.0.0.1", 8000)
print(osc_data)
