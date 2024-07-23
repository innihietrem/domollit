import matplotlib.pyplot as plt

points = [(10, 20), (30, 50), (40, 70)]

for point in points:
    plt.scatter(point[0], point[1])

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot of Points')
plt.show()
