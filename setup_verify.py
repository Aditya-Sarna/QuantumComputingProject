#!/usr/bin/env python3
"""
Setup and verification script for the quantum computing project.
"""

import sys
import subprocess


def check_python_version():
    """Check if Python version is compatible."""
    print("Checking Python version...")
    version = sys.version_info
    
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print(f"[FAIL] Python {version.major}.{version.minor} detected")
        print("  This project requires Python 3.8 or higher")
        return False
    
    print(f"[PASS] Python {version.major}.{version.minor}.{version.micro} detected")
    return True


def check_dependencies():
    """Check if all required packages are installed."""
    print("\nChecking dependencies...")
    
    required_packages = {
        'qiskit': 'Qiskit',
        'matplotlib': 'Matplotlib',
        'numpy': 'NumPy',
    }
    
    all_installed = True
    for module, name in required_packages.items():
        try:
            __import__(module)
            print(f"[PASS] {name} is installed")
        except ImportError:
            print(f"[FAIL] {name} is not installed")
            all_installed = False
    
    return all_installed


def verify_qiskit():
    """Verify Qiskit installation and functionality."""
    print("\nVerifying Qiskit functionality...")
    
    try:
        from qiskit import QuantumCircuit
        from qiskit.primitives import StatevectorSampler
        
        # Create a simple circuit
        qc = QuantumCircuit(1, 1)
        qc.h(0)
        qc.measure(0, 0)
        
        # Run it
        sampler = StatevectorSampler()
        job = sampler.run([qc], shots=100)
        result = job.result()
        counts = result[0].data.c.get_counts()
        
        if '0' in counts and '1' in counts:
            print("[PASS] Qiskit is working correctly")
            return True
        else:
            print("[FAIL] Qiskit test failed - unexpected results")
            return False
            
    except Exception as e:
        print(f"[FAIL] Qiskit verification failed: {e}")
        return False


def run_quick_test():
    """Run a quick test of the quantum experiments."""
    print("\nRunning quick functionality test...")
    
    try:
        from test_quantum import run_all_tests
        
        # Suppress output during test
        import io
        from contextlib import redirect_stdout
        
        with redirect_stdout(io.StringIO()):
            success = run_all_tests()
        
        if success:
            print("[PASS] All tests passed")
            return True
        else:
            print("[FAIL] Some tests failed")
            return False
            
    except Exception as e:
        print(f"[FAIL] Test execution failed: {e}")
        return False


def print_summary():
    """Print project information."""
    print("\n" + "=" * 70)
    print("     QUANTUM COMPUTING PROJECT - SETUP COMPLETE")
    print("=" * 70)
    print("\nProject Structure:")
    print("  • quantum_experiments.py - Main experiments module")
    print("  • quantum_utils.py       - Utility functions")
    print("  • examples.py            - Usage examples")
    print("  • test_quantum.py        - Validation tests")
    print("\nQuick Start:")
    print("  Run all experiments:")
    print("    python quantum_experiments.py")
    print("\n  Run examples:")
    print("    python examples.py")
    print("\n  Run tests:")
    print("    python test_quantum.py")
    print("\nFor more information, see README.md")
    print("=" * 70)


def main():
    """Run setup verification."""
    print("=" * 70)
    print("     QUANTUM COMPUTING PROJECT - SETUP VERIFICATION")
    print("=" * 70)
    
    checks = [
        check_python_version(),
        check_dependencies(),
        verify_qiskit(),
        run_quick_test(),
    ]
    
    print("\n" + "=" * 70)
    if all(checks):
        print("[SUCCESS] Setup verification completed successfully!")
        print("=" * 70)
        print_summary()
        return 0
    else:
        print("[FAILED] Setup verification failed")
        print("=" * 70)
        print("\nPlease install missing dependencies:")
        print("  pip install -r requirements.txt")
        return 1


if __name__ == "__main__":
    sys.exit(main())
