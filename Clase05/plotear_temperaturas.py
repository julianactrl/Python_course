import matplotlib.pyplot as plt
import numpy as np

def plotear_temperaturas():
    temperaturas = np.load('../Data/temperaturas.npy')
    plt.hist(temperaturas,bins=22)
    plt.show()

print(plotear_temperaturas())