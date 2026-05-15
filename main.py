import numpy as np
from teleportation import teleport
from verification import verify

theta = np.random.uniform(0, np.pi)
phi = np.random.uniform(0, 2*np.pi)

qc = teleport(theta, phi)

print("\nQuantum Teleportation Circuit:\n")
print(qc.draw())

state = verify(qc)

print("\nFinal Bob Statevector:\n")
print(state)
