from redesigned_barnacle.mock import MockFramebuffer
from redesigned_barnacle.sparkline import Sparkline
from unittest import TestCase


class SparkTest(TestCase):
  def test_line(self):
    sl = Sparkline(32, 64)
    sl.push(16)
    sl.draw(MockFramebuffer(), 0, 0)