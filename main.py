import consts
import socketio
import threading
import led
import time
import id

def listenConsole() :
    print("listening to console")
    while True :
        led.changePattern(int(input()))

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
    
def onError(e: Exception) :
    if socket.connected :
        socket.emit("robotTargetError", str(e))
    else :
        led.displayLog(consts.ERROR_COLOR)

# init
socket = socketio.SimpleClient()

# setup
if consts.USE_WEBSOCKET : 
    try :
        socket.connect(consts.WS_URL, auth={"role": "robot","key": consts.WS_KEY,"robot_id":id.getID()})
        print("connected websocket")
        threading.Thread(target=listen).start()
    except socketio.exceptions.ConnectionError as e :
        print(e)
        led.displayLog(consts.ERROR_COLOR)

if consts.USE_CONSOLE_INPUT :
    threading.Thread(target=listenConsole).start()

# loop
while True :
    led.ledControl.updatePattern()
    led.ledControl.show()

    time.sleep(consts.LED_INTERVAL_TIMEOUT)