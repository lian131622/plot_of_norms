import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm


# get the type and shape(if has one) of an variable
def var_info(var, name='', show=0):
    print('-' * 25, name, '-' * 25)
    print('type:', type(var))
    try:
        var.shape
    except AttributeError:
        print('no shape attribute')
    else:
        print('shape:', var.shape)
    try:
        len(var)
    except TypeError:
        print("no length")
    else:
        print('len:', len(var))
    if show == 1:
        print(var)


num = 200
x = np.linspace(-10, 10, num)
x_1, x_2 = np.meshgrid(x, -x)
fx_1 = np.zeros_like(x_1)
fx_2 = np.zeros_like(x_1)
fx_3 = np.zeros_like(x_1)
fx_4 = np.zeros_like(x_1)
fx_5 = np.zeros_like(x_1)
fx_6 = np.zeros_like(x_1)

for i in range(num):
    for j in range(num):
        fx_1[i, j] = np.sqrt(x_1[i, j] ** 2 + x_2[i, j] ** 2) # L-2 Norm
        fx_2[i, j] = (np.sqrt(np.abs(x_1[i, j])) + np.sqrt(np.abs(x_2[i, j])))**2
        fx_3[i, j] = max(10 * x_1[i, j] + x_2[i, j], x_1[i, j] + x_2[i, j], x_1[i, j] + 5 * x_2[i, j])
        fx_4[i, j] = min(10 * x_1[i, j] + x_2[i, j], x_1[i, j] + x_2[i, j], x_1[i, j] + 5 * x_2[i, j])
        fx_5[i, j] = 2 * x_1[i, j] ** 2 + x_2[i, j] ** 2 - 2 * x_1[i, j] * (x_2[i, j] + 1)
        fx_6[i, j] = np.linalg.norm([x_1[i, j], x_2[i, j]], ord=1)


def plot_function(fx):
    fig = plt.figure()
    ax3 = plt.axes(projection='3d')
    ax3.plot_surface(x_1, x_2, fx, cmap=cm.coolwarm, linewidth=0, antialiased=False, alpha=0.4)
    ax3.contour(x_1, x_2, fx, zdir='z', offset=-1, cmap=cm.coolwarm)
    ax3.set_xlabel('X1')
    ax3.set_ylabel('X2')
    # plt.savefig('./function.png')
    plt.show()


plot_function(fx_1)
plot_function(fx_2)
plot_function(fx_3)
plot_function(fx_4)
plot_function(fx_5)
plot_function(fx_6)
