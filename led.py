import consts
import ledDriving
import patterns

CONSOLE_PATTERN = patterns.Solid(consts.PRELIMINARY_COLOR)

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

def changePattern(index) :
    ledControl.setPattern(MATCH_PATTERNS[index])

# initialize
ledControl = ledDriving.LEDControl(pin=consts.LED_SIG_PIN, n=consts.LED_NUMBER, brightness=consts.BRIGHTNESS, auto_write=False)
ledControl.setPattern(CONSOLE_PATTERN)