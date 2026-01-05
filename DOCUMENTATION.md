# Quantum Computing Experiments - Detailed Documentation

## Table of Contents
1. [Overview](#overview)
2. [Experiments](#experiments)
3. [Utility Functions](#utility-functions)
4. [API Reference](#api-reference)
5. [Troubleshooting](#troubleshooting)

## Overview

This project provides a comprehensive set of quantum computing experiments built with Qiskit 2.x. All experiments use local simulators and don't require access to real quantum hardware.

## Experiments

### 1. Basic Hadamard Measurement
**File**: `quantum_experiments.py::basic_hadamard_measurement()`

Creates a single qubit in superposition and measures it.

**Circuit**:
```
q_0: ─H─M─
```

**Expected Results**: 50% probability each for |0⟩ and |1⟩

### 2. Identity Operation (H·H = I)
**File**: `quantum_experiments.py::single_qubit_h_h_measurement()`

Demonstrates that two Hadamard gates in succession return to the original state.

**Circuit**:
```
q_0: ─H─H─M─
```

**Expected Results**: 100% probability for |0⟩

### 3. Bell State Creation
**File**: `quantum_utils.py::create_bell_state(variant)`

Creates any of the four maximally entangled Bell states.

**Variants**:
- `phi_plus`: |Φ+⟩ = (|00⟩ + |11⟩)/√2
- `phi_minus`: |Φ-⟩ = (|00⟩ - |11⟩)/√2
- `psi_plus`: |Ψ+⟩ = (|01⟩ + |10⟩)/√2
- `psi_minus`: |Ψ-⟩ = (|01⟩ - |10⟩)/√2

**Example**:
```python
from quantum_utils import create_bell_state
qc = create_bell_state('phi_plus')
```

### 4. GHZ State Experiments
**File**: `quantum_experiments.py::ghz_experiments()`

Creates and analyzes 3-qubit GHZ states: (|000⟩ + |111⟩)/√2

**Measurements**:
- Computational (Z) basis: Only |000⟩ and |111⟩ observed
- X basis: All 8 states possible with equal probability
- With phase flip: Modified distribution showing quantum interference

### 5. Quantum Interference
**File**: `quantum_experiments.py::interference_experiments()`

Demonstrates quantum interference through various phase manipulations.

**Experiments**:
- **Single-qubit**: H·H = Identity
- **Two-qubit baseline**: H·H on both qubits results in |00⟩
- **With Z gates**: Phase flips change interference pattern
- **With CZ gate**: Controlled phase flip affects |11⟩ state

### 6. CNOT Gate Demonstration
**File**: `quantum_experiments.py::cnot_demonstration()`

Shows controlled-NOT gate behavior.

**Circuit**: CNOT(0,1), X(0), CNOT(0,1)
**Result**: Both qubits in |1⟩ state (measured as '11')

## Utility Functions

### `run_circuit_sampler(qc, shots=1000)`
Run a quantum circuit and return measurement counts.

**Parameters**:
- `qc`: QuantumCircuit to execute
- `shots`: Number of measurements (default: 1000)

**Returns**: Dictionary of measurement counts

### `create_bell_state(variant='phi_plus')`
Create a Bell state circuit.

**Parameters**:
- `variant`: 'phi_plus', 'phi_minus', 'psi_plus', or 'psi_minus'

**Returns**: QuantumCircuit

### `create_w_state(n_qubits=3)`
Create a W state for n qubits.

**Parameters**:
- `n_qubits`: Number of qubits (≥2)

**Returns**: QuantumCircuit

### `create_superposition_state(n_qubits)`
Create equal superposition of all basis states.

**Parameters**:
- `n_qubits`: Number of qubits

**Returns**: QuantumCircuit

### `print_statevector(sv, threshold=1e-10)`
Pretty print a quantum statevector.

**Parameters**:
- `sv`: Statevector object
- `threshold`: Minimum amplitude to display

### `compare_circuits(qc1, qc2, label1="Circuit 1", label2="Circuit 2")`
Compare two circuits by computing their fidelity.

**Parameters**:
- `qc1`, `qc2`: QuantumCircuits to compare
- `label1`, `label2`: Labels for output

**Returns**: Boolean (True if circuits are equivalent)

### `get_pauli_expectation(state, pauli_string)`
Calculate expectation value of a Pauli observable.

**Parameters**:
- `state`: Statevector
- `pauli_string`: String like 'XYZ' for Pauli operators

**Returns**: Real number (expectation value)

## API Reference

### Running Experiments

```python
from quantum_experiments import *

# Run individual experiments
basic_hadamard_measurement()
two_qubit_measurement()
ghz_experiments()
interference_experiments()
cnot_demonstration()

# Run all experiments
main()
```

### Creating Custom Circuits

```python
from quantum_utils import *
from qiskit.quantum_info import Statevector

# Create a Bell state
bell = create_bell_state('phi_plus')

# Analyze statevector
sv = Statevector.from_instruction(bell)
print_statevector(sv)

# Create superposition
super_qc = create_superposition_state(3)
```

### Running with Custom Parameters

```python
from quantum_experiments import run_circuit_sampler
from qiskit import QuantumCircuit

# Create custom circuit
qc = QuantumCircuit(2, 2)
qc.h(0)
qc.cx(0, 1)
qc.measure([0, 1], [0, 1])

# Run with custom shot count
counts = run_circuit_sampler(qc, shots=5000)
print(counts)
```

## Troubleshooting

### Import Errors

**Problem**: `ModuleNotFoundError: No module named 'qiskit'`

**Solution**:
```bash
pip install -r requirements.txt
```

### Matplotlib Issues

**Problem**: Plots not displaying

**Solution**:
```python
import matplotlib
matplotlib.use('TkAgg')  # or 'Qt5Agg', 'Agg'
```

**Problem**: "UserWarning: Matplotlib is currently using agg"

**Solution**: Install a GUI backend:
```bash
pip install PyQt5  # or: pip install tkinter
```

### Python Version Issues

**Problem**: "SyntaxError" or compatibility issues

**Solution**: Ensure Python 3.8+:
```bash
python --version
```

### Virtual Environment Issues

**Problem**: Packages not found even after installation

**Solution**: Activate virtual environment:
```bash
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

### Performance Issues

**Problem**: Experiments run slowly

**Solution**: Reduce shot counts in code:
```python
counts = run_circuit_sampler(qc, shots=100)  # instead of 1000+
```

## Best Practices

1. **Always activate virtual environment** before running experiments
2. **Start with examples.py** to understand basic usage
3. **Run test_quantum.py** to verify installation
4. **Modify shot counts** based on your needs (lower = faster, higher = more accurate)
5. **Close matplotlib windows** between experiments to free memory

## Additional Resources

- [Qiskit Documentation](https://qiskit.org/documentation/)
- [Qiskit Tutorials](https://qiskit.org/learn/)
- [Quantum Computing Textbook](https://qiskit.org/textbook/)

## Support

For issues specific to this project, check:
1. Run `python setup_verify.py` to diagnose setup issues
2. Run `python test_quantum.py` to validate functionality
3. Check Python and package versions match requirements
