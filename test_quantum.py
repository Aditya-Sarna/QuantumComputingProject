"""
Quick tests to validate quantum experiments are working correctly.
"""

import numpy as np
from quantum_experiments import (
    run_circuit_sampler,
    basic_hadamard_measurement,
)
from quantum_utils import create_bell_state, print_statevector
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector


def test_basic_measurement():
    """Test basic measurement functionality."""
    print("Testing basic measurement...")
    qc = QuantumCircuit(1, 1)
    qc.h(0)
    qc.measure(0, 0)
    
    counts = run_circuit_sampler(qc, shots=1000)
    
    # Should have roughly equal distribution
    assert '0' in counts and '1' in counts
    assert 400 < counts.get('0', 0) < 600
    assert 400 < counts.get('1', 0) < 600
    print("[PASS] Basic measurement test passed")


def test_identity():
    """Test that H*H = Identity."""
    print("\nTesting H*H = Identity...")
    qc = QuantumCircuit(1, 1)
    qc.h(0)
    qc.h(0)
    qc.measure(0, 0)
    
    counts = run_circuit_sampler(qc, shots=1000)
    
    # Should always measure |0>
    assert counts.get('0', 0) == 1000
    print("[PASS] Identity test passed")


def test_bell_state():
    """Test Bell state creation."""
    print("\nTesting Bell state...")
    qc = create_bell_state('phi_plus')
    qc.measure(range(2), range(2))
    
    counts = run_circuit_sampler(qc, shots=1000)
    
    # Should only measure |00> and |11>
    assert '00' in counts and '11' in counts
    assert counts.get('01', 0) == 0
    assert counts.get('10', 0) == 0
    print("[PASS] Bell state test passed")


def test_statevector():
    """Test statevector functionality."""
    print("\nTesting statevector...")
    qc = QuantumCircuit(2)
    qc.h(0)
    qc.cx(0, 1)
    
    sv = Statevector.from_instruction(qc)
    
    # Bell state should have amplitude 1/sqrt(2) for |00> and |11>
    expected_amp = 1 / np.sqrt(2)
    assert abs(abs(sv.data[0]) - expected_amp) < 1e-6
    assert abs(abs(sv.data[3]) - expected_amp) < 1e-6
    assert abs(sv.data[1]) < 1e-10
    assert abs(sv.data[2]) < 1e-10
    print("[PASS] Statevector test passed")


def run_all_tests():
    """Run all validation tests."""
    print("=" * 60)
    print("RUNNING VALIDATION TESTS")
    print("=" * 60)
    
    try:
        test_basic_measurement()
        test_identity()
        test_bell_state()
        test_statevector()
        
        print("\n" + "=" * 60)
        print("ALL TESTS PASSED!")
        print("=" * 60)
        return True
    except AssertionError as e:
        print(f"\n[FAIL] Test failed: {e}")
        return False
    except Exception as e:
        print(f"\n[ERROR] Error occurred: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    run_all_tests()
