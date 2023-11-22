import consts
import socketio
from socketio import exceptions as socketioExeptions
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
    if event[0] == "setBucketState":
        pattern = event[1]
        print("setting pattern", pattern)
        led.changePattern(event[1])
    elif event[0] == "changeBrightness":
        led.changeBrightness(event[1])
    elif event[0] == "changeID":
        id.changeID(event[1], event[2]) # might add a type check later on
    else :
        print("unknown event", event)
    

# init
socket = socketio.SimpleClient()

# setup
if consts.USE_WEBSOCKET : 
    try :
        socket.connect(consts.WS_URL, auth={"role": "robot","key": consts.WS_KEY,"robot_id":id.getID()})
        print("connected websocket")
    except socketio.exceptions.ConnectionError as e :
        print(e)
        led.displayError()
    finally : 
        threading.Thread(target=listen).start()

# loop
while True :
    led.ledControl.writePattern()
    led.ledControl.show()
    
    time.sleep(consts.LED_INTERVAL_TIMEOUT)