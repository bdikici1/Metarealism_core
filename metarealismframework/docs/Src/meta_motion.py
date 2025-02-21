import numpy as np
import matplotlib.pyplot as plt

# Zaman ekseni
t = np.linspace(0, 10, 1000)

# Temel hareket fonksiyonları
def linear_motion(t, v=1):
    return v * t

def circular_motion(t, r=1, omega=1):
    return r * np.cos(omega * t), r * np.sin(omega * t)

def stochastic_motion(t, alpha=0.5, sigma=1):
    noise = np.random.normal(0, sigma, size=len(t))
    return alpha * np.cumsum(noise)

def fractal_motion(t):
    return np.sin(t * np.pi) * np.log(t + 1)

# Meta-motion fonksiyonu
def meta_motion(t, w1=0.4, w2=0.3, w3=0.2, w4=0.1):
    x_linear = linear_motion(t)
    x_circular, y_circular = circular_motion(t)
    x_stochastic = stochastic_motion(t)
    x_fractal = fractal_motion(t)

    x_final = w1 * x_linear + w2 * x_circular + w3 * x_stochastic + w4 * x_fractal
    y_final = w2 * y_circular  

    return x_final, y_final

# Simülasyonu çalıştır
x, y = meta_motion(t)
plt.plot(x, y, label="Meta Motion")
plt.legend()
plt.title("Meta-Motion Model")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.show()
