import microcontroller
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

class loopbytearray(bytearray) :

    def __init__(self) :
        self.__offset = 0 # I have an obsession with private variables

    def setOffset(self, offset) :
        self.__offset = offset

    def __getitem__(self, __key) -> int :
        return super().__getitem__((__key + self.__offset) % len(self))

class LEDControl(neopixel.NeoPixel) :

    def __init__(self, 
        pin: microcontroller.Pin,
        n: int,
        *,
        bpp: int = 3,
        brightness: float = 1,
        auto_write: bool = True,
        pixel_order: str = None
    ) :
        super().__init__(pin=pin, n=n, bpp=bpp,brightness=brightness,auto_write=auto_write,pixel_order=pixel_order)
        self._post_brightness_buffer = loopbytearray(self._post_brightness_buffer)


    def clear(self) :
        self.fill(0)

    def setPattern(self, pattern: LEDPattern) :
        self.__pattern = pattern
        pattern.transition(self)

    def writePattern(self) :
        for index in self.__pattern.range(self.n) :
            r, g, b, w = self._parse_color(self.__pattern.getPixel(index))
            self._set_item(index, r, g, b, w)