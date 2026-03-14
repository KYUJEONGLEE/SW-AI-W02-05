class Solution:
    def simplifyPath(self, path):
        stack = []
        # 일단 '/' 를 지워야함
        path = path.split('/')
        # 무시해도 되는 문자들 '', '.' '///~'
        # // 가 여러개인 것들은 이미 split으로 지웠음
        for str in path:
            if str == '':
                # 다음 텍스트로 넘어감
                continue
            if str == '.':
                continue
            # .. 을 만난다면 이전 디렉토리로 이동
            # 즉, ".." 앞에 적혀있는 텍스트를 지워야한다.
            # 그리고 스택이 비어있다면 무시한다.
            # .. 을 만났다면 스택 pop 하고 다음 str로 이동
            if str == "..":
                if stack:
                    stack.pop()
                continue
            # / 와 '.' , ".." 을 제외한 디렉터리 명들은 스택에 넣는다.
            stack.append(str)

        return '/' + '/'.join(stack)
