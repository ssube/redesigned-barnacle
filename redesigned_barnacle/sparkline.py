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
    print(val, dist)

    fb.fill_rect(x, y, self._height, self._width)
    fb.hline(x, y + 1, dist, 0xff)

  def push(self, value):
    self._buffer.push(value)