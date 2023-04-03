import numpy as np
import matplotlib.pyplot as plt

N = 60
A = 16
C = 120
x = np.arange(1, N + 1, 2)

osic = A * x
near_ml = A * x * (2 + A)
zero_forcing = x
complex_net = 13 * x ** 2
lmmse = 4 * x ** 3 + 3 * x ** 2 + x
mobile_net = x ** 2 + 2 * x + x * np.log2(x)
polar_net = 10 * x ** 2 + 2 * x
phase_net = 5 * x ** 2
grid_net_square = x ** 2 + x * np.log2(x) + C
grid_net_polar = x ** 2 + x * np.log2(x) + 2*C

plt.figure(figsize=(10, 6))
plt.plot(x, osic, label='OSIC', linestyle='-', marker='o')
plt.plot(x, near_ml, label='NearML', linestyle='--', marker='v')
plt.plot(x, zero_forcing, label='Zero Forcing', linestyle='-.', marker='s')
plt.plot(x, complex_net, label='ComplexNet', linestyle=':', marker='p')
plt.plot(x, lmmse, label='LMMSE', linestyle='-', marker='*')
plt.plot(x, mobile_net, label='MobileNet', linestyle='--', marker='x')
plt.plot(x, polar_net, label='PolarNet', linestyle='-.', marker='D')
plt.plot(x, phase_net, label='PhaseNet', linestyle=':', marker='+')
plt.plot(x, grid_net_square, label='GridNet Square', linestyle='-', marker='.')
plt.plot(x, grid_net_polar, label='GridNet Polar', linestyle='--', marker='1')
plt.yscale('log') 
plt.axvline(x=48, color='r',linestyle='--')

plt.xlabel('N')
plt.ylabel('Operations')
plt.legend()
plt.title('Big O Benchmark')
plt.show()
