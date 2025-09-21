import matplotlib.pyplot as plt

plt.ion()
fig, ax = plt.subplots()
x_data, y_data = [], []
line, = ax.plot(x_data, y_data)

sigma = 10
rho = 28
beta = 1/3
x = 0.01
y = 0
z = 0

for t in range(10000):
    dt = 0.01
    dx = sigma * (y-x) * dt
    dy = (x * (rho - z) - y) * dt
    dz = (x * y - beta * z) * dt
    x = x + dx
    y = y + dy
    z = z + dz
    x_data.append(x)
    y_data.append(y)
    line.set_data(x_data, y_data)
    ax.relim()
    ax.autoscale_view()
    plt.draw()
    plt.pause(0.01)
plt.ioff()
plt.show()
