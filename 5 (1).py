import itertools
from collections import defaultdict


class Solution:
    def __init__(self, filename):
        self.segments = []
        self.read_segments(filename)

    def read_segments(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                x1, y1, x2, y2, index = map(float, line.split())
                self.segments.append(((x1, y1), (x2, y2), int(index)))

    def area_ratio(self):
        ratios = []
        for (x1, y1), (x2, y2), index in self.segments:
            if x1 > x2:
                x1, x2 = x2, x1
            if y1 > y2:
                y1, y2 = y2, y1

            area_left = x1 * y1
            area_right = 1 - x2 * y2
            area_top = (1 - y2) * (x2 - x1)
            area_bottom = y1 * (x2 - x1)

            total_area = 1
            ratio = (area_left + area_right + area_top + area_bottom) / total_area
            ratios.append((index, ratio))

        return ratios

    def intersect(self, p1, p2, p3, p4):
        """ Return the intersection point of two lines (if it exists) """
        denom = (p4[0] - p3[0]) * (p2[1] - p1[1]) - (p2[0] - p1[0]) * (p4[1] - p3[1])
        if denom == 0:
            return None  # Parallel lines

        ua = ((p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])) / denom
        ub = ((p4[0] - p3[0]) * (p3[1] - p1[1]) - (p4[1] - p3[1]) * (p3[0] - p1[0])) / denom

        if 0 <= ua <= 1 and 0 <= ub <= 1:
            x = p1[0] + ua * (p2[0] - p1[0])
            y = p1[1] + ua * (p2[1] - p1[1])
            return (x, y)
        return None

    def find_intersections(self):
        intersection_points = defaultdict(int)
        for (p1, p2, idx1), (p3, p4, idx2) in itertools.combinations(self.segments, 2):
            point = self.intersect(p1, p2, p3, p4)
            if point and 0 <= point[0] <= 1 and 0 <= point[1] <= 1:
                intersection_points[point] += 1

        return intersection_points

    def find_triple_intersections(self):
        intersection_points = self.find_intersections()
        triple_intersections = [point for point, count in intersection_points.items() if count >= 3]

        if triple_intersections:
            return triple_intersections
        else:
            print("Таких точек не найдено")
            return []


def write_segments_to_file(filename):
    segments = [
        (0.1, 0.2, 0.4, 0.5, 1),  # x1, y1, x2, y2, index
        (0.2, 0.3, 0.6, 0.7, 2),
        (0.3, 0.1, 0.5, 0.4, 3),
        (0.4, 0.5, 0.8, 0.2, 4),
        (0.7, 0.6, 0.9, 0.9, 5)
    ]

    with open(filename, 'w') as file:
        for segment in segments:
            line = ' '.join(map(str, segment)) + '\n'
            file.write(line)


# Запись координат в файл
filename = 'segments.txt'
write_segments_to_file(filename)

# Создание объекта класса Solution и вывод результатов
solution = Solution(filename)

# Вывод соотношений площадей
area_ratios = solution.area_ratio()
print("Соотношения площадей для каждого отрезка:")
for index, ratio in area_ratios:
    print(f"Отрезок {index}: Соотношение площадей = {ratio:.4f}")

# Вывод точек пересечения, где пересекаются минимум три отрезка
triple_intersections = solution.find_triple_intersections()
if triple_intersections:
    print("Точки пересечения, где пересекаются минимум три отрезка:")
    for point in triple_intersections:
        print(point)
