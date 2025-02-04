# n = 10^4
# 신발끈 공식 이용
import sys
input = sys.stdin.readline

n = int(input())
points = []
for _ in range(n):
    x, y = map(int ,input().split())
    points.append((x, y))

def shoelace_area(points):
    """
    신발끈 공식을 사용하여 다각형의 면적을 계산하는 함수
    :param points: 다각형 꼭짓점 리스트 (예: [(x1, y1), (x2, y2), ..., (xn, yn)])
    :return: 다각형의 면적
    """
    n = len(points)
    area = 0

    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % n]  # 마지막 점 다음은 첫 점과 연결
        area += (x1 * y2) - (y1 * x2)

    return abs(area) / 2
result = shoelace_area(points)
print(f"{result:.1f}")