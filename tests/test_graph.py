from redesigned_barnacle.buffer import CircularBuffer
from redesigned_barnacle.graph import Sparkline
from redesigned_barnacle.mock import MockFramebuffer
from unittest import TestCase


class SparkTest(TestCase):
  def test_line(self):
    buf = CircularBuffer()
    sl = Sparkline(32, 64, buf)
    sl.push(16)
    sl.draw(MockFramebuffer(), 0, 0)