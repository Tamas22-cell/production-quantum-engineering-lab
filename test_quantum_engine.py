
import unittest

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit_aer import AerSimulator


class TestQuantumEngine(unittest.TestCase):

    def test_bell_state_probabilities(self):
        circuit = QuantumCircuit(2)
        circuit.h(0)
        circuit.cx(0, 1)

        state = Statevector.from_instruction(circuit)
        probabilities = state.probabilities_dict()

        self.assertAlmostEqual(
            probabilities.get("00", 0), 0.5
        )
        self.assertAlmostEqual(
            probabilities.get("11", 0), 0.5
        )
        self.assertAlmostEqual(
            probabilities.get("01", 0), 0.0
        )
        self.assertAlmostEqual(
            probabilities.get("10", 0), 0.0
        )

    def test_bell_state_simulation(self):
        circuit = QuantumCircuit(2, 2)
        circuit.h(0)
        circuit.cx(0, 1)
        circuit.measure([0, 1], [0, 1])

        simulator = AerSimulator()
        result = simulator.run(
            circuit, shots=4096, seed_simulator=42
        ).result()

        counts = result.get_counts()

        self.assertEqual(sum(counts.values()), 4096)
        self.assertEqual(
            set(counts.keys()), {"00", "11"}
        )

        probability_00 = counts["00"] / 4096
        self.assertAlmostEqual(
            probability_00, 0.5, delta=0.05
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
