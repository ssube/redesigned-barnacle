from redesigned_barnacle.buffer import CircularBuffer


class Sparkline():
  def __init__(self, height, width, samples=16):
    oversample = int(width / samples)
    self._buffer = CircularBuffer(capacity=samples, oversample=oversample)
    self._height = height
    self._width = width

  def draw(self, fb, x, y):
    val = self._buffer.get(self._buffer.position() - 1)
    dist = (val / self._height) * self._width

    fb.fill_rect(x, y, self._height, self._width, 0x00)
    fb.hline(x, int(y + (self._height / 2)), int(dist), 0xff)

  def push(self, value):
    self._buffer.push(value)