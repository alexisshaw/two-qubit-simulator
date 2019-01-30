"""
Implements a controlled version of a given gate
"""

import numpy as np
from .quantum_gate import QuantumGate


class ControlledGate(QuantumGate):
    """
    Given a gate, this class implements a controlled version of the given gate.
    """

    def __init__(self, quantum_gate):
        unitary_shape = quantum_gate.unitary_operator.shape
        assert unitary_shape[0] == unitary_shape[1]  # The unitary should be square

        dimension = unitary_shape[0]

        unitary_matrix = np.block([[np.identity(dimension),          np.zeros((dimension, dimension))],
                                   [np.zeros((dimension, dimension), quantum_gate)]])
        QuantumGate.__init__(self, unitary_matrix, " X \n{}".format(quantum_gate.symbol))
