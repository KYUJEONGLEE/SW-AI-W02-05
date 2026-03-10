import sys

input = sys.stdin.readline().rstrip()

# 2001:db8:85a3::8a2e:370:7334
if "::" in input:
    left, right = input.split("::")
    # :: 기준으로 l,r 로 나눈다.
    # l ,r 을 또 : 로 나눈다
    if left:
        left = left.split(':')
    else:
        left = []

    if right:
        right = right.split(':')
    else:
        right = []

    # left, right 가 없다면 빈 리스트를 반환한다.
    # 나누어진 문자열의 길이를 체크한다.
    fill_count = 8 - (len(left) + len(right))

    # 예시에서는 left = ["2001", "db8", "85a3"] , right = ["8a2a", "370", "7334"]
    # 원래 IPv6 는 콜론 7개와 구역 8개로 되어있으니까
    # 추가해야 하는 부분 = 8 - (len(right) + len(left)) = 2개
    modify_list = left + ['0'] * fill_count + right
else:
    modify_list = input.split(':')


IPv6 = ':'.join(group.zfill(4) for group in modify_list)
print(IPv6)
# : 를 기준으로 각 자리수가 4자리가 되도록 0을 채운다.
