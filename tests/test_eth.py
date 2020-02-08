from jubilant_train.eth import eth_check
from jubilant_train.mock import MockNetwork
from unittest import TestCase


class CheckNetworkTest(TestCase):
    def test_unconnected(self):
        self.assertEqual(
            eth_check(MockNetwork()),
            False,
        )

    def test_connected_nullip(self):
        self.assertEqual(
            eth_check(MockNetwork(connected=True)),
            False,
        )

    def test_connected_withip(self):
        self.assertEqual(
            eth_check(MockNetwork(connected=True, ip='1.1.1.1')),
            True,
        )
