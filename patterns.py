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
    __ledSpeed = 15

    def __init__(self, redWin) :
        if redWin :
            self.__winColor = consts.RED_ALLIANCE_COLOR
            # self.__loseColor = consts.BLUE_ALLIANCE_COLOR
        else :
            self.__winColor = consts.BLUE_ALLIANCE_COLOR
            # self.__loseColor = consts.RED_ALLIANCE_COLOR

    def toRGB(self, hex) :
        return [hex >> 16, (hex >> 8) & 0xff, hex & 0xff]
    
    def transitionColor(self, prev, next, progress, index) :
        return math.floor(next[index] * progress + prev[index] * (1 - progress))

    def transition(self, pixels):
        pixels.setLoopBufferSize(pixels.n)

        rainbowColors = consts.RAINBOW_COLORS
        rainbowColorsLength = len(rainbowColors)

        n = pixels.n

        prevColor = self.toRGB(rainbowColors[rainbowColorsLength-1])

        for c in range(rainbowColorsLength+1) :
            nextColor = self.toRGB(rainbowColors[(c+1) % rainbowColorsLength])

            start = math.floor(n * c / (rainbowColorsLength))
            end = math.floor(n * (c + 1) / (rainbowColorsLength))

            for pixelIndex in range(start, end) :
                progress = (pixelIndex - start) / (end - start)
                pixels[pixelIndex%pixels.n] = self.__winColor if not (pixelIndex % 3) else (
                # pixels[pixelIndex%pixels.n] = (
                    self.transitionColor(prevColor, nextColor, progress, 0), 
                    self.transitionColor(prevColor, nextColor, progress, 1), 
                    self.transitionColor(prevColor, nextColor, progress, 2)
                    )
            
            prevColor = nextColor

    
    def update(self, pixels) :
        # pixels[0] = self.__winColor if time.time() / self.__blinkSpeed % 2 > 1 else 0x646464
        pixels.setLoopBufferOffset(math.floor(time.time() * self.__ledSpeed % pixels.n) * 3)

class AllianceWin(LEDPattern) :
    __blinkSpeed = 3

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
        pixels[0] = self.__winColor if time.time() * self.__blinkSpeed % 2 > 1 else 0x333333

class AllianceStation(LEDPattern) :

    __ledSpeed = 1

    def __init__(self) :
        self.__stationID = id.getNumberID()

    def transition(self, pixels) -> None:
        pixels.setLoopBufferSize(5)
        pixels.setLoopBufferOffset(0)

        pixels.clear()

    def update(self, pixels) :
        brightness = (math.sin(time.time() * self.__ledSpeed) + 1) / 2 * 0.5

        r = math.floor((allianceColor >> 16) * brightness)
        g = math.floor(((allianceColor >> 8) & 0xff) * brightness)
        b = math.floor((allianceColor & 0xff) * brightness)

        for index in range(self.__stationID) :
            pixels[index] = (r, g, b)

class HitPattern(LEDPattern) :

    def __init__(self, timesHit) :
        self.__skips = 1 << timesHit

    def transition(self, pixels):
        pixels.setLoopBufferOffset(0)
        pixels.setLoopBufferSize(self.__skips)

        pixels.clear()

        pixels[0] = allianceColor