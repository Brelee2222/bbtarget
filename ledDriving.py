from __future__ import annotations
import microcontroller
import neopixel
from abc import abstractmethod

class LEDPattern :

    # Sets the initial pixels of the pattern
    @abstractmethod
    def transition(self, pixels: LEDControl) -> None:
        pass

    @abstractmethod
    def update(self, pixels: LEDControl) -> None:
        pass

class loopbytearray(bytearray) :

    def __init__(self, buffer: bytearray) :
        super().__init__(buffer)

        self.setSize(len(buffer))
        self.setOffset(0) # I have an obsession with private variables

    def setSize(self, size) :
        self.__size = size

    def setOffset(self, offset) :
        self.__offset = offset

    def __getitem__(self, __key) -> int :
        return super().__getitem__((__key + self.__offset) % self.__size)

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

    def setLoopBufferSize(self, size) :
        self._post_brightness_buffer.setSize(size)

    def setLoopBufferOffset(self, offset) :
        self._post_brightness_buffer.setOffset(offset)

    def clear(self) :
        self.fill(0)

    def setPattern(self, pattern: LEDPattern) :
        self.__pattern = pattern
        pattern.transition(self)

    def updatePattern(self) :
        self.__pattern.update(self)