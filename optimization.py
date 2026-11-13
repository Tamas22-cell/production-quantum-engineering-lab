"""Small, reproducible VQE and QAOA examples using Qiskit Statevector.

Educational simulations; not financial advice or hardware benchmarks.
"""
import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector, SparsePauliOp


def vqe_circuit(theta):
    """One-qubit Ry ansatz for H = Z."""
    qc = QuantumCircuit(1)
    qc.ry(float(theta), 0)
    return qc


def vqe_energy(theta):
    state = Statevector.from_instruction(vqe_circuit(theta))
    return float(np.real(state.expectation_value(SparsePauliOp.from_list([("Z", 1.0)]))))


def solve_vqe(grid_points=181):
    """Deterministic grid search; returns angle and estimated ground energy."""
    if grid_points < 2:
        raise ValueError("grid_points must be >= 2")
    angles = np.linspace(0, 2 * np.pi, grid_points)
    energies = np.array([vqe_energy(t) for t in angles])
    index = int(np.argmin(energies))
    return {"theta": float(angles[index]), "energy": float(energies[index])}


def portfolio_cost(bits, returns=(0.12, 0.08), risk_penalty=0.04, budget_penalty=1.0):
    """Toy two-asset binary allocation objective (lower is better)."""
    if len(bits) != 2 or any(b not in (0, 1) for b in bits):
        raise ValueError("bits must be two binary values")
    if len(returns) != 2:
        raise ValueError("returns must have length 2")
    x0, x1 = bits
    return float(-returns[0] * x0 - returns[1] * x1
                 + risk_penalty * x0 * x1
                 + budget_penalty * (x0 + x1 - 1) ** 2)


def qaoa_circuit(gamma, beta):
    """One-layer QAOA for the diagonal toy portfolio cost Hamiltonian."""
    qc = QuantumCircuit(2)
    qc.h([0, 1])
    # Apply diagonal cost phases exactly in the computational basis.
    from qiskit.circuit.library import DiagonalGate
    costs = [portfolio_cost((i & 1, (i >> 1) & 1)) for i in range(4)]
    qc.append(DiagonalGate([np.exp(-1j * gamma * c) for c in costs]), [0, 1])
    qc.rx(2 * beta, [0, 1])
    return qc


def qaoa_expected_cost(gamma, beta):
    probabilities = Statevector.from_instruction(qaoa_circuit(gamma, beta)).probabilities()
    return float(sum(probabilities[i] * portfolio_cost((i & 1, (i >> 1) & 1))
                     for i in range(4)))


def solve_qaoa(grid_points=21):
    """Deterministic parameter sweep, returning best bitstring and expected cost."""
    if grid_points < 2:
        raise ValueError("grid_points must be >= 2")
    best = None
    for gamma in np.linspace(0, 2 * np.pi, grid_points):
        for beta in np.linspace(0, np.pi, grid_points):
            cost = qaoa_expected_cost(gamma, beta)
            if best is None or cost < best["expected_cost"]:
                probs = Statevector.from_instruction(qaoa_circuit(gamma, beta)).probabilities()
                best = {"gamma": float(gamma), "beta": float(beta),
                        "expected_cost": cost,
                        "most_likely_bits": [int(np.argmax(probs) & 1),
                                            int((np.argmax(probs) >> 1) & 1)]}
    return best


if __name__ == "__main__":
    print("VQE:", solve_vqe())
    print("QAOA toy portfolio:", solve_qaoa())
