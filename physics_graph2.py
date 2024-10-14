import numpy as np
import matplotlib.pyplot as plt

def damped_oscillator(m, k, b, x0, t_max=10, num_points=1000):
    # Compute derived constants
    omega_0 = np.sqrt(k / m)
    gamma = b / m

    # Create time array
    t = np.linspace(0, t_max, num_points)

    A1 = x0 / 2
    A2 = x0 / 2

    # Calculate
    discriminant = (gamma**2 / 4) - omega_0**2
    if discriminant > 0:
        root = np.sqrt(discriminant)
        x_t = np.exp(-gamma * t / 2) * (A1 * np.exp(root * t) + A2 * np.exp(-root * t))
    
    elif discriminant == 0:
        x_t = (A1 + A2 * t) * np.exp(-gamma * t / 2)
    
    else:
        root = np.sqrt(-discriminant)
        x_t = np.exp(-gamma * t / 2) * (A1 * np.cos(root * t) + A2 * np.sin(root * t))

    plt.plot(t, x_t, label=f"m={m} kg")
    plt.xlabel("Time (s)")
    plt.ylabel("Displacement (m)")
    plt.title("Damped Harmonic Oscillator")
    plt.grid(True)
    plt.legend()
    plt.show()


# Constants
m = 5.0
k = 5.0
b = 0.5
x0 = 1.0 

damped_oscillator(m, k, b, x0)
