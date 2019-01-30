"""
Implements a Pauli gate along the desired axis
"""

import numpy as np
from .quantum_gate import QuantumGate


class Pauli(QuantumGate):
    """ Implements the Hadamard gate by delegating to QuantumGate """

    def __init__(self, dimension):
        if dimension == "I":
            QuantumGate.__init__(self, np.identity(2), "---")
        elif dimension == "X":
            QuantumGate.__init__(self, np.array([[0, 1], [1, 0]]), "[X]")
        elif dimension == "Y":
            QuantumGate.__init__(self, np.array([[0, -1j], [1j, 0]]), "[Y]")
        elif dimension == "Z":
            QuantumGate.__init__(self, np.array([[1, 0], [0, -1]]), "[Z]")
        else:
            assert False, "dimension should be \"I\", \"X\", \"Y\", or \"Z\" "
