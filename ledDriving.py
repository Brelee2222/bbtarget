from abc import abstractmethod
import neopixel

class LEDPattern :

    # Sets the initial pixels of the pattern
    @abstractmethod
    def transition(self, pixels: neopixel.NeoPixel) -> None:
        pass

    # Returns the range of leds that should be updated
    @abstractmethod
    def range(self) -> range: # list[[start, stop step]]
        return range(0)

    # Gets the pixel of the given index
    @abstractmethod
    def getPixel(self, index: int) -> int :
        pass

class LEDControl(neopixel.NeoPixel) :
    def clear(self) :
        self.fill(0)

    def setPattern(self, pattern: LEDPattern) :
        self.__pattern = pattern
        pattern.transition(self)

    def writePattern(self) :
        for index in self.__pattern.range() :
            r, g, b, w = self._parse_color(self.__pattern.getPixel(index))
            self._set_item(index, r, g, b, w)