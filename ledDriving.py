from typing import Callable
import neopixel

type Pattern = Callable[[list, int], list[int]]

class LEDPattern :

    def __init__(self, patterns: list[Pattern]) :
        self.patterns = patterns

    def writePixels(self, pixels: neopixel.NeoPixel) :
        for pattern in self.patterns :
            for index in range(len(pixels)) :
                pixels[index] = pattern(pixels[index], index)

class LEDControl(neopixel.NeoPixel) :

    def __init__(self, sigPin, pixels: int, bpp: int, brightness: float) :
        super().__init__(sigPin, pixels, bpp, brightness)

    def setPattern(self, pattern: LEDPattern) :
        self.__pattern = pattern

    def writePattern(self) :
        self.__pattern.writePixels(self)