from redesigned_barnacle.buffer import CircularBuffer


class GraphEdge:
  TOP = 1
  BOTTOM = -1

class Bar():
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


class Sparkline():
    def __init__(self, height, width, samples=16, edge=GraphEdge.BOTTOM):
        oversample = int(width / samples)
        self._buffer = CircularBuffer(capacity=samples, oversample=oversample)
        self._edge = edge
        self._height = height
        self._width = width

    def draw(self, fb, x, y):
        fb.fill_rect(x, y, self._height, self._width, 0x00)

        for i in range(0, self._width):
            val = self._buffer.sample(i)
            if self._edge == GraphEdge.BOTTOM:
              val = 1 - val

            row_y = int(val * self._height)
            row_h = self._height - row_y
            fb.vline(x + i, y + row_y, row_h, 0xff)

    def push(self, value):
        self._buffer.push(value)
