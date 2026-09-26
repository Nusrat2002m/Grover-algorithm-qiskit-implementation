import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, transpile
from qiskit.visualization import plot_histogram
from qiskit_aer import AerSimulator

# 1. 3qbit circuit make
qc = QuantumCircuit(3, 3)

# Superposition
qc.h([0, 1, 2])
qc.barrier()

# Oracle (Target state: |101>)
qc.x(1)
qc.h(2)
qc.mcx([0, 1], 2)
qc.h(2)
qc.x(1)
qc.barrier()

# Diffuser
qc.h([0, 1, 2])
qc.x([0, 1, 2])
qc.h(2)
qc.mcx([0, 1], 2)
qc.h(2)
qc.x([0, 1, 2])
qc.h([0, 1, 2])
qc.barrier()

# Measurement
qc.measure([0, 1, 2], [0, 1, 2])

# 2. run simulator
simulator = AerSimulator()
compiled_circuit = transpile(qc, simulator)
job = simulator.run(compiled_circuit, shots=1024)
result = job.result()
counts = result.get_counts()

print("Measurement Counts:", counts)

plot_histogram(counts)
