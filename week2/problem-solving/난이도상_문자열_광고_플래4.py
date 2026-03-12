# 문자열 - 광고 (백준 플래4)
# 문제 링크: https://www.acmicpc.net/problem/1305

L = int(input())
X = input().rstrip()

# 반복되는 문자열을 찾는 문제인거같다.
# 앞에서 부터 문자를 하나씩 인덱싱,


def advertisement(n):

    length = len(n)
    min = length
    for i in range(1, length):
        if n[:i] == n[-i:]:
            # 슬라이싱은 비용이 많이 나간다. 시간복잡도 위험
            if min > length - len(n[:i]):
                min = length - len(n[:i])

    return min


if __name__ == "__main__":
    min_length = advertisement(X)
    print(min_length)

    # 문자열 n을 처음부터 i 번째 까지 indexing 한 값들이랑
    # 문자열 -1 부터 아래로 인덱싱?

    # veracro = 7 길이
    # roveracroveracrove = 18 길이
    # roveracrove 11

    # r ro rov rove rover rovera roverac roveracr roveracro roveracrov roveracrove roveracrover roveracrovera roveracroverac roveracroveracr roveracroveracro roveracroveracrov
    # e ve ove rove crove acrove racrove eracrove veracrove overacrove roveracrove croveracrove acroveracrove racroveracrove eracroveracrove veracroveracrove overacroveracrove

# aababab
