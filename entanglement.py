from qiskit import QuantumCircuit

def create_entanglement():
    qc = QuantumCircuit(3,2)

    qc.h(1)
    qc.cx(1,2)

    return qc
