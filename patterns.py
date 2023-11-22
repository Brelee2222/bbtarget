import math
from ledDriving import LEDPattern
import consts
import id
import time

allianceColor = consts.RED_ALLIANCE_COLOR if id.isRed() else consts.BLUE_ALLIANCE_COLOR

class Solid(LEDPattern) :
    def __init__(self, color: int) :
        self.__color = color
    
    def range(self, n: int) :
        return range(n)
    
    def getPixel(self, index) :
        return self.__color

class FinalsWin(LEDPattern) :
    __blinkSpeed = 0.5

    def __init__(self, redWin) :
        if redWin :
            self.__winColor = consts.RED_ALLIANCE_COLOR
            # self.__loseColor = consts.BLUE_ALLIANCE_COLOR
        else :
            self.__winColor = consts.BLUE_ALLIANCE_COLOR
            # self.__loseColor = consts.RED_ALLIANCE_COLOR

    def range(self, n: int) :
        return range(n)
    
    def getPixel(self, index) :
        return self.__winColor if index & 0b1 and (time.time() / self.__blinkSpeed % 2) > 1 else 0x646464

class AllianceWin(LEDPattern) :
    __blinkSpeed = 0.5

    def __init__(self, redWin) :
        if redWin :
            self.__winColor = consts.RED_ALLIANCE_COLOR
            # self.__loseColor = consts.BLUE_ALLIANCE_COLOR
        else :
            self.__winColor = consts.BLUE_ALLIANCE_COLOR
            # self.__loseColor = consts.RED_ALLIANCE_COLOR

    def range(self, n: int) :
        return range(n)
    
    def getPixel(self, index) :
        return self.__winColor if index & 0b1 and (time.time() / self.__blinkSpeed % 2) > 1 else 0x646464

class AllianceStation(LEDPattern) :

    __ledSpeed = 5

    def __init__(self) :
        self.__lastLedIndex = 0
        self.__stationID = id.getNumberID()

    def range(self, n) :
        lastLEDIndex = self.__lastLedIndex
        self.__lastLedIndex = (math.floor(time.time() * self.__ledSpeed) % n) - n
        return range(lastLEDIndex, self.__lastLedIndex + self.__stationID)

    def getPixel(self, index) :
        index -= self.__lastLedIndex
        return allianceColor if 0 <= index and index > self.__stationID else 0

class HitPattern(LEDPattern) :

    def __init__(self, timesHit) :
        self.__skips = 1 << timesHit

    def range(self, n: int):
        return range(0, n, self.__skips)

    def getPixel(self, index) :
        return allianceColor