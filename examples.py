"""
Example usage of quantum experiments.

This script demonstrates how to run individual experiments
or customize them for your own use.
"""

from quantum_experiments import (
    basic_hadamard_measurement,
    ghz_experiments,
    interference_experiments,
    cnot_demonstration,
    visualize_circuit_example,
)
from quantum_utils import (
    create_bell_state,
    create_superposition_state,
    print_statevector,
)
from qiskit.quantum_info import Statevector


def example_1_single_experiment():
    """Example 1: Run a single experiment."""
    print("=" * 60)
    print("EXAMPLE 1: Running basic Hadamard measurement")
    print("=" * 60)
    basic_hadamard_measurement()


def example_2_ghz_state():
    """Example 2: Run GHZ experiments."""
    print("\n" + "=" * 60)
    print("EXAMPLE 2: Running GHZ experiments")
    print("=" * 60)
    ghz_experiments()


def example_3_custom_bell_state():
    """Example 3: Create and analyze a custom Bell state."""
    print("\n" + "=" * 60)
    print("EXAMPLE 3: Custom Bell State Analysis")
    print("=" * 60)
    
    # Create different Bell states
    for variant in ['phi_plus', 'phi_minus', 'psi_plus', 'psi_minus']:
        print(f"\n{variant.upper()} Bell State:")
        qc = create_bell_state(variant)
        sv = Statevector.from_instruction(qc)
        print_statevector(sv)


def example_4_superposition():
    """Example 4: Create superposition states."""
    print("\n" + "=" * 60)
    print("EXAMPLE 4: Superposition States")
    print("=" * 60)
    
    for n in [2, 3, 4]:
        print(f"\n{n}-qubit equal superposition:")
        qc = create_superposition_state(n)
        sv = Statevector.from_instruction(qc)
        print_statevector(sv, threshold=0.1)


def main():
    """Run all examples."""
    print("\n" + "=" * 70)
    print("     QUANTUM COMPUTING EXAMPLES")
    print("=" * 70)
    
    # Uncomment the examples you want to run:
    
    example_1_single_experiment()
    # example_2_ghz_state()
    # example_3_custom_bell_state()
    # example_4_superposition()
    
    print("\n" + "=" * 70)
    print("Examples completed! Uncomment more examples in examples.py")
    print("=" * 70)


if __name__ == "__main__":
    main()

