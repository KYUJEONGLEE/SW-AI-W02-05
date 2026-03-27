# 문제 링크 : https://www.acmicpc.net/problem/2252
"""
N명의 학생들을 키 순서대로 줄을 세우려고 한다.
각 학생의 키를 직접 재서 정렬하면 간단하겠지만,
마땅한 방법이 없어서 두 학생의 키를 비교하는 방법을 사용하기로 하였다.
그나마도 모든 학생들을 다 비교해 본 것이 아니고, 일부 학생들의 키만을 비교해 보았다.

일부 학생들의 키를 비교한 결과가 주어졌을 때,
줄을 세우는 프로그램을 작성하시오.

A B 이면 학생 A가 학생 B의 앞에 서야 한다는 의미이다?
=> 화살표 방향이 A -> B ?
"""
import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
graph = {i: [] for i in range(N + 1)}
indegree = {i: 0 for i in range(N + 1)}
answer = []
for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    graph[A].append(B)
    indegree[B] += 1


"""
진입차수가 0인 정점을 먼저 넣는다.
"""


def line(V):
    q = deque()
    # 진입차수가 0인 정점을 찾아야하는데?
    for v in V:
        if v == 0:
            continue
        if indegree[v] == 0:
            q.append(v)

    # 그럼 q에 진입차수가 0인 정점들이 들어와있다.
    while q:
        cur_q = q.popleft()
        answer.append(cur_q)
        for next in graph[cur_q]:
            indegree[next] -= 1
            if indegree[next] == 0:
                q.append(next)

        # 하나 pop 하고 정답 리스트에 삽입한다
        # 다음 해당 노드와 연결된 노드들의 진입차수를 1 감소시킨다.

        # cur_q 가 가리키는 정점의 진입 차수 감소
    return answer


result = line(graph)
print(*result, end='')

"""
위상 정렬 푸는법:
1. 그래프와 진입차수 준비
- 그래프 : A -> B 저장
- 진입차수: B를 1 증가
** A가 B 앞에 서야한다 => A -> B

2. 진입차수 0인 노드를 큐에 전부 넣기
- 진입 차수가 0이라는 것은 앞에 올 사람이 없다는 뜻

3. 큐가 빌 때까지 반복
- 하나 꺼내서 정답에 넣고
- "그 노드가 가리키는 다음 노드" 들의 진입차수를 1 감소
- 감소 결과가 0 이 되면 큐에 넣기
"""
