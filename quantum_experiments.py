"""
Quantum Computing Experiments with Qiskit
==========================================
This module contains various quantum computing experiments including:
- Basic quantum measurements
- GHZ state generation
- Interference experiments
- CNOT gate demonstrations
"""

from qiskit import QuantumCircuit, transpile
from qiskit.visualization import plot_histogram, plot_bloch_multivector
from qiskit.primitives import StatevectorSampler
from qiskit.quantum_info import Statevector
import matplotlib.pyplot as plt
import numpy as np


def run_circuit_sampler(qc, shots=1000):
    """
    Run a quantum circuit using StatevectorSampler.
    
    Args:
        qc: QuantumCircuit to execute
        shots: Number of measurement shots
    
    Returns:
        Dictionary of measurement counts
    """
    sampler = StatevectorSampler()
    job = sampler.run([qc], shots=shots)
    result = job.result()
    
    # Extract counts from the BitArray
    bit_array = result[0].data.c
    counts = bit_array.get_counts()
    return counts


def basic_hadamard_measurement():
    """Demonstrates a basic Hadamard gate followed by measurement."""
    print("--- Basic Hadamard Measurement ---")
    qc = QuantumCircuit(1, 1)
    qc.h(0)
    qc.measure(0, 0)

    counts = run_circuit_sampler(qc, shots=1000)
    print("Measurement counts:", counts)
    plot_histogram(counts)
    plt.title("Single Qubit Hadamard Measurement")
    plt.show()


def two_qubit_measurement():
    """Two-qubit measurement with Hadamard gates."""
    print("\n--- Two-qubit Hadamard Measurement ---")
    qc = QuantumCircuit(2, 2)
    qc.h(0)
    qc.h(1)
    qc.measure([0, 1], [0, 1])

    counts = run_circuit_sampler(qc, shots=1000)
    print("Measurement counts:", counts)
    plot_histogram(counts)
    plt.title("Two Qubit Hadamard Measurement")
    plt.show()


def single_qubit_h_h_measurement():
    """Single qubit with two Hadamard gates (H H = Identity)."""
    print("\n--- Single qubit H H measurement (Identity) ---")
    qc = QuantumCircuit(1, 1)
    qc.h(0)
    qc.h(0)
    qc.measure(0, 0)

    counts = run_circuit_sampler(qc, shots=1000)
    print("Measurement counts:", counts)
    print("Expected: Should measure |0> with ~100% probability (H*H = Identity)")
    plot_histogram(counts)
    plt.title("Single Qubit H-H Measurement")
    plt.show()


def run_and_print(qc, shots=1024, show_statevector=False):
    """
    Helper function to run quantum circuit and print results.
    
    Args:
        qc: QuantumCircuit to execute
        shots: Number of measurement shots
        show_statevector: Whether to display statevector amplitudes
    
    Returns:
        Statevector if show_statevector=True, None otherwise
    """
    if shots > 0:
        counts = run_circuit_sampler(qc, shots=shots)
        print("Counts:", counts)
        plot_histogram(counts)
        plt.show()

    if show_statevector:
        # Create circuit without measurements for statevector
        qc_no_meas = qc.remove_final_measurements(inplace=False)
        sv = Statevector.from_instruction(qc_no_meas)
        
        print("Statevector amplitudes (index -> amplitude):")
        for i, amp in enumerate(sv.data):
            if abs(amp) > 1e-10:  # Only show non-zero amplitudes
                print(f"{i:03b} -> {amp}")
        return sv
    return None


def ghz_experiments():
    """GHZ state experiments with different measurement bases."""
    print("\n--- GHZ + Hadamard Interference ---")
    
    # GHZ state measured in computational (Z) basis
    qc_ghz = QuantumCircuit(3, 3)
    qc_ghz.h(0)       # H on qubit 0
    qc_ghz.cx(0, 1)   # entangle q0->q1
    qc_ghz.cx(0, 2)   # entangle q0->q2
    qc_ghz.measure([0, 1, 2], [0, 1, 2])

    print("=== GHZ state measured in computational (Z) basis ===")
    print("Expected: Only |000> and |111> states")
    run_and_print(qc_ghz, shots=2048, show_statevector=False)

    # GHZ statevector (no measurements)
    qc_ghz_sv = QuantumCircuit(3)
    qc_ghz_sv.h(0)
    qc_ghz_sv.cx(0, 1)
    qc_ghz_sv.cx(0, 2)
    print("\n=== GHZ statevector (amplitudes) ===")
    sv = run_and_print(qc_ghz_sv, shots=0, show_statevector=True)

    # GHZ measured in X basis
    qc_ghz_in_x = QuantumCircuit(3, 3)
    qc_ghz_in_x.h(0)
    qc_ghz_in_x.cx(0, 1)
    qc_ghz_in_x.cx(0, 2)
    qc_ghz_in_x.h([0, 1, 2])
    qc_ghz_in_x.measure([0, 1, 2], [0, 1, 2])

    print("\n=== GHZ measured in X basis (H on each qubit before measurement) ===")
    run_and_print(qc_ghz_in_x, shots=2048)

    # GHZ with phase
    qc_ghz_phase = QuantumCircuit(3, 3)
    qc_ghz_phase.h(0)
    qc_ghz_phase.cx(0, 1)
    qc_ghz_phase.cx(0, 2)
    qc_ghz_phase.z(0)
    qc_ghz_phase.h([0, 1, 2])
    qc_ghz_phase.measure([0, 1, 2], [0, 1, 2])

    print("\n=== GHZ with a Z on qubit0, measured in X basis (reveals phase) ===")
    run_and_print(qc_ghz_phase, shots=2048)


