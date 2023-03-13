""" 
- 나이트, 비숍, 룩
- 1, 2, 3, .. 순서대로 방문하기
- 말 이동시키기 or 말 바꾸기
- N-1 에서 N까지 이동 가능한 최솟값 계산하기

- 나이트 : 이동 가능 8개
- 룩 : x, y 좌표 중 하나가 같으면 한 번에 이동 가능
- 비숍 : x, y 좌표 차이가 같아야 한 번에 이동 가능
    - x, y 좌표 차이의 합이 홀수면 이동 불가능함
"""
from collections import deque

# 1. 입력 받기
N = int(input())    # 체스판 크기
numbers = {}           # '1' : (1, 1)
for i in range(N):
    line = list(map(int, input().split()))
    for j in range(N):
       numbers[line[j]] = (i, j)

# 말 이동 경로
knight = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
rook = [(-1, 0), (1, 0), (0, -1), (0, 1)]
bishop = [(-1, -1), (1, -1), (1, 1), (-1, 1)]

# 나이트, 룩, 비숍
KNIGHT, ROOK, BISHOP = 0, 1, 2

# q : (현재 x좌표, y좌표, 목표 숫자, 체스말, 시간)
x, y = numbers[1]
q = deque([(x, y, 2, KNIGHT, 0), (x, y, 2, ROOK, 0), (x, y, 2, BISHOP, 0)])
visited = set([(x, y, 2, KNIGHT), (x, y, 2, ROOK), (x, y, 2, BISHOP) ])
#visited = [[[[False for _ in range(3)] for _ in range(N ** 2 + 1)] for _ in range(N)] for _ in range(N)]
#visited[x][y][2][KNIGHT] = visited[x][y][2][ROOK] = visited[x][y][2][BISHOP] = True

answer = 0
while q:
    x, y, num, chess, t = q.popleft()

    # 탈출 조건
    if num == N * N + 1:  # 마지막 수 도달
        answer = t
        break

    tx, ty = numbers[num]   # 목표 숫자의 좌표

    # 말 바꾸는 경우
    for i in range(3):
        if i == chess or (x, y, num, i) in visited : continue
        #if i == chess or visited[x][y][num][i]: continue
        
        q.append((x, y, num, i, t+1))
        visited.add((x, y, num, i))
        #visited[x][y][num][i] = True

    if chess == KNIGHT:
        for i in range(8):
            nx, ny = x+knight[i][0], y+knight[i][1]

            if nx < 0 or nx >= N or ny < 0 or ny >= N : break
            if (nx, ny, num, KNIGHT) in visited : continue
            #if visited[ny][ny][num][KNIGHT] : continue

            visited.add((nx, ny, num, KNIGHT))
            #visited[nx][ny][num][KNIGHT] = True
            if nx == tx and ny == ty:   # 목표 숫자 위치에 도달한 경우
                q.append((tx, ty, num+1, KNIGHT, t+1))
            else:
                q.append((nx, ny, num, KNIGHT, t+1))

    elif chess == ROOK:
        for i in range(4):
            nx, ny = x, y
            while 0 <= nx < N and 0 <= ny < N :
                nx, ny = nx+rook[i][0], ny+rook[i][1]

                if nx < 0 or nx >= N or ny < 0 or ny >= N : break
                if (nx, ny, num, ROOK) in visited: continue
                #if visited[nx][ny][num][ROOK] : continue

                visited.add((nx, ny, num, ROOK))
                #visited[nx][ny][num][ROOK] = True
                if nx == tx and ny == ty :
                    q.append((tx, ty, num+1, ROOK, t+1))
                else:
                    q.append((nx, ny, num, ROOK, t+1))

    else:   # BISHOP
        for i in range(4):
            nx, ny = x, y
            while 0 <= nx < N and 0 <= ny < N :
                nx, ny = nx+bishop[i][0], ny+bishop[i][1]
            
                if nx < 0 or nx >= N or ny < 0 or ny >= N : break
                if (nx, ny, num, BISHOP) in visited: continue
                #if visited[nx][ny][num][BISHOP] : continue

                visited.add((nx, ny, num, BISHOP))
                #visited[nx][ny][num][BISHOP] = True
                if nx == tx and ny == ty :
                    q.append((tx, ty, num+1, BISHOP, t+1))
                else :
                    q.append((nx, ny, num, BISHOP, t+1))

print(answer)