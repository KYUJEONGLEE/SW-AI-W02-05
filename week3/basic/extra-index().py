if __name__ == "__main__":
    test_array = [2, 6, 9, 11, 15, 16, 19, 21, 26]
    n = 21
    is_key_in_array = test_array.index(n)
    print(is_key_in_array)

# 파이썬에서 튜플과 리스트는 index() 파이썬 내장함수를 사용해서 탐색이 가능하다.
# 문법 : obj.index(x,i,j) => obj[i:j] 안에 x값이 있는가?
# 보통 obj 에서 전체범위를 검사하므로 obj.index(x) 라고들 적는다
# 반환값 => x값을 찾으면 해당 index를 반환, 없으면 ValueError
