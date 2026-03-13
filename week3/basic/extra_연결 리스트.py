from __future__ import annotations
from typing import Any, Type


class Node:
    # Node 라는 개념을 사용하기 위해 클래스화
    # 초기화 함수 __init__: data - Any 로 선언, 어떤 자료형이든 받을 수 있음
    #                     next - Node 자료형\
    # 왜 next는 노트형으로 선언할까? next가 가르키는 대상은 단순한 data가 아니라
    # 다음 노드 전체 이기 때문이다
    def __init__(self, data: Any = None, next: Node = None):
        self.data = data
        self.next = next
        # self 사용이유, class 를 만들면 같은 설계도로 객체를 여러개 생성할 수 있다.
        # 그럴 떄, 본인의 data나 next 같은 속성을 구분 짓기 위해서


class LinkedList:

    def __init__(self) -> None:
        self.no = 0
        self.head = None
        self.current = None

    def __len__(self) -> int:
        return self.no

    def search(self, data: Any) -> int:
        # 연결리스트에서 data를 search 하는 함수
        # 있다면 그 노드가 몇번쨰 인지 반환한다.
        # 없으면 -1을 반환한다.

        # 헤드부터 꼬리까지 선형탐색으로 진행한다
        cnt = 0
        # 시작 : 헤드부터, 그걸 ptr 이라는 변수에 저장
        ptr = self.head
        # 종료 조건 -> p 노드가 가르키는 값이 None 이면 꼬리
        while ptr is not None:
            # ptr 이 None 이 아닐때까지 반복한다.
            if ptr.data == data:
                return cnt

            # 현재 가르키고 있는 ptr을 다음 next 노드로 정한다.
            ptr = ptr.next
            cnt += 1
            # 노드를 탐색할떄마다 카운트 + 1
        return -1

    def contain(self, data: Any) -> bool:
        if self.search(data) >= 0:
            return True
        return False
        # 현재 data가 포함되어있는지 여부를 bool 값으로 알려주는 함수
        # 위에서 구현한 search() 를 이용한다.

    def add_head(self, data: Any) -> None:
        # 맨 앞 head 에 원소를 추가하는 함수
        # 현재 헤드가 가지고 있는 포인터 참조값을 ptr 변수에 담아준다.
        # 왜? 새로 추가한 노드의 next를 현재 헤드노드로 연결 해줘야 하기 때문에

        # 그 다음 head 가 current(현재 가리키고 있는 노드)로 설정해주고,
        # 입력하고자 하는 값 data 와 다음노드(맨 앞에 추가하므로 원래 맨 앞에 있던 노드)
        # 다음노드를 가르키게 한다.
        # 노드가 추가 될 때마다 no(len) 증가
        ptr = self.head
        self.head = self.current = Node(data, ptr)
        self.no += 1


if __name__ == "__main__":
    P = Node
