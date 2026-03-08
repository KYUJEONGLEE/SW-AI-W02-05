# 정수론 - 골드바흐의 추측 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/9020

import sys

N = int(sys.stdin.readline())
T = [int(sys.stdin.readline()) for _ in range(N)]

# 문제 해결법 도출

# n 이하의 소수를 찾는 방법? 소수를 찾을까, 합성수를 지울까
# 합성수를 지우기로 선택
# i * 2,3,4... 이렇게 하면 중복적으로 지우는 부분이 생기는데?
# 그럼 반복문 안쪽의 j범위를 어디서부터 시작해야지?
# n = 10일떄, i = 2부터 시작하면 2 * 2, 2 * 3, 2 * 4 까지만 지우고, 3 * 2 = 6 을 할때
# 이미 지워졌다는 걸 발견했음
# 그럼 j가 i보다 작은수부터 시작하면 이미 지워진 수에 대해 접근하는 것이기 때문에 불필요한 연산을 진행한다
# 그럼 j = i 부터 시작하면 어떨까?
# i = 2 일때 2 * 2 부터 ...
# i = 3 일떄,3 * 3 부터 ...
# i = 4 일때,4 * 4 부터 ..?? 이미 지워졌는데??
# 일단 넘어가고, j 시작값을 정했음(i부터 시작)
# 이제 i값이 이미 지워진(0) 상태라면 안해야한다.
# 그럼 a[i-2] = 0 이면 continue 하면 다음 i로 넘어간다.
# i의 끝점을 정해보자.
# 어떤 수 i와 i 를 곱해서 나오는 수가 n보다 작아야 한다. i ^ 2 < n => 이거를 i에 대해서 정리하면 i < 루트(n)
# 여기에서는 루트n은 실수니까 int 변환하면 내림 정수가 된다. 그 내림 정수까지 i를 돌아야하므로 루트  n + 1 까지 범위를 잡아준다.
# 안쪽 j값의 끝점을 생각해보자.
# i 의 배수를 구할때, i * (j=i) 부터 시작한다.
# 똑같은 방식으로 하면 안될까? => 예외가 존재함.
# i * j < n 은 똑같은 방식이다. 이걸 j에 대해 정리하면 j < n / i
# 근데 여기서 리스트의 끝의 원소가 n - 1 이란걸 대입하면 결국 j의 끝점은 j < (n - 1) / i 가 되야한다.
# 그래서 a[i * j - 2] 을 지워준다(0). -2 를 해준 이유는 2부터 시작했기 때문에 index가 2개가 빈다.


def get_prime(n):
    prime_list = []
    ans = [_ for _ in range(2, n)]
    # 바꿔야 할 부분
    # 바깥 반복문에서 i를 2부터 n까지 굳이 다 봐야할까?
    # 이미 0이 된 숫자에 대해서는 연산이 필요없다.

    for i in range(2, int(n**0.5) + 1):

        if ans[i - 2] == 0:
            continue

        for j in range(i, (n-1)//i + 1):
            if ans[i * j - 2] == 0:
                pass
            else:
                ans[i * j - 2] = 0

    # 0 이 아닌값들만 모아준다.
    for x in ans:
        if x != 0:
            prime_list.append(x)

    return prime_list


# r 에서 소수들을 뺀 조합을 생각하면 뺴는 수와 결과값이 소수인 경우가 도출된다.
    # 이떄 얻어낸 두 값들의 차가 적은것을 선택

def goldbach_partitions(R):
    partition = []
    sub_value = 10000
    for r in R:
        prime_list = get_prime(r)

    for prime in prime_list:
        p1 = r - prime
        if p1 in prime_list:
            if sub_value > abs(p1 - prime):
                partition.append([prime, p1])
                sub_value = p1 - prime

    print(*partition[0], sep=" ")


goldbach_partitions(T)
