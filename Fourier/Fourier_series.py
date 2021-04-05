import scipy.integrate as integrate
from scipy.integrate import quad
import scipy.special as special
import numpy as np
from numpy import sqrt, sin, cos, pi
import matplotlib.pyplot as plt
# matplotlib inline


def bies(n, y):
    L = pi
    res1 ,err1 = (quad(lambda x: -y*sin(n*(pi/L)*x), -pi, 0))
    res2 ,err2 = (quad(lambda x: y*sin(n*(pi/L)*x), 0, pi))
    res = (1/L)*(res1 + res2)
    # print(res1, res2, res)
    return float(res)

def fourier_series_square(n, L, x):
    waves = []
    for i in range(1, n, 2):
        ampl = np.asarray([])
        ampl = bies(i, 1)*sin(i*(pi/L)*x)
        waves.append(ampl)
    return waves

def fourier_series_saw(n, L, x):
    waves = []
    for i in range(1, n):
        ampl = np.asarray([])
        ampl = (1/(i*pi))*sin((i*pi*x)/L)
        waves.append(ampl)
    return waves

def draw_graph(amplitudes):
    left, width = 0.1, 0.8
    rect1 = [left, 0.7, width, 0.25]  # left, bottom, width, height
    rect2 = [left, 0.45, width, 0.25]
    rect3 = [left, 0.15, width, 0.3]

    fig = plt.figure(figsize=(16, 6))

    ax1 = fig.add_axes(rect1) 
    ax2 = fig.add_axes(rect2, sharex=ax1)
    ax3 = fig.add_axes(rect3, sharex=ax1)

    time = np.arange(-10, 10, 0.1)
  # x = np.linspace(0, 6.5*np.pi, 200)
    y1 = np.sin(time)
    y2 = np.sin(2*time)
    y3 = np.sin(3*time)

    ax1.plot(time, y1, color='b', lw=2)
    ax2.plot(time, y2, color='g', lw=2)
    # ax3.plot(time, y1+y2+y3, color='r', lw=2)
    ax3.plot(time, amplitudes, color='r', lw=2)

    ax3.get_xaxis().set_ticks([])

    for ax in [ax1, ax2, ax3]:
        ax.hlines(0, -10, 10, color='black')
        ax.vlines(0, -1, 1, color='black')

    for key in ['right', 'top', 'bottom']:
        ax.spines[key].set_visible(False)
          

    plt.xlim(-10, 10)
    ax3.text(2, 0.5, 'Sum signal', fontsize=12)
    plt.show()
 

time = np.arange(-10, 10, 0.1)
waves = fourier_series_saw(100, pi, time )
# waves = fourier_series_square(100, pi, time )
wave = sum(waves)
wave = 0.5-wave
draw_graph(wave)



