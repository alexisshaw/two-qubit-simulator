"""
Contains the CNOT gate
"""

from .quantum_gate import QuantumGate
from .pauli import Pauli
frim .controlled_gate import ControlledGate

class CNOT(QuantumGate):
    """ Implements the CNOT gate """

    def __init__(self):
        pauli_x = Pauli("X");
        controlled_pauli_x = ControlledGate(pauli_x)
        QuantumGate.__init__(self, controlled_pauli_x)
