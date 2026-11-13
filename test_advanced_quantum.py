import unittest
from advanced_quantum import ghz_circuit, ghz_probabilities, noisy_bell_counts


class AdvancedQuantumTests(unittest.TestCase):
    def test_ghz_probabilities(self):
        p = ghz_probabilities(3)
        self.assertAlmostEqual(p.get("000", 0), 0.5)
        self.assertAlmostEqual(p.get("111", 0), 0.5)
        self.assertAlmostEqual(sum(p.values()), 1.0)

    def test_ghz_invalid_size(self):
        with self.assertRaises(ValueError):
            ghz_circuit(1)

    def test_noisy_counts(self):
        counts = noisy_bell_counts(shots=1024)
        self.assertEqual(sum(counts.values()), 1024)
        self.assertTrue(set(counts).issubset({"00", "01", "10", "11"}))

    def test_invalid_noise(self):
        with self.assertRaises(ValueError):
            noisy_bell_counts(error_probability=1.1)


if __name__ == "__main__":
    unittest.main()
