import matplotlib.pyplot as plt
from random_walk import RandomWalk


# Новые блуждания создаются пока програма активна
while True:

    # Построение случайного блуждания
    rw = RandomWalk(50000)
    rw.fill_walk()

    # Нанесение точек на диаграмму
    plt.style.use('classic')
    # функция figure() - fig управляет шириной, высотой, цветом фона и разрешением диаграммы
    fig, ax = plt.subplots(figsize=(10, 6), dpi=128)

    # Генерируем количество чисел равное количеству блужданий для назначения цвета каждой из этих точек
    point_numbers = range(rw.num_points)

    # cm.Blues - градиент перехода синего цвета, edgecolors - цвет контура точек
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=3)

    # Выделение первой и последней точек
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    # Удаление осей с диаграммы для наглядности
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input('Make another Random Walk? (y/n): ')
    if keep_running == 'n':
        break
