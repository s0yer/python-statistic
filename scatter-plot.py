import matplotlib.pyplot as plt

min = 55
max = 555
size = random.randrange(5,55)
lista_random_x = numpy.random.uniform(min, max, size)
lista_random_y = numpy.random.uniform(min, max, size)

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,79,85,90]

plt.scatter(x, y)
plt.scatter(lista_random_x, lista_random_y)
plt.show()