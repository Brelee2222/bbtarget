import consts
import socketio
import threading
import led
import time
import id

def listen() :
    print("starting listener")
    while True :
        try :
            event = socket.receive(timeout=consts.WS_TIMEOUT)
            on_message(event)
        except socketio.exceptions.TimeoutError as e :
            print(e)

def on_message(event) :
    if (event[0] == "setBucketState"):
        pattern = event[1]
        print("setting pattern", pattern)
        led.changePattern(event[1])
    else:
        print("unknown event", event)
    
    

# init
socket = socketio.SimpleClient()

# setup
if consts.USE_WEBSOCKET : 
    socket.connect(consts.WS_URL, auth={"role": "robot","key": consts.WS_KEY,"robot_id":id.getID()})
    print("connected websocket")

    threading.Thread(target=listen).start()

# loop
while True :
    led.ledControl.writePattern()
    led.ledControl.show()