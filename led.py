import consts
import ledDriving
import patterns

LED_PATTERNS = [
    ledDriving.LEDPattern([lambda : 0]),
    patterns.HitPattern(0), # 1 hit left
    patterns.HitPattern(1), # 2 hits left
    patterns.HitPattern(2), # 3 hits left
    ledDriving.LEDPattern([lambda : 0]),
    ledDriving.LEDPattern([lambda : consts.RED_ALLIANCE_COLOR]),
    ledDriving.LEDPattern([lambda : consts.BLUE_ALLIANCE_COLOR]),
    patterns.Rainbow([lambda : consts.FULL_BATTERY_COLOR]), # placeholder
    patterns.AllianceStation()
]

def changePattern(index) :
    ledControl.setPattern(LED_PATTERNS[index])

# initialize
ledControl = ledDriving.LEDControl(pin=consts.LED_SIG_PIN, n=consts.LED_NUMBER, brightness=consts.BRIGHTNESS)