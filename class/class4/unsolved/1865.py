# floyd 사용해서 그냥 하려고 했는데 O(N^3)으로 안 됨
# 인접리스트로 하는 것이 일반적이고 인접행렬을 한다고 달라지지 않음

import sys
input = sys.stdin.readline
# graph 입력받기 -> adjecent list 이용 -> 이것도 플로이드 알고리즘을 이용한다면 O(N^3)