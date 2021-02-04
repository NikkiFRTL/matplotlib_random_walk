import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()

# c = color для выбора цвета точек в виде строки 'red' или кортежа (0, 0.8, 0) диапозон от 0 до 1.
ax.scatter(x_values, y_values, c='red', s=10)

# min и max точки по осям x, y
ax.axis([0, 1100, 0, 1100000])

plt.show()
# Сохранить диаграмму в файл
# plt.savefig('name_plt.png' - имя файла, 'bbox_inches='tight' - отсекает пустое пространство, можно опустить)
