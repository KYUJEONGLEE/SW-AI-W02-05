
"""
접근 방법:
비밀번호 리스트 중에 뒤집어서 쓴 문자열이 있는지 검사해야 한다.
단어의 개수 100개
각 원소의 길이 3 ~ 13

reverse를 사용해서 비교할까

내가 지금 읽은 단어 word
reversed_word를 만든다
reversed_word가 저장소에 있나?
있으면 종료
없으면 word 저장
마지막에 길이와 가운데 문자 출력
"""
import sys

N = int(sys.stdin.readline())
X = [sys.stdin.readline().rstrip() for _ in range(N)]
visited_set = set()

for word in X:
    reverse_word = ''.join(reversed(word))
    if reverse_word == word:
        print(f"{len(word)} {word[len(word) // 2]}")
        break
    if word in visited_set:
        print(f"{len(word)} {word[len(word) // 2]}")
        break
    else:
        visited_set.add(reverse_word)
