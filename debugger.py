import math
import pdb


def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def calculate_slope(x1, y1, x2, y2):
    pdb.set_trace()
    delta_y = y2 - y1
    delta_x = x2 - x1
    return delta_y / delta_x


def calculate_y_intercept(slope, x, y):
    return y - slope * x


def get_line_equation(x1, y1, x2, y2):
    slope = calculate_slope(x1, y1, x2, y2)
    y_intercept = calculate_y_intercept(slope, x1, y1)
    return (slope, y_intercept)


def line_from_two_points(x1, y1, x2, y2):
    slope, y_intercept = get_line_equation(x1, y1, x2, y2)
    return f"y = {slope}x + {y_intercept}"


# print(line_from_two_points(3, 6, 8, 4))
print(line_from_two_points(0, 0, 0, 0))
