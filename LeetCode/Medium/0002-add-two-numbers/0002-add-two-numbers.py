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