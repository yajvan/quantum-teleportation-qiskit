from qiskit.quantum_info import Statevector
from qiskit_aer import AerSimulator

def verify(qc):

    sim = AerSimulator(method='statevector')
    qc.save_statevector()

    result = sim.run(qc).result()
    final_state = result.get_statevector()

    return final_state
