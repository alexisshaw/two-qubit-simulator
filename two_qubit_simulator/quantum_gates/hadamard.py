"""
Contains the Hadamard gate
"""

import numpy as np
from .quantum_gate import QuantumGate


class Hadamard(QuantumGate):
    """ Implements the Hadamard gate by delegating to QuantumGate """

    def __init__(self):
        QuantumGate.__init__(self, np.array([[1, 1], [1, -1]]), "[H]")
    pass
