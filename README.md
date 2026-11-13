![Production Quantum Engineering Lab](./67ee54b7-e7b7-4370-9acf-20279b98413a.png)

# Production Quantum Engineering Lab

## Overview

Production Quantum Engineering Lab is a Python-based quantum computing project focused on building, simulating, and testing quantum circuits using Qiskit.

The project explores foundational quantum engineering techniques with an emphasis on modular code, reproducible simulations, and automated testing.

## Features

- Quantum circuit simulation
- Bell-state generation
- Quantum measurement analysis
- Probability validation
- Automated unit testing
- Qiskit Aer simulation backend

## Technologies

- Python
- Qiskit
- Qiskit Aer
- Git and GitHub
- Python unittest

## Project Structure

```text
production-quantum-engineering-lab/
├── quantum_engine.py
├── test_quantum_engine.py
└── README.md
```

## Installation

Install the required Python packages:

```bash
pip install qiskit qiskit-aer
```

## Run the Quantum Engine

```bash
python quantum_engine.py
```

## Run Automated Tests

```bash
python test_quantum_engine.py
```

## Validation

The initial Bell-state simulation and probability tests have passed successfully.

The project currently includes two passing automated tests.

## Future Development

Planned improvements include:

- Quantum noise modeling
- GHZ-state validation
- Quantum circuit benchmarking
- Performance monitoring
- Extended automated testing
- Quantum hardware-oriented workflows

## Research Focus

Quantum Computing | Quantum Engineering | Python | Qiskit | Quantum Simulation | Software Testing

## Project Status

Active Development — Initial Engine and Tests Operational


## VQE and QAOA Optimization Examples

The `optimization.py` module provides two small, reproducible examples:

- **VQE:** a one-qubit variational circuit minimizing the expectation value of the Pauli-Z Hamiltonian, with a deterministic angle grid search.
- **QAOA:** a one-layer, two-qubit circuit minimizing a **toy** binary portfolio cost function, using a parameter grid search.

The portfolio example uses illustrative fixed returns, a simple pairwise risk penalty and a one-asset budget constraint. It is not a realistic portfolio model, a quantum advantage claim, or investment advice.

Run the examples:

```bash
python optimization.py
```

Run all tests (including VQE and QAOA):

```bash
python -m unittest discover -v
```

The GitHub Actions workflow runs these tests automatically on pushes and pull requests. Check the Actions tab for the latest run result; a successful commit alone does not confirm tests passed.
