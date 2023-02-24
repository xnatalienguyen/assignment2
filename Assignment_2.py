from statistics import NormalDist

class SignalDetection:
    def __init__(self, hits, misses, falseAlarm, correctRejections):
        self.hit = hits
        self.misses = misses
        self.falseAlarm = falseAlarm
        self.correctRejections = correctRejections
        self.hit_rate = hits / (hits + misses)
        self.false_alarm_rate = falseAlarm / (falseAlarm + correctRejections)
        self.hit_dist = NormalDist().inv_cdf(self_hit.rate)
        self.false_dist = NormalDist().inv_cdf(self.false_alarm_rate)
    def d_prime(self):
        d = self.hit_dist - (self.false_dist)
        return d
    def criterion(self):
        c = (-0.5) * ((self.hit_dist) + (self.false_dist))
        return c
    def __add__(self, other):
        return SignalDetection(self.hit + other.hit, self.misses + other.misses, self.falseAlarm + other.falseAlarm, self.correctRejections + other.correctRejections)
    def __mul__(self, scalar):
        return SignalDetection(self.hit * scalar, self.misses * scalar, self.falseAlarm * scalar, self.correctRejections * scalar)

import unittest 

class TestSignalDetection(unittest.TestCase):
    def test_d_prime_zero(self):
        sd   = SignalDetection(15, 5, 15, 5)
        expected = 0
        obtained = sd.d_prime()
        # Compare calculated and expected d-prime
        self.assertAlmostEqual(obtained, expected, places=6)
    def test_d_prime_nonzero(self):
        sd   = SignalDetection(15, 10, 15, 5)
        expected = -0.421142647060282
        obtained = sd.d_prime()
        # Compare calculated and expected d-prime
        self.assertAlmostEqual(obtained, expected, places=6)
    def test_criterion_zero(self):
        sd   = SignalDetection(5, 5, 5, 5)
        # Calculate expected criterion        
        expected = 0
        obtained = sd.criterion()
        # Compare calculated and expected criterion
        self.assertAlmostEqual(obtained, expected, places=6)
    def test_criterion_nonzero(self):
        sd   = SignalDetection(15, 10, 15, 5)
        # Calculate expected criterion        
        expected = -0.463918426665941
        obtained = sd.criterion()
        # Compare calculated and expected criterion
        self.assertAlmostEqual(obtained, expected, places=6)
    def test_addition(self):
        sd = SignalDetection(1, 1, 2, 1) + SignalDetection(2, 1, 1, 3)
        expected = SignalDetection(3, 2, 3, 4).criterion()
        obtained = sd.criterion()
        # Compare calculated and expected criterion
        self.assertEqual(obtained, expected)
    def test_multiplication(self):
        sd = SignalDetection(1, 2, 3, 1) * 4
        expected = SignalDetection(4, 8, 12, 4).criterion()
        obtained = sd.criterion()
        # Compare calculated and expected criterion
        self.assertEqual(obtained, expected)
    def test_corruption(self):
        sd = SignalDetection(1, 2, 3, 1)
        sd.__hits = 5
        sd.__misses = 5
        sd.__correctRejections = 5
        sd.__falseAlarm = 5
        sd.__hit_rate = 5
        sd.__false_alarm_rate = 5
        sd.__hit_dist = 5
        sd.__false_dist = 5
        expected_c = SignalDetection(1, 2, 3, 1).criterion()
        obtained_c = sd.criterion()
        expected_d = SignalDetection(1, 2, 3, 1).d_prime()
        obtained_d = sd.d_prime()
        self.assertEqual(obtained_c, expected_c)
        self.assertEqual(obtained_d, expected_d)

if __name__ == '__main__':
    unittest.main()
