"""
Contains the Phase gate
"""

import numpy as np
from .quantum_gate import QuantumGate


class Phase(QuantumGate):
    """ Implements the Phase gate
        This implements the single qubit phase gate one qubit, with
        a phase rotation of 2 * PI * phase.
    """

    def __init__(self, phase):
        complex_phase = np.cos(2*np.pi*phase) + 1j * sin(2*np.pi*phase)
        U = np.array([[1, 0], [0, complex_phase]])
        QuantumGate.__init__(self, U, "[Cphase (2Pi*{})]".format(phase))

