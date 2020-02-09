class CircularBuffer:
    def __init__(self, capacity=16, oversample=4):
        self._buffer = [0] * capacity
        self._index = 0
        self._capacity = capacity
        self._oversample = oversample

    def get(self, index):
        return self._buffer[index % self._capacity]

    def push(self, value):
        self._buffer[self._index] = value
        self._index = (self._index + 1) % self._capacity

    def position(self):
        return self._index

    def range(self):
        return self._capacity * self._oversample

    def sample(self, position):
        point_a = int(position / self._oversample) % self._capacity
        point_b = (point_a + 1) % self._capacity
        delta = float(position % self._oversample) / self._oversample

        value_a = self._buffer[point_a]
        value_b = self._buffer[point_b]

        return (value_b * delta) + (value_a * (1.0 - delta))
