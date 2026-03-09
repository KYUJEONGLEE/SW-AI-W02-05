
def num_to_word(n):
    # visited = [False] * len(n)

    phone = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
             "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

    result = []

    def backtracking(start, current_combination):
        # 종료 조건 : 입력값 n의 길이와 current_com 길이가 같을때
        # start => 시작하는 지점(현재 위치?), current_combination => 문자 조합 저장 리스트
        if len(current_combination) == len(n):
            result_combination = current_combination.copy()
            result.append(result_combination)
            return

        for char in phone[n[start]]:
            current_combination.append(char)
            backtracking(start + 1, current_combination)
            current_combination.pop()

    backtracking(0, [])
    return result


if __name__ == "__main__":
    output = num_to_word("23")
    for char in output:
        print(*char)
