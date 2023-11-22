import neopixel

class LEDPattern :

    def range(self) -> range: # list[[start, stop step]]
        pass

    def getPixel(self, index) -> int :
        pass

class LEDControl(neopixel.NeoPixel) :

    def clear(self) :
        self.fill(0)

    def setPattern(self, pattern: LEDPattern) :
        self.__pattern = pattern

    def writePattern(self) :
        for index in self.__pattern.range() :
            r, g, b, w = self._parse_color(self.__pattern.getPixel(index))
            self._set_item(index, r, g, b, w)