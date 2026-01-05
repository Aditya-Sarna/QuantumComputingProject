"""
Custom quantum circuit utilities and helper functions.
"""

from qiskit import QuantumCircuit, ClassicalRegister
from qiskit.quantum_info import Statevector
import numpy as np


def create_bell_state(variant='phi_plus'):
    """
    Create one of the four Bell states.
    
    Args:
        variant: One of 'phi_plus', 'phi_minus', 'psi_plus', 'psi_minus'
    
    Returns:
        QuantumCircuit representing the Bell state
    """
    qc = QuantumCircuit(2, 2)
    
    if variant == 'phi_plus':
        # |Φ+⟩ = (|00⟩ + |11⟩) / √2
        qc.h(0)
        qc.cx(0, 1)
    elif variant == 'phi_minus':
        # |Φ-⟩ = (|00⟩ - |11⟩) / √2
        qc.h(0)
        qc.z(0)
        qc.cx(0, 1)
    elif variant == 'psi_plus':
        # |Ψ+⟩ = (|01⟩ + |10⟩) / √2
        qc.h(0)
        qc.cx(0, 1)
        qc.x(1)
    elif variant == 'psi_minus':
        # |Ψ-⟩ = (|01⟩ - |10⟩) / √2
        qc.h(0)
        qc.z(0)
        qc.cx(0, 1)
        qc.x(1)
    else:
        raise ValueError(f"Unknown Bell state variant: {variant}")
    
    return qc


def create_w_state(n_qubits=3):
    """
    Create a W state: |W⟩ = (|100...⟩ + |010...⟩ + ... + |00...1⟩) / √n
    
    Args:
        n_qubits: Number of qubits (must be >= 2)
    
    Returns:
        QuantumCircuit representing the W state
    """
    if n_qubits < 2:
        raise ValueError("W state requires at least 2 qubits")
    
    qc = QuantumCircuit(n_qubits)
    
    # Simple construction for 3 qubits
    if n_qubits == 3:
        qc.x(0)
        qc.ch(0, 1)
        qc.ch(0, 2)
        qc.cx(1, 0)
        qc.cx(2, 0)
    else:
        # General case - use recursive construction
        angle = 2 * np.arccos(np.sqrt(1 / n_qubits))
        qc.ry(angle, 0)
        
        for i in range(1, n_qubits):
            angle = 2 * np.arccos(np.sqrt(1 / (n_qubits - i)))
            qc.cry(angle, i - 1, i)
    
    return qc


def create_superposition_state(n_qubits):
    """
    Create an equal superposition of all basis states.
    
    Args:
        n_qubits: Number of qubits
    
    Returns:
        QuantumCircuit with all qubits in superposition
    """
    qc = QuantumCircuit(n_qubits)
    qc.h(range(n_qubits))
    return qc


def measure_all(qc):
    """
    Add measurement operations to all qubits.
    
    Args:
        qc: QuantumCircuit to add measurements to
    
    Returns:
        Modified QuantumCircuit with measurements
    """
    if qc.num_clbits == 0:
        qc.add_register(ClassicalRegister(qc.num_qubits, 'c'))
    qc.measure(range(qc.num_qubits), range(qc.num_qubits))
    return qc


def print_statevector(sv, threshold=1e-10):
    """
    Pretty print a statevector.
    
    Args:
        sv: Statevector object
        threshold: Minimum amplitude to display
    """
    n_qubits = int(np.log2(len(sv.data)))
    print(f"Statevector ({n_qubits} qubits):")
    
    for i, amp in enumerate(sv.data):
        if abs(amp) > threshold:
            basis = f"|{i:0{n_qubits}b}⟩"
            phase = np.angle(amp)
            magnitude = abs(amp)
            
            if abs(phase) < threshold:
                print(f"  {basis}: {magnitude:.4f}")
            else:
                print(f"  {basis}: {magnitude:.4f} * e^(i*{phase:.4f})")


def compare_circuits(qc1, qc2, label1="Circuit 1", label2="Circuit 2"):
    """
    Compare two quantum circuits by computing their statevectors.
    
    Args:
        qc1: First QuantumCircuit
        qc2: Second QuantumCircuit
        label1: Label for first circuit
        label2: Label for second circuit
    
    Returns:
        Boolean indicating if circuits are equivalent
    """
    sv1 = Statevector.from_instruction(qc1)
    sv2 = Statevector.from_instruction(qc2)
    
    # Check if statevectors are equal (up to global phase)
    fidelity = abs(np.dot(np.conj(sv1.data), sv2.data))
    
    print(f"\n{label1}:")
    print_statevector(sv1)
    print(f"\n{label2}:")
    print_statevector(sv2)
    print(f"\nFidelity: {fidelity:.6f}")
    
    return np.isclose(fidelity, 1.0)


def get_pauli_expectation(state, pauli_string):
    """
    Calculate expectation value of a Pauli string on a quantum state.
    
    Args:
        state: Statevector
        pauli_string: String of Pauli operators (e.g., 'XYZ')
    
    Returns:
        Expectation value
    """
    from qiskit.quantum_info import Pauli
    
    pauli_op = Pauli(pauli_string)
    expectation = state.expectation_value(pauli_op)
    return expectation.real
