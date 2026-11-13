"""Reproducible GHZ and noisy Bell-state experiments."""
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit_aer import AerSimulator
from qiskit_aer.noise import NoiseModel, depolarizing_error


def ghz_circuit(n_qubits=3, measure=False):
    if n_qubits < 2:
        raise ValueError("GHZ state requires at least two qubits")
    qc = QuantumCircuit(n_qubits, n_qubits if measure else 0)
    qc.h(0)
    for i in range(1, n_qubits):
        qc.cx(0, i)
    if measure:
        qc.measure(range(n_qubits), range(n_qubits))
    return qc


def ghz_probabilities(n_qubits=3):
    return Statevector.from_instruction(ghz_circuit(n_qubits)).probabilities_dict()


def noisy_bell_counts(shots=4096, error_probability=0.02, seed=42):
    if shots <= 0:
        raise ValueError("shots must be positive")
    if not 0 <= error_probability <= 1:
        raise ValueError("error_probability must be between 0 and 1")
    qc = ghz_circuit(2, measure=True)
    noise = NoiseModel()
    noise.add_all_qubit_quantum_error(
        depolarizing_error(error_probability, 2), ["cx"]
    )
    result = AerSimulator(noise_model=noise).run(
        qc, shots=shots, seed_simulator=seed
    ).result()
    return result.get_counts()


if __name__ == "__main__":
    print("GHZ probabilities:", ghz_probabilities())
    print("Noisy Bell counts:", noisy_bell_counts())
