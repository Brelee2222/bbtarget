import math
from ledDriving import LEDPattern
import consts
import id
import time

allianceColor = consts.RED_ALLIANCE_COLOR if id.isRed() else consts.BLUE_ALLIANCE_COLOR

class Rainbow(LEDPattern) :
    pass

class AllianceWin(LEDPattern) :
    __blinkSpeed = 0.5

    def __init__(self, redWin) :
        super().__init__([self.writeWinPixel, self.writeLosePixel])
        if redWin :
            self.__winColor = consts.RED_ALLIANCE_COLOR
            self.__loseColor = consts.BLUE_ALLIANCE_COLOR
        else :
            self.__winColor = consts.BLUE_ALLIANCE_COLOR
            self.__loseColor = consts.RED_ALLIANCE_COLOR

    def writeWinPixel(self, pixels, index) :
        return self.__winColor
    
    def writeLosePixel(self, pixels, index) :
        self.__loseColor if index & 0b1 and (time.time() / self.__blinkSpeed % 2) > 1 else 0

class AllianceStation(LEDPattern) :

    ledSpeed = 5

    def __init__(self) :
        super().__init__([self.writePixel])
        self.__stationNumber = id.getNumberID()

    def writePixel(self, pixels, index) :
        index -= math.floor(time.time() * self.ledSpeed)
        ledNumber = math.floor(time.time() * self.ledSpeed - index) % consts.LED_NUMBER
        # ledNumber>>=1
        return allianceColor if ledNumber <= self.__stationNumber else 0

class HitPattern(LEDPattern) :

    def __init__(self, timesHit) :
        super().__init__([self.writePixel])
        self.__n = 1 << timesHit # n is the number describing the n-th LED to turn on. I couldn't think of a good variable name for n.

    def writePixel(self, pixels, index) :
        return allianceColor if index % self.__n == 0 else 0 