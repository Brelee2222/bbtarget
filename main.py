import consts
import socketio
import threading
import led
import time
import id

def listen() :
    while True :
        try :
            event = socket.receive(timeout=consts.WS_TIMEOUT)
            
            on_message(event)
        except socketio.exceptions.TimeoutError as e :
            print(e)

def on_message(event) :
    led.changePattern(event[1])
    

# init
socket = socketio.SimpleClient()

# setup
if consts.USE_WEBSOCKET : 
    socket.connect(consts.WS_URL, headers={"robotId":id.getID()})
    print("connected websocket")

    threading.Thread(target=listen)

# loop
while True :
    led.ledControl.writePattern()
    led.ledControl.show()