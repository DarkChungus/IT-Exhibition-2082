import matplotlib.pyplot as plt

plt.ion()
fig, ax = plt.subplots()
x_data1, y_data1, x_data2, y_data2, x_data3, y_data3, x_data4, y_data4 = [], [], [], [], [], [], [], []
line, = ax.plot(x_data1, y_data1)

x1, y1 = 4, 0
x2, y2 = 5, 0
x3, y3 = 6, 0
x4, y4 = 7, 0

for t in range(1000):
    dt = 0.01
    dx1 = (x1 - (1/3)*(x1**3) - y1)*dt
    dy1 = x1*dt
    x1 = x1 + dx1
    y1 = y1 + dy1
    x_data1.append(x1)
    y_data1.append(y1)
    dx2 = (x2 - (1/3)*(x2**3) - y2)*dt
    dy2 = x2*dt
    x2 = x2 + dx2
    y2 = y2 + dy2
    x_data2.append(x2)
    y_data2.append(y2)
    dx3 = (x3 - (1/3)*(x3**3) - y3)*dt
    dy3 = x3*dt
    x3 = x3 + dx3
    y3 = y3 + dy3
    x_data3.append(x3)
    y_data3.append(y3)
    dx4 = (x4 - (1/3)*(x4**3) - y4)*dt
    dy4 = x4*dt
    x4 = x4 + dx4
    y4 = y4 + dy4
    x_data4.append(x4)
    y_data4.append(y4)
    line.set_data(x_data1, y_data1)
    line.set_data(x_data2, y_data2)
    line.set_data(x_data3, y_data3)
    line.set_data(x_data4, y_data4)
    ax.plot(x_data1, y_data1, color='r')
    ax.plot(x_data2, y_data2, color='g')
    ax.plot(x_data3, y_data3, color='b')
    ax.plot(x_data4, y_data4, color='y')

plt.ioff()
plt.show()
