# 문제 링크: https://www.acmicpc.net/problem/2295
"""
특정 원소를 찾는 문제 => 집합(SET)을 사용하는 문제?
답이 항상 존재하므로 set은 의미가 없는 자료구조인가

"해시 테이블" = 값을 아주 빠르게 찾기 위한 자료구조
평균적으로 O(1) 시간에 가까운 속도로 찾기, 추가, 삭제를 할 수 있다.
=> 어떤 값을 넣으면, 그 값을 특정한 위치로 바꿔주는 규칙이 있다.

처음 떠올린 생각: 
U 집합을 돌면서 세 값을 더한다.
세 값을 더한 값이 리스트 안에 존재하면 정답 리스트에 append 해놓는다.
그렇게 모든 조합을 검사한 후에 정답 리스트에서 가장 큰 값을 출력한다.

느낀 문제점:
세 개의 원소를 검사해야 하므로 시간복잡도가 O(n^3) 이 걸리지 않을까?
그리고 그 합이 리스트에 존재하는지 체크하려면 O(n)
결과적으로 O(n^4) 이 될거같은데?

내가 생각한 해결 방법:
세 값을 더한 값을 집합에 넣어두면, 중복값도 검사할 필요가 없고,
그 값이 있는지 확인하는 과정은 O(1) 시간이 걸려서 시간을 줄일 수 있다.
x + y 를 해서 K - z 를 만족하는 z를 찾을 수 있을까?
모든 x + y를 집합에 넣어 둔 뒤, K - z 값을 해쉬테이블에서 찾는다.

"""
import sys

N = int(sys.stdin.readline())
U = set(int(sys.stdin.readline()) for _ in range(N))
sum_set = set()
answer_set = set()

for x in U:
    for y in U:
        sum_set.add(x + y)

for K in U:
    for z in U:
        if K - z in sum_set:
            answer_set.add(K)

print(max(answer_set))
