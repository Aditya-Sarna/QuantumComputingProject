# Quantum Computing Experiments

A comprehensive collection of quantum computing experiments using IBM's Qiskit framework, demonstrating fundamental quantum phenomena including superposition, entanglement, and interference.

## Features

- **Basic Quantum Measurements**: Single and multi-qubit Hadamard gate experiments
- **GHZ States**: Generation and measurement of Greenberger-Horne-Zeilinger states in different bases
- **Bell States**: All four Bell states with analysis utilities
- **Quantum Interference**: Demonstrations of interference patterns with phase manipulation
- **CNOT Gate**: Controlled-NOT gate behavior experiments
- **Statevector Analysis**: Amplitude visualization for quantum states
- **Utility Functions**: Helper functions for common quantum operations

## Installation

1. Clone or download this project
2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
# or
venv\Scripts\activate  # On Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Verify installation:
```bash
python setup_verify.py
```

## Usage

### Run All Experiments
```bash
python quantum_experiments.py
```

### Run Examples
```bash
python examples.py
```

### Run Tests
```bash
python test_quantum.py
```

### Use in Your Own Code
```python
from quantum_experiments import ghz_experiments, interference_experiments
from quantum_utils import create_bell_state, print_statevector

# Run specific experiments
ghz_experiments()

# Create custom circuits
bell_circuit = create_bell_state('phi_plus')
```

## Project Structure

```
quantum/
├── quantum_experiments.py  # Main experiments module
├── quantum_utils.py        # Utility functions and helpers
├── examples.py             # Usage examples
├── test_quantum.py         # Validation tests
├── setup_verify.py         # Setup verification script
├── requirements.txt        # Python dependencies
├── README.md              # This file
└── .gitignore            # Git ignore rules
```

## Notes

- Originally designed for Google Colab but adapted for standalone use
- Uses modern Qiskit 2.x API with built-in simulators
- All experiments use local quantum simulators (no real quantum hardware required)
- Visualization plots display automatically when running experiments
- Compatible with Python 3.8 through 3.13

## License

This is an educational project for learning quantum computing concepts.
