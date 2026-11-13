import unittest
import numpy as np
from optimization import (
    vqe_energy, solve_vqe, portfolio_cost,
    qaoa_circuit, qaoa_expected_cost, solve_qaoa
)
from qiskit.quantum_info import Statevector


class OptimizationTests(unittest.TestCase):
    def test_vqe_known_energies(self):
        self.assertAlmostEqual(vqe_energy(0), 1.0, places=7)
        self.assertAlmostEqual(vqe_energy(np.pi), -1.0, places=7)

    def test_vqe_minimum(self):
        self.assertAlmostEqual(solve_vqe()["energy"], -1.0, places=6)

    def test_portfolio_budget_penalty(self):
        self.assertLess(portfolio_cost((1, 0)), portfolio_cost((0, 0)))
        self.assertLess(portfolio_cost((1, 0)), portfolio_cost((1, 1)))

    def test_qaoa_normalization(self):
        probabilities = Statevector.from_instruction(qaoa_circuit(0.7, 0.4)).probabilities()
        self.assertAlmostEqual(float(sum(probabilities)), 1.0)

    def test_qaoa_zero_angles_uniform(self):
        expected = sum(portfolio_cost((i & 1, (i >> 1) & 1)) for i in range(4)) / 4
        self.assertAlmostEqual(qaoa_expected_cost(0, 0), expected)

    def test_qaoa_search(self):
        result = solve_qaoa(grid_points=7)
        self.assertEqual(len(result["most_likely_bits"]), 2)
        self.assertLessEqual(result["expected_cost"], qaoa_expected_cost(0, 0) + 1e-9)


if __name__ == "__main__":
    unittest.main()
