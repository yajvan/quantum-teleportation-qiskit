from qiskit import QuantumCircuit
import numpy as np

def create_random_state():
    theta = np.random.uniform(0, np.pi)
    phi = np.random.uniform(0, 2*np.pi)

    qc = QuantumCircuit(1)
    qc.ry(theta, 0)
    qc.rz(phi, 0)

    return qc, theta, phi
