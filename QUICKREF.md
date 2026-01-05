# Quantum Computing Project - Quick Reference

## Quick Start
```bash
# Setup
python -m venv venv
source venv/bin/activate  # or: venv\Scripts\activate on Windows
pip install -r requirements.txt
python setup_verify.py

# Run experiments
python quantum_experiments.py
python examples.py
python test_quantum.py
```

## File Overview
| File | Purpose |
|------|---------|
| `quantum_experiments.py` | Main experiments (GHZ, Bell, interference, etc.) |
| `quantum_utils.py` | Helper functions (create states, print results) |
| `examples.py` | Usage examples and tutorials |
| `test_quantum.py` | Automated validation tests |
| `setup_verify.py` | Verify installation and dependencies |
| `README.md` | Project overview and getting started |
| `DOCUMENTATION.md` | Detailed documentation and API reference |

## Common Code Patterns

### Run a Single Experiment
```python
from quantum_experiments import basic_hadamard_measurement
basic_hadamard_measurement()
```

### Create and Run Custom Circuit
```python
from qiskit import QuantumCircuit
from quantum_experiments import run_circuit_sampler

qc = QuantumCircuit(2, 2)
qc.h(0)
qc.cx(0, 1)
qc.measure([0, 1], [0, 1])

counts = run_circuit_sampler(qc, shots=1000)
print(counts)
```

### Create Bell State
```python
from quantum_utils import create_bell_state
from qiskit.quantum_info import Statevector

bell = create_bell_state('phi_plus')
sv = Statevector.from_instruction(bell)
print(sv)
```

### Analyze Statevector
```python
from quantum_utils import print_statevector
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)

sv = Statevector.from_instruction(qc)
print_statevector(sv)
```

### Compare Two Circuits
```python
from quantum_utils import compare_circuits
from qiskit import QuantumCircuit

qc1 = QuantumCircuit(1)
qc1.h(0)
qc1.h(0)

qc2 = QuantumCircuit(1)
# Identity (do nothing)

are_equal = compare_circuits(qc1, qc2, "H*H", "Identity")
```

## Common Gates

| Gate | Qiskit Code | Description |
|------|-------------|-------------|
| Hadamard | `qc.h(0)` | Creates superposition |
| X (NOT) | `qc.x(0)` | Bit flip |
| Y | `qc.y(0)` | Y rotation |
| Z | `qc.z(0)` | Phase flip |
| CNOT | `qc.cx(0, 1)` | Controlled-NOT |
| CZ | `qc.cz(0, 1)` | Controlled-Z |
| Measurement | `qc.measure(0, 0)` | Measure qubit to classical bit |

## Expected Results

| Experiment | Expected Outcome |
|------------|------------------|
| Single H gate | 50/50 split between \|0⟩ and \|1⟩ |
| H·H gates | 100% \|0⟩ (identity) |
| Bell state (Φ+) | 50/50 split between \|00⟩ and \|11⟩ |
| GHZ state | 50/50 split between \|000⟩ and \|111⟩ |
| CNOT demo | 100% \|11⟩ |

## Troubleshooting Quick Fixes

| Problem | Quick Fix |
|---------|-----------|
| Import errors | `pip install -r requirements.txt` |
| Wrong Python version | Use Python 3.8+ |
| Plots not showing | `matplotlib.use('TkAgg')` |
| Tests failing | Run `python setup_verify.py` |
| Slow performance | Reduce shot count |

## Key Concepts

**Superposition**: Qubit in combination of \|0⟩ and \|1⟩
- Created by: Hadamard gate (H)
- Visualized by: ~50/50 measurement distribution

**Entanglement**: Qubits correlated, cannot be described independently
- Created by: CNOT on superposition
- Example: Bell states, GHZ states

**Interference**: Quantum amplitudes add/cancel
- Demonstrated by: H·H = Identity
- Key to: Quantum algorithms

**Measurement**: Collapses superposition to definite state
- Result: Classical bit (0 or 1)
- Probabilistic: Based on quantum amplitudes

## Dependencies

```
qiskit>=2.0.0      # Quantum computing framework
matplotlib>=3.7.0  # Plotting and visualization
numpy>=1.24.0      # Numerical computations
```

## Quick Commands

```bash
# Verify everything works
python setup_verify.py

# Run all experiments (with plots)
python quantum_experiments.py

# Run quick examples
python examples.py

# Run tests (no plots)
python test_quantum.py

# Check Python version
python --version

# List installed packages
pip list | grep -i qiskit
```

## Project Statistics

- **7 files**: Main code and documentation
- **10+ experiments**: From basic to advanced
- **15+ utility functions**: For common operations
- **4 Bell states**: All variants implemented
- **100% test coverage**: All core functionality tested

---

**Need more help?** See `DOCUMENTATION.md` for detailed API reference and troubleshooting.
