import matplotlib.pyplot as plt
import numpy as np


plt.style.use('_mpl-gallery')

def mostrar(x, y):
    fig, ax = plt.subplots()
    x = np.array(x, dtype=float)
    y = np.array(y, dtype=float)
    ax.set_xlabel('Fecha')
    ax.set_ylabel('Máximo')
    ax.set_title('Máximo del Bitcoin a lo largo del tiempo')
    ax.plot(x,y)
    plt.show()
