## [LinkedList] LeetCode - 2. Add Two Numbers

> **핵심 키워드:** *#LinkedList #DummyNode #PointerManagement #Carry #EdgeCases*

[https://leetcode.com/problems/add-two-numbers/](https://leetcode.com/problems/add-two-numbers/)

### 1. 💡 핵심

* > **"각 노드를 순회하며 1의 자리 합과 올림수(Carry)를 계산하고, Dummy Node를 활용해 새 연결 리스트를 구축한다!"**


* **올림수(Carry) 전산:** 두 숫자의 합이 $10$ 이상일 때, 몫($// 10$)은 다음 자리로 넘길 `carry`가 되고 남은 값($\% 10$)은 현재 노드의 값이 됨.
* **자료구조 & 패턴 선택:**
* 연결 리스트 생성을 손쉽게 하기 위해 **Dummy Node(더미 노드)** 패턴을 활용.
* 첫 번째 노드 생성 시의 예외 처리(`if not head:`) 없이 $O(N)$으로 깔끔하게 리스트 구축 가능.



---

### 2. 주의 사항 (시행착오 복기)

* **시행착오 - 연결 리스트 자체 연산 시도:** `l1 + l2`처럼 노드 객체끼리 직접 더하려 함(오류!).
* 연결 리스트 노드는 숫자가 아닌 객체(Pointer)이므로 반드시 `l1.val`, `l2.val`로 내부에 접근해야 함.


* **`l1 = l1.next`의 오해:** 데이터가 삭제되는 것이 아니라, 탐색하는 **포인터(현재 위치)의 이동**임.
* 메모리 내 노드 자체는 훼손되지 않으며, `l1` 변수가 가리키는 주소만 다음 칸으로 갱신됨.


* **두 리스트의 길이가 다른 경우 (`AttributeError` 방지):**
* 한쪽 리스트가 먼저 끝나 `None`이 되었을 때 `l1.val`이나 `l1.next`에 직접 접근하면 프로그램이 멈춤.
* **값 접근 시:** `l1.val if l1 else 0` 삼항 연산자로 안전하게 `0` 처리.
* **포인터 이동 시:** `if l1: l1 = l1.next`처럼 노드가 존재하는 경우에만 이동.


* **마지막 올림수 처리:** 두 리스트의 탐색이 모두 끝났더라도 마지막 연산에서 올림수(`carry`)가 남아있을 수 있음.
* `while l1 or l2 or carry:` 조건문으로 `carry`가 남아있다면 끝에 노드 하나를 더 생성해 주어야 함 (예: $5 + 5 = 10$).



#### + 🧸 Related concepts

* **Multiply Strings / Add Binary:** 문자열이나 배열 형태의 숫자를 더할 때도 똑같이 `carry` 개념을 적용.
* **Dummy Node Pattern:** 연결 리스트를 새로 만들거나, 기존 리스트의 Head를 수정할 때 시작점 위치를 보존하기 위해 필수적으로 쓰이는 테크닉.

---

### 3. 코드 설계 흐름

1. **준비:** 시작점 손잡이 역할을 할 `dummy` 노드와, 이동용 포인터 `curr = dummy`를 생성. 올림수를 저장할 `carry = 0` 초기화.
2. **순회:** `l1`, `l2` 노드가 남아있거나 처리해야 할 `carry`가 남아있는 동안 계속 반복.
3. **값 추출:** 각 리스트가 존재하면 노드의 `.val`을 가져오고, 이미 끝나서 `None`이라면 `0`으로 가상 처리.
4. **연산 및 올림수 갱신:** `total = val1 + val2 + carry`를 구하고, 다음 자릿수로 넘길 `carry = total // 10`과 현재 노드 값 `val = total % 10` 계산.
5. **연결 및 이동:** `curr.next = ListNode(val)`로 새 노드를 잇고 `curr = curr.next`로 이동. `l1`, `l2` 역시 존재할 때만 다음 노드로 이동.
6. **반환:** `dummy` 노드 다음인 `dummy.next` (진짜 결과 리스트의 Head) 반환.

---

### 4. ☁️ 최종 정답 코드

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #결과 리스트의 시작점
        dummy = ListNode(0)
        # 현재 위치 가리킬 포인터
        curr = dummy

        carry = 0

        while l1 or l2 or carry:
            # 노드 존재하면 그값을 가져오고, 이미 끝났다면 0으로 처리
            # 이미 짧아서 끝난 리스트의 값을 가져올 때 에러 나지 않게 0으로 가상 채움 해주기
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # 합산
            total = val1 + val2 + carry

            carry = total // 10
            val = total % 10

            # 새 노드 연결
            curr.next = ListNode(val)
            # 포인터 이동(새 노드로)
            curr = curr.next

            # 다음 노드로 이동
            #이미 None이 된 상태에서 None.next를 실행해서 터지는 에러 방지
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        # dummy 노드 다음(진짜 시작 노드)부터 반환
        return dummy.next

```

---

> **연결 리스트 제어**의 핵심은 **포인터 위치 관리**와 **`None` 참조 에러 방지**.
> 
> 
> 
>  **길이가 다른 입력값**과 **마지막 Carry 처리**에 유의하며 
> 
> 
> 
>  Dummy Node 패턴을 꺼내 쓰는 정석적인 문제.
