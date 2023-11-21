import consts
import ledDriving
import patterns

LED_PATTERNS = [
    ledDriving.LEDPattern([lambda pixels, index : 0]),
    patterns.HitPattern(0), # 1 hit left
    patterns.HitPattern(1), # 2 hits left
    patterns.HitPattern(2), # 3 hits left
    patterns.AllianceStation(),
    ledDriving.LEDPattern([lambda pixels, index : consts.RED_ALLIANCE_COLOR]),
    ledDriving.LEDPattern([lambda pixels, index : consts.BLUE_ALLIANCE_COLOR]),
    patterns.Rainbow([lambda pixels, index : consts.FULL_BATTERY_COLOR]), # placeholder
]

def changePattern(index) :
    ledControl.setPattern(LED_PATTERNS[index])

# initialize
ledControl = ledDriving.LEDControl(pin=consts.LED_SIG_PIN, n=consts.LED_NUMBER, brightness=consts.BRIGHTNESS)