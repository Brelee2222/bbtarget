import consts
import ledDriving
import patterns

# LEDs may also be used to display console later on

ERROR_PATTERN = patterns.Solid(consts.ERROR_COLOR)

MATCH_PATTERNS = [
    patterns.Solid(0),
    patterns.HitPattern(0), # 1 hit left
    patterns.HitPattern(1), # 2 hits left
    patterns.HitPattern(2), # 3 hits left
    patterns.AllianceStation(),
    patterns.AllianceWin(True),
    patterns.AllianceWin(False),
    patterns.FinalsWin(True),
    patterns.FinalsWin(False),
]

def displayError() :
    ledControl.setPattern

def changePattern(index) :
    ledControl.setPattern(MATCH_PATTERNS[index])

def changeBrightness(brightness: int) :
    ledControl.brightness = brightness

# initialize
ledControl = ledDriving.LEDControl(pin=consts.LED_SIG_PIN, n=consts.LED_NUMBER, brightness=consts.BRIGHTNESS, auto_write=False)
ledControl.setPattern(patterns.Solid(consts.PRELIMINARY_COLOR))