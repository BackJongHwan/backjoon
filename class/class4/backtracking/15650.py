def generate_sequences(N, M):
    def backtrack(start, path):
        # path 길이가 M과 같으면 출력
        if len(path) == M:
            print(" ".join(map(str, path)))
            return
        for i in range(start, N + 1):
            # 현재 숫자를 path에 추가
            path.append(i)
            # 재귀 호출로 다음 숫자 선택
            backtrack(i + 1, path)
            # backtracking을 위해 path에서 숫자 제거
            path.pop()
    # 백트래킹 시작
    backtrack(1, [])
# 입력 받기
N, M = map(int, input().split())

# 수열 생성 및 출력
generate_sequences(N, M)