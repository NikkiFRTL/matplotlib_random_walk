import matplotlib.pyplot as plt


# Для отображения линий
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

# Для отображения точек
x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

# Используемый стиль фона
plt.style.use('seaborn')
fig, ax = plt.subplots()

# Для нанесения на диаграмму точек и их размер
ax.scatter(x_values, y_values, s=100)

# Используемые данные для нанесения линии
ax.plot(input_values, squares, linewidth=3)

# Назначение заголовка диаграммы и меток осей
ax.set_title('Square Numbers', fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Square of Value', fontsize=14)

# Назначение размера шрифта делений на осях
ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()
