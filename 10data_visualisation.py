import matplotlib.pyplot as plt

x = []
y = []

with open('data.txt', 'r') as f:
    for line in f:
        values = line.split()
        x.append(int(values[0]))
        y.append(int(values[1]))

plt.plot(x, y, marker='o', linewidth=2)
plt.title('Daily Sales Trend')
plt.xlabel('Day')
plt.ylabel('Sales')
plt.grid(True)
plt.show()