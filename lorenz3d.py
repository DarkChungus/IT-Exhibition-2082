import matplotlib.pyplot as plt


plt.ion()
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x_data, y_data, z_data = [], [], []
rho = 28
sigma = 10
beta = 8/3
x = 0.01
y = 0
z = 0
for i in range(10000):
    dt = 0.01
    dx = sigma * (y-x) * dt
    dy = (x * (rho - z) - y) * dt
    dz = (x*y - beta*z) * dt
    x = x + dx
    y = y + dy
    z = z + dz
    x_data.append(x)
    y_data.append(y)
    z_data.append(z)
    ax.clear()
    ax.scatter(x_data, y_data, z_data, c=z_data, cmap='viridis')
    plt.draw()
    plt.pause(0.0001)
plt.ioff()
plt.show()
