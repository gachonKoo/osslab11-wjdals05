"""
tester.py

geo 패키지 안의 함수들이 제대로 동작하는지 확인하는 간단한 테스트 스크립트입니다.
"""

from geo import distance, circle_area, triangle_area, midpoint


def main() -> None:
    p1 = (0.0, 0.0)
    p2 = (3.0, 4.0)
    p3 = (4.0, 0.0)
    p4 = (0.0, 3.0)

    d = distance(p1, p2)
    c_area = circle_area(1.0)
    t_area = triangle_area(p1, p3, p4)
    mid = midpoint(p1, p2)

    # 출력 형식은 단순히 값만 한 줄씩 출력
    print(d)        # 5.0
    print(c_area)   # 3.14159...
    print(t_area)   # 6.0
    print(mid)      # (1.5, 2.0) 아님 (2.0, 2.666...) → 실제 값 확인


if __name__ == "__main__":
    main()
