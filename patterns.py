from ledDriving import LEDPattern
import consts
import id
import time

allianceColor = consts.RED_ALLIANCE_COLOR if id.isRed() else consts.BLUE_ALLIANCE_COLOR

class Rainbow(LEDPattern) :
    pass

class AllianceStation(LEDPattern) :

    ledSpeed = 0.5

    def __init__(self) :
        super().__init__()
        self.__stationNumber = id.getNumberID()

    def writePixel(self, pixels, index) :
        index - (((time.time() * self.ledSpeed) % 1) * 30)
        return allianceColor if index >= 0 and index <= self.__stationNumber else 0
        

class HitPattern(LEDPattern) :

    def __init__(self, hitsLeft) :
        super().__init__()
        self.__hitsLeft = hitsLeft

    def writePixel(self, pixels, index) :
        allianceColor if index % 4 < self.__hitsLeft else 0 # Currently, only red is being used.