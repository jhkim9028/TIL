# 깊이우선탐색(DFS)

## 그래프 탐색 알고리즘

시작 정점에서 간선을 타고 이동할 수 있는 모든 정점을 찾는 알고리즘

핵심 : 관계성

그래프 탐색 알고리즘에는 깊이우선탐색과 너비우선탐색이 있다.

깊이우선탐색(DFS) : 그래프의 깊이를 우선으로 탐색하기 위해 **스택**의 개념을 활용

너비우선탐색(BFD) : 그래프의 너비를 우선으로 탐색하기 위해 **큐**의 개념을 활용

## 깊이우선탐색(Depth-First Search : DFS)

시작 정점으로부터 갈 수 있는 하위 정점까지 가장 깊게 탐색하고, 더 이상 갈 곳이 없다면 마지막 갈림길로 돌아와서 다른 정점을 탐색하며 결국 모든 정점을 방문하는 순회 방법

미로 탈출로 생각하면 이해하기 쉽다.

특징

모든 정점을 방문할 때 유리하다. 따라서 경우의 수, 순열과 조합 문제에서 많이 사용한다.

너비우선탐색에 비해 코드 구현이 간단하다.

단, 모든 정점을 방문할 필요가 없거나 최단 거리를 구하는 경우에는 너비우선탐색이 유리하다.

동작과정

DFS를 하기 전에, 일단 탐색을 진행할 그래프가 필요하다.

그래프는 인접 행렬 혹은 인접 리스트 방식으로 표현할 수 있다.

각 정점을 방문했는지 여부를 판별할 방문 체크 리스트가 필요하다.

사람과 달리 컴퓨터는 각 정점에 방문했는지 여부를 알 수 없다.

따라서 visited 리스트를 따로 선언하여 각 정점을 방문했는지 체크한다.

```python
visited = [False] * n # n은 정점의 개수
```

DFS의 구현방식

```python
visited = [False] * n # 방문 처리 리스트 만들기
def dfs(start):                    
    stack = [start] # 돌아갈 곳을 기록
    visited[start] = True # 시작 정점 방문 처리

    while stack: # 스택이 빌 때까지(돌아갈 곳이 없을때까지) 반복
        cur = stack.pop() # 현재 방문 정점(후입선출)

        for adj in graph[cur]: # 인접한 모든 정점에 대해
            if not visited[adj]: # 아직 방문하지 않았다면
                visited[adj] = True # 방문 처리
                stack.append(adj) # 스택에 넣기
dfs(0) # 0번 정점에서 시작
```
