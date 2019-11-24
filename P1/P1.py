import math
import numpy as np
import matplotlib.pyplot as plt

f = 60.0
T = 1 / f
fs = 1000
N = 5
A = 1
n = 999

t = np.arange(0, N * T , N * T / float(fs))

some_creepy_wave = np.zeros(fs)

for i in range(n):
    harmonic = 1 / float(2*i+1) / float(2*i+1) * np.sin(2 * math.pi * (2*i+1) * f * t)
    some_creepy_wave += harmonic

sin_t = A * np.sin(2 * math.pi * f * t)

plt.plot(t, sin_t, 'r', label='s1')
plt.savefig('s1.png')

plt.clf()

plt.plot(t, some_creepy_wave, 'b', label='sine wave')
plt.savefig('s2.png')

plt.plot(t, sin_t, 'r', label='s1')
plt.savefig('s1&s2.png')

# plt.show()