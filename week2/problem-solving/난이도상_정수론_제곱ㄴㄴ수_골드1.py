# 정수론 - 제곱 ㄴㄴ 수 (백준 골드1)
# 문제 링크: https://www.acmicpc.net/problem/1016

# 어떤 정수 X가 1보다 큰 제곱수로 나누어 떨어지지 않을 때, 그 수를 제곱ㄴㄴ수라고 한다.
# 제곱수는 정수의 제곱이다. min과 max가 주어지면, min보다 크거나 같고, max보다 작거나 같은 제곱ㄴㄴ수가 몇 개 있는지 출력한다.

# 에라토스테네스의 체 : 해당 값을 찾는게 아니라 해당 값을 제외한 값들을 지운다.
# 어떤 수의 제곱인 수를 제외하고 남는 개수를 센다.
# min 의 범위가 굉장히 크지만, 결국 max - min <= 1,000,000 이다. 즉 구간의 길이는 길지않다.
# 1,000,000 개의 숫자를 특정 수의 제곱으로 일일히 나누어 보는건 시간초과가 난다.
# 그럼 제곱해야 해야 하는 k 값의 범위에 대해서 생각해보면,
# k^2 이 max 보다 크면 의미가 없어진다 , k <= sqrt(max)

# 최대 1,000,001 크기의 배열을 만들고, index를 매핑시킨다.

min, max = input().split()
min, max = int(min), int(max)

# 제곱 ㄴㄴ수가 아닌지 표시하는 리스트
# 각 숫자칸은 숫자 n - min 칸에 매핑
no_square_list = [0] * (max - min + 1)


def square_nono(a, b):
    # a, b = 최소값과 최댓값을 입력받으면
    # 두 사이의 ㄴㄴ 제곱수의 개수를 반환하는 함수
    # => 제곱수의 배수를 찾아 지우는 문제로 변환

    # min 이상인 '제곱수X의 첫 번째 배수'는 어떻게 구하지?
    # min / 제곱수 k 했을 때, 나머지가 0이면 min 이 첫 배수,
    # 아니면 (몫 + 1) * k 가 첫 배수
    i = 2

    while i ** 2 <= max:
        k = i ** 2
        mul_k = 0

        if a % k == 0:
            mul_k = a
        else:
            mul_k = ((a // k) + 1) * k

        while mul_k <= max:
            no_square_list[mul_k - a] = 1
            mul_k += k

        i += 1

    return no_square_list.count(0)


if __name__ == "__main__":
    nono_square = square_nono(min, max)
    print(nono_square)
