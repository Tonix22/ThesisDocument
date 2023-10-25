import numpy as np
import matplotlib.pyplot as plt

N = 60
A = 4
x = np.arange(1, N + 1, 2)

osic = A * x
near_ml = A * x * (2 + A)
lmmse = 4 * x ** 3 + 3 * x ** 2 + x
phase_net = 5 * x ** 2

plt.figure(figsize=(10, 6))
plt.plot(x, osic, label='OSIC', linestyle='-', marker='o')
plt.plot(x, near_ml, label='NearML', linestyle='--', marker='v')
plt.plot(x, lmmse, label='LMMSE', linestyle='-.', marker='s')
plt.plot(x, phase_net, label='PhaseNet', linestyle=':', marker='p')

plt.yscale('log')
plt.axvline(x=48, color='r', linestyle='--')

plt.xlabel('N')
plt.ylabel('Operations (log scale)')
plt.legend()
plt.title('Big O Benchmark')
plt.show()
