import neopixel

class LEDPattern :

    def __init__(self, patterns: list) :
        self.patterns = patterns

    def writePixels(self, pixels: neopixel.NeoPixel) :
        for pattern in self.patterns :
            for index in range(len(pixels)) :
                pixels[index] = pattern(pixels[index], index)

class LEDControl(neopixel.NeoPixel) :

    def __init__(self, pin, n: int, brightness: float) :
        super().__init__(pin=pin, n=n, brightness=brightness, auto_write=False)

    def setPattern(self, pattern: LEDPattern) :
        self.__pattern = pattern

    def writePattern(self) :
        self.__pattern.writePixels(self)