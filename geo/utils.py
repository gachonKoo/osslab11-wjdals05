import math

# 두 점 p, q 사이의 거리
def distance(p, q):
    """
    p, q는 (x, y) 형태의 튜플이라고 가정합니다.
    예: distance((0, 0), (3, 4)) -> 5.0
    """
    x1, y1 = p
    x2, y2 = q
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


# 반지름 r인 원의 넓이
def circle_area(r):
    """
    예: circle_area(1) -> math.pi
    """
    return math.pi * (r ** 2)


# 세 점으로 이루어진 삼각형의 넓이 (Shoelace 공식)
def triangle_area(p1, p2, p3):
    """
    p1, p2, p3는 (x, y) 튜플
    예: triangle_area((0, 0), (4, 0), (0, 3)) -> 6.0
    """
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3

    return abs(
        x1 * (y2 - y3)
        + x2 * (y3 - y1)
        + x3 * (y1 - y2)
    ) / 2.0


# 두 점의 중점
def midpoint(p, q):
    """
    예: midpoint((0, 0), (4, 2)) -> (2.0, 1.0)
    """
    x1, y1 = p
    x2, y2 = q
    return ((x1 + x2) / 2.0, (y1 + y2) / 2.0)
