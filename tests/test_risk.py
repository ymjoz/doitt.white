import unittest
from risk import Risk


class TestRisk(unittest.TestCase):
    def setUp(self) -> None:
        print('Start test')

    def tearDown(self) -> None:
        print('End of test')

    def test_init(self):
        risk = Risk('Risk 1', 1)
        self.assertEqual(risk.name, 'Risk 1')
        self.assertEqual(risk.risk_level, 1)

    def test_add_numbers(self):
        self.assertEqual(Risk.add_numbers(1, 2), 3)

    def test_subtract_numbers(self):
        self.assertEqual(Risk.subtract_numbers(2, 1), 1)
