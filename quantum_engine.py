
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

def main():
    circuit = QuantumCircuit(2, 2)

    circuit.h(0)
    circuit.cx(0, 1)
    circuit.measure([0, 1], [0, 1])

    simulator = AerSimulator()
    result = simulator.run(circuit, shots=1024).result()

    print("Production Quantum Engineering Lab")
    print("Bell State Simulation Results:")
    print(result.get_counts())

if __name__ == "__main__":
    main()
