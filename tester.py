from geo import distance, circle_area


def main():
    # c = 5.0 이 나오도록 두 점 설정
    p1 = (0, 0)
    p2 = (3, 4)
    c = distance(p1, p2)

    # area = 314.1592653589793 이 나오도록 반지름 10 사용
    r = 10
    area = circle_area(r)

    # autograder가 기대하는 출력 형식
    print(f"c = {c}")
    print(f"area = {area}")


if __name__ == "__main__":
    main()
