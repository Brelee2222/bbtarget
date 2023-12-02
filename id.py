import sys
# import RPi.GPIO as GPIO
# import consts
# Should return R1, R2, R3, B1, B2, or B3 for FMS

# GPIO.setup([consts.ID_PLUS_1_PIN, consts.ID_PLUS_2_PIN, consts.ID_RED_BLUE_PIN], GPIO.IN, pull_up_down=GPIO.PUD_UP)

def getPlus1() :
    # return GPIO.input(consts.ID_PLUS_1_PIN)
    pass

def getPlus2() :
    # return GPIO.input(consts.ID_PLUS_2_PIN)
    pass

def getRedBlue() :
    # return GPIO.input(consts.ID_RED_BLUE_PIN)
    pass

def getID() -> str :
    return ("R" if isRed() else "B") + str(numberID)

def getNumberID() -> int :
    return numberID

def isRed() -> bool :
    return redBlue

def changeID(id: int, red: bool) :
    pass

try :
    numberID = int(sys.argv[1])
    redBlue = bool(sys.argv[2])
except :
    numberID = (not getPlus1()) + ((not getPlus2()) << 1)
    redBlue = not getRedBlue()

print(numberID)
print(redBlue)