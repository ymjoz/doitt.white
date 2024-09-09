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

    def test_calculate_risk_level(self):
        self.assertEqual(Risk.calculate_risk_level(6, '檢警調通知', '極高'), '高度風險')
        self.assertEqual(Risk.calculate_risk_level(4, '金融機構通知', '高'), '中高度風險')
        self.assertEqual(Risk.calculate_risk_level(2, '業者KYC', '中'), '中度風險')
        self.assertEqual(Risk.calculate_risk_level(1, '業者KYC', '中'), '中度風險')
