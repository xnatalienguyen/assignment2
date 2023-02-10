from statistics import NormalDist

class SignalDetection:
    def __init__(self, hits, misses, falseAlarm, correctRejections):
        self.hit = hits
        self.misses = misses
        self.falseAlarm = falseAlarm
        self.correctRejections = correctRejections
        self.hit_rate = hits / (hits + misses)
        self.false_alarm_rate = falseAlarm / (falseAlarm + correctRejections)
    def d_prime(self):
        d = NormalDist().inv_cdf(self.hit_rate) - NormalDist().inv_cdf(self.false_alarm_rate)
        return d
    def criterion(self):
        c = (-0.5) * (NormalDist().inv_cdf(self.hit_rate) + NormalDist().inv_cdf(self.false_alarm_rate))
        return c

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

if __name__ == '__main__':
    unittest.main()
