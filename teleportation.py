from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister

def teleport(theta, phi):

    q = QuantumRegister(3, 'q')
    c = ClassicalRegister(2, 'c')
    qc = QuantumCircuit(q, c)

    # Step 1: prepare unknown state
    qc.ry(theta, q[0])
    qc.rz(phi, q[0])

    # Step 2: entanglement
    qc.h(q[1])
    qc.cx(q[1], q[2])

    # Step 3: Bell measurement
    qc.cx(q[0], q[1])
    qc.h(q[0])

    qc.measure(q[0], c[0])
    qc.measure(q[1], c[1])

    # Step 4: Bob correction (NEW METHOD)
    qc.cx(q[1], q[2])
    qc.cz(q[0], q[2])

    return qc
