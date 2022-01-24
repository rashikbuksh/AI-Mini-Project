import matplotlib.pyplot as plt
import numpy as np

# Value of x within a range
valx = np.linspace(-15, 12, num=50)
valx1 = np.linspace(-12, 15, num=50)

# assigning y on the value of x
valy = 0.1065 * valx ** 2 + 0.6164 * valx + 3.1565
valy1 = -(0.1065 * valx1 ** 2) + 0.6164 * valx1 - 3.1565

# plotting graph with the values of x and y
plt.figure(num=0, dpi=200)
plt.axhline(0, color='black', alpha=0.5, dashes=[2, 4], linewidth=1)
plt.axvline(0, color='black', alpha=0.5, dashes=[2, 4], linewidth=1)
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.plot(valx, valy)
plt.plot(valx1, valy1)
plt.title("0.1065 * valx ** 2 + 0.6164 * valx + 3.1565\n-(0.1065 * valx1 ** 2) + 0.6164 * valx1 - 3.1565")
plt.show()
