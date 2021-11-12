import numpy as np
from matplotlib import pyplot as plt
import csv

with open('Grid 1 Cp.csv', mode='r') as grid1cp:
    csv_reader = csv.reader(grid1cp)
    x_cor_grid1cp = []
    grid1cp_plot = []
    for line in csv_reader:
       x_cor_grid1cp.append(eval(line[0]))
       grid1cp_plot.append(eval(line[1]))

with open('Grid 2 Cp.csv', mode='r') as grid2cp:
    csv_reader = csv.reader(grid2cp)
    x_cor_grid2cp = []
    grid2cp_plot = []
    for line in csv_reader:
       x_cor_grid2cp.append(eval(line[0]))
       grid2cp_plot.append(eval(line[1]))

with open('Grid 1 Heat flux.csv', mode='r') as grid1h:
    csv_reader = csv.reader(grid1h)
    x_cor_grid1h = []
    grid1h_plot = []
    for line in csv_reader:
       x_cor_grid1h.append(eval(line[0]))
       grid1h_plot.append(eval(line[1]))


with open('Grid 2 Heat flux.csv', mode='r') as grid2h:
    csv_reader = csv.reader(grid2h)
    x_cor_grid2h = []
    grid2h_plot = []
    for line in csv_reader:
       x_cor_grid2h.append(eval(line[0]))
       grid2h_plot.append(eval(line[1]))


plt.plot(x_cor_grid1cp, grid1cp_plot)
plt.plot(x_cor_grid2cp, grid2cp_plot)
plt.ylabel("Cp")
plt.xlabel("X [m]")
plt.legend(['Grid 1', 'Grid 2'])
plt.show()


plt.plot(x_cor_grid1h, grid1h_plot)
plt.plot(x_cor_grid2h, grid2h_plot)
plt.ylabel("Heat Flux Coefficient [W/(m^2k)]")
plt.xlabel("X [m]")
plt.legend(['Grid 1', 'Grid 2'])
plt.show()

