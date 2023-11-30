import math
from ledDriving import LEDPattern
import consts
import id
import time

allianceColor = consts.RED_ALLIANCE_COLOR if id.isRed() else consts.BLUE_ALLIANCE_COLOR

class Console(LEDPattern) : # might not work due--
    def transition(self, pixels):
        pixels.setLoopBufferOffset(0)
        pixels.setLoopBufferSize(pixels.n)

        half = math.floor(pixels.n/2)

        for index in range(half) :
            pixels[index] = 0

        for index in range(half, pixels.n) :
            pixels[index] = consts.CONSOLE_COLOR

        for index in range(0, 20, 1) :
            pixels[index] = self.__statusColor
    
    def setMessage(self, statusColor: int) :
        self.__statusColor = statusColor

class Solid(LEDPattern) :
    def __init__(self, color: int) :
        self.__color = color

    def transition(self, pixels):
        pixels.setLoopBufferOffset(0)
        pixels.setLoopBufferSize(1)

        pixels[0] = self.__color

class FinalsWin(LEDPattern) : # not done yet
    __blinkSpeed = 0.5
    __ledSpeed = 50

    def __init__(self, redWin) :
        if redWin :
            self.__winColor = consts.RED_ALLIANCE_COLOR
            # self.__loseColor = consts.BLUE_ALLIANCE_COLOR
        else :
            self.__winColor = consts.BLUE_ALLIANCE_COLOR
            # self.__loseColor = consts.RED_ALLIANCE_COLOR

    def toRGB(self, hex) :
        return [hex >> 16, (hex >> 8) & 0xff, hex & 0xff]

    def transition(self, pixels):


        rainbowColors = consts.RAINBOW_COLORS
        rainbowColorsLength = len(rainbowColors)

        n = pixels.n

        prevColor = self.toRGB(rainbowColors[rainbowColorsLength-1])

        for c in range(rainbowColorsLength) :
            nextColor = self.toRGB(rainbowColors[(c+1) % rainbowColorsLength])

            start = math.floor(n * c / rainbowColorsLength)
            end = math.floor(n * (c + 1) / rainbowColorsLength)

            for pixelIndex in range(start, end) :
                progress = (pixelIndex - start) / (end - start)
                pixels[pixelIndex%pixels.n] = (math.floor(nextColor[0] * progress + prevColor[0] * (1 - progress)), math.floor(nextColor[1] * progress + prevColor[1] * (1 - progress)), math.floor(nextColor[2] * progress + prevColor[2] * (1 - progress)))
            
            prevColor = nextColor

    
    def update(self, pixels) :
        # pixels[0] = self.__winColor if time.time() / self.__blinkSpeed % 2 > 1 else 0x646464
        pixels.setLoopBufferOffset(math.floor(time.time() * self.__ledSpeed % pixels.n))

class AllianceWin(LEDPattern) :
    __blinkSpeed = 2

    def __init__(self, redWin) :
        if redWin :
            self.__winColor = consts.RED_ALLIANCE_COLOR
            # self.__loseColor = consts.BLUE_ALLIANCE_COLOR
        else :
            self.__winColor = consts.BLUE_ALLIANCE_COLOR
            # self.__loseColor = consts.RED_ALLIANCE_COLOR

    def transition(self, pixels):
        pixels.setLoopBufferOffset(0)
        pixels.setLoopBufferSize(2)

        pixels.clear() # clearing is not necessary

        pixels[1] = self.__winColor
    
    def update(self, pixels) :
        pixels[0] = self.__winColor if time.time() / self.__blinkSpeed % 2 > 1 else 0x646464

class AllianceStation(LEDPattern) :

    __ledSpeed = 15

    def __init__(self) :
        self.__stationID = id.getNumberID()

    def transition(self, pixels) -> None:
        pixels.setLoopBufferSize(pixels.n)
        pixels.setLoopBufferOffset(0)

        pixels.clear()

        for index in range(self.__stationID) :
            pixels[index] = allianceColor

    def update(self, pixels) :
        pixels.setLoopBufferOffset(math.floor(time.time() * self.__ledSpeed % pixels.n))

class HitPattern(LEDPattern) :

    def __init__(self, timesHit) :
        self.__skips = 1 << timesHit

    def transition(self, pixels):
        pixels.setLoopBufferOffset(0)
        pixels.setLoopBufferSize(self.__skips)

        pixels.clear()

        pixels[0] = allianceColor