def run_show(qc, shots=1024, show_statevector=False):
    """
    Alternative helper to run and show quantum circuit results.
    
    Args:
        qc: QuantumCircuit to execute
        shots: Number of measurement shots
        show_statevector: Whether to display statevector
    
    Returns:
        Statevector if show_statevector=True, None otherwise
    """
    counts = run_circuit_sampler(qc, shots=shots)
    print("Counts:", counts)
    plot_histogram(counts)
    plt.show()

    if show_statevector:
        qc_nom = qc.remove_final_measurements(inplace=False)
        sv = Statevector.from_instruction(qc_nom)
        print("Statevector (ordered |00..0> .. |11..1>):")
        for i, amp in enumerate(sv.data):
            if abs(amp) > 1e-10:  # Only show non-zero amplitudes
                print(f"{i:0{qc.num_qubits}b} -> {amp}")
        return sv
    return None


def interference_experiments():
    """Demonstrates quantum interference with Hadamard gates and phase flips."""
    print("\n--- Interference experiments (H then H, phase flip effect) ---")
    
    # Part A: Single-qubit H then H
    print("\n--- Part A: Single-qubit H then H ---")
    print("Expected: H*H = Identity, so should measure |0> with ~100% probability")
    qc1 = QuantumCircuit(1, 1)
    qc1.h(0)
    qc1.h(0)
    qc1.measure(0, 0)
    run_show(qc1, shots=1024, show_statevector=True)

    H = (1 / np.sqrt(2)) * np.array([[1, 1], [1, -1]])
    print("\nH matrix:\n", H)
    print("\nH @ H (should be Identity):\n", np.round(H.dot(H), 10))

    # Part B: Two-qubit interference
    print("\n--- Part B: Two-qubit interference (phase flip effect) ---")

    # Baseline (no phase)
    qc2_base = QuantumCircuit(2, 2)
    qc2_base.h([0, 1])
    qc2_base.h([0, 1])
    qc2_base.measure([0, 1], [0, 1])
    print("\nBaseline (no phase) — expected result: mostly '00'")
    run_show(qc2_base, shots=2048, show_statevector=True)

    # With per-qubit Z phase
    qc2_phase = QuantumCircuit(2, 2)
    qc2_phase.h([0, 1])
    qc2_phase.z(0)
    qc2_phase.z(1)
    qc2_phase.h([0, 1])
    qc2_phase.measure([0, 1], [0, 1])
    print("\nWith per-qubit Z phase (affects interference) — expected pattern differs from baseline")
    run_show(qc2_phase, shots=2048, show_statevector=True)

    # With CZ phase flip
    qc2_cz = QuantumCircuit(2, 2)
    qc2_cz.h([0, 1])
    qc2_cz.cz(0, 1)
    qc2_cz.h([0, 1])
    qc2_cz.measure([0, 1], [0, 1])
    print("\nWith CZ phase flip on |11> — shows how a targeted phase changes interference")
    run_show(qc2_cz, shots=2048, show_statevector=True)

    print("\nDone — experiments finished.")


def cnot_demonstration():
    """Demonstrates CNOT gate behavior."""
    print("\n--- CNOT gate demonstration ---")
    print("Circuit: CNOT(0,1), X(0), CNOT(0,1)")
    print("Expected: |11> state (both qubits should be 1)")
    
    qc = QuantumCircuit(2, 2)
    qc.cx(0, 1)       # control=0, target=1 should NOT flip (both start at 0)
    qc.x(0)           # flip qubit 0 to 1
    qc.cx(0, 1)       # now qubit 1 should flip to 1
    qc.measure([0, 1], [0, 1])

    counts = run_circuit_sampler(qc, shots=1024)
    print("Counts:", counts)
    plot_histogram(counts)
    plt.title("CNOT Gate Demonstration")
    plt.show()


def visualize_circuit_example():
    """Show how to visualize quantum circuits."""
    print("\n--- Circuit Visualization Example ---")
    
    # Create a simple Bell state circuit
    qc = QuantumCircuit(2, 2)
    qc.h(0)
    qc.cx(0, 1)
    qc.measure([0, 1], [0, 1])
    
    print("Bell State Circuit:")
    print(qc.draw(output='text'))
    
    # Run and show results
    counts = run_circuit_sampler(qc, shots=1000)
    print("\nBell State Measurements:", counts)
    print("Expected: Equal probabilities for |00> and |11>")
    plot_histogram(counts)
    plt.title("Bell State Measurement")
    plt.show()


def main():
    """Run all quantum experiments."""
    print("=" * 70)
    print("     QUANTUM COMPUTING EXPERIMENTS WITH QISKIT")
    print("=" * 70)
    
    try:
        basic_hadamard_measurement()
        two_qubit_measurement()
        single_qubit_h_h_measurement()
        visualize_circuit_example()
        ghz_experiments()
        interference_experiments()
        cnot_demonstration()
        
        print("\n" + "=" * 70)
        print("     ALL EXPERIMENTS COMPLETED SUCCESSFULLY!")
        print("=" * 70)
    except Exception as e:
        print(f"\nError occurred: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
