from random import choice


class RandomWalk:
    """
    Класс генерирования случайных блужданий
    """
    def __init__(self, num_points=5000):
        self.num_points = num_points

        # Все блуждания начинаются с точки (0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """
        Вычисляет все точки блуждания
        """
        # Шаги генерируются до достижения нужной длины
        while len(self.x_values) < self.num_points:

            # Определение направления и пути движения
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
            y_step = y_direction * y_distance

            # Отклонение нуелвых перемещений (блуждание остановится, но цикл продолжится)
            if x_step == 0 or y_step == 0:
                continue

            # Вычисление следующего шага (последний + следующий)
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)
