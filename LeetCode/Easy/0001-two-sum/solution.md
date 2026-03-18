## [Hash] LeetCode - 1. Two Sum
> **핵심 키워드:** *#Hash #Dictionary #Complement #IndexManagement*

[https://leetcode.com/problems/two-sum/](https://leetcode.com/problems/two-sum/)


### 1. 💡 핵심
* > **"하나를 고정하고 '나머지 하나(Target - 현재값)'가 이전에 나온 적 있는지 확인하면 $O(N)$에 끝난다!"**
* **보수(Complement) 찾기:** $a + b = target$ 이라면, 우리는 $a$를 볼 때마다 "과거에 $target - a$가 나온 적 있는가?"만 확인.
* **자료구조 선택:** "특정 값이 있는지"와 "그 값의 인덱스가 무엇인지"를 동시에 $O(1)$에 찾아야 하므로 **Hash Map(Python의 `dict`)**이 최적.



---


### 2. 주의 사항 (시행착오 복기)

* **시행착오 - 정렬 후 투 포인터:** 정렬($O(N \log N)$)을 하면 값은 찾을 수 있지만, 문제에서 요구하는 **원래의 인덱스 정보**가 파괴됨. 
  * 인덱스를 지키려면 `(value, index)` 쌍으로 묶어서 정렬해야 함.
* **음수와 타겟값:** `if nums[i] <= target` 같은 조건은 음수가 포함된 경우(`-1 + 10 = 9`)를 제외함(오류!).
* **자기 자신 사용 방지:** `dict`에 현재 숫자를 넣기 **전에** `target - num`이 있는지 먼저 검사해야 함. 
  * `nums = [3], target = 6`일 때 자기 자신(3)을 두 번 써서 정답이라고 판단 오류를 내릴 수 있음.
* **`if index:`의 함정:** 파이썬에서 인덱스 `0`은 `False`로 처리. 반드시 `if complement in hash_map` 또는 `is not None`으로 존재 여부를 체크해야 함.
* **누적합(Prefix Sum)과의 차이:** 연속된 구간의 합을 구할 때는 누적합을 쓰지만, 떨어져 있는 두 수의 조합을 찾을 때는 Hash나 정렬이 우선.

#### + 🧸 Related concepts
- **3Sum / 4Sum:** 숫자의 개수가 늘어나면 정렬 후 투 포인터(인덱스 상관없을 때)나 고정 후 Hash 방식을 응용.
- **Two Pointer:** 만약 배열이 **이미 정렬되어 있고** 인덱스를 반환할 필요가 없다면 공간 복잡도 $O(1)$인 투 포인터가 최적.

---


### 3. 코드 설계 흐름
1. **준비:** 숫자를 키로, 인덱스를 값으로 저장할 빈 딕셔너리(`prev_map`)를 만듦.
2. **순회:** 배열을 한 번 돌면서 현재 숫자(`num`)와 인덱스(`i`)를 가져옴.
3. **계산:** *필요한 값*(`diff = target - num`)을 계산.
4. **확인:** `diff`가 `prev_map`에 있다면 즉시 `[prev_map[diff], i]`를 반환.
5. **저장:** 없다면 현재 숫자와 인덱스를 딕셔너리에 기록.

---


### 4. ☁️ 최종 정답 코드

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 1. 숫자의 값과 인덱스를 매핑할 해시맵(딕셔너리)
        # key: 숫자 값, value: 해당 숫자의 인덱스
        hashmap = {}
        for i in range(len(nums)):
            # 2. 필요한 값 계산
            need = target - nums[i]

            # 3. ⭐️ 핵심: 필요한 값이 이전에 등장했는지 확인
            if need in hashmap:                 # dict의 'in' 연산은 평균 O(1)의 시간복잡도를 가짐
                # answer 반환
                return [i, hashmap[need]]

            # 4. 정답을 못 찾았다면 현재 숫자와 인덱스를 저장
            hashmap[nums[i]] = i

        return [] # 실제 실행 X
```





---

> **문제의 구조**를 파악하는 것이 중요.<br> **연속된 합**인지 **자유로운 조합**인지, **인덱스 보존**이 필요한지에 따라 <br> 누적합, Hash, 투 포인터 중 무엇을 꺼낼지 결정됨.