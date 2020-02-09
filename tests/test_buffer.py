from redesigned_barnacle.buffer import CircularBuffer
from random import random
from unittest import TestCase


class CircularTest(TestCase):
  def test_range(self):
    buffer = CircularBuffer()
    self.assertEqual(buffer.range(), 64)

  def test_push(self):
    buffer = CircularBuffer()
    pos = buffer.position()
    val = random()
    buffer.push(val)
    self.assertEqual(buffer.get(pos), val)
    self.assertEqual(buffer.position(), pos + 1)

  def test_sample(self):
    buffer = CircularBuffer(capacity=2, oversample=4)
    buffer.push(0)
    buffer.push(10)

    self.assertEqual(buffer.sample(0), 0.0)
    self.assertEqual(buffer.sample(1), 2.5)
    self.assertEqual(buffer.sample(2), 5.0)
    self.assertEqual(buffer.sample(3), 7.5)
    self.assertEqual(buffer.sample(4), 10.0)
    self.assertEqual(buffer.sample(8), 0.0)
    self.assertEqual(buffer.sample(12), 10.0)