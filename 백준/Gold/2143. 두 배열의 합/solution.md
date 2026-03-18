## [Hash/누적합] 백준 - 2143. 두 배열의 합
> **핵심 키워드:** *#누적합 #PrefixSum #Hash #TwoSum #부분배열*

[https://www.acmicpc.net/problem/2143](https://www.acmicpc.net/problem/2143)

### 1. 💡 핵심
* > **"모든 부분합을 구한 뒤, $A$의 부분합($S_A$)과 $B$의 부분합($S_B$)의 조합이 $T$가 되는 쌍을 찾는다."**
* **부분합의 개수:** 각 배열의 크기가 $N$일 때, 부분합의 개수는 $\frac{N(N+1)}{2}$. $N=1000$일 때 약 50만 개가 생성.
* **Hash 매칭:** 두 부분합의 모든 조합을 비교하면 $50만 \times 50만$으로 시간 초과가 발생. 따라서 **한쪽의 부분합 개수를 Hash Map(dict)에 저장**하여 $O(1)$로 매칭.



---

### 2. 주의 사항 (시행착오 복기)

* **시행착오 - 단순 누적합:** 전체 배열의 누적합 2개를 비교하는 문제 X. 
  * **모든 가능한 연속 부분배열**의 합을 각각 추출.
* **시간 복잡도 계산:** 부분합 추출($O(N^2)$) + Hash 매칭($O(N^2)$)으로 전체 $O(N^2 + M^2)$ 내에 해결해야 함. 
* **Hash 구조:** `dict`의 **Key는 '부분합의 값'**, **Value는 그 값이 나타난 횟수**여야 함. 횟수를 곱해줘야 모든 경우의 수가 옴.
* **변수 혼용:** 배열 $A$와 $B$의 부분합을 구할 때 각각의 배열 데이터를 참조하는지 엄격히 확인.
* **결과 자료형:** 가능한 쌍의 개수가 매우 클 수 있으므로 파이썬의 정수형을 믿되, 다른 언어라면 `long long` 타입을 고려해야 함.

#### + 🧸 Related concepts
- **Two Sum:** $a + b = T$를 찾는 가장 기본적인 해시 활용 패턴.
- **Subarray Sum Equals K:** 하나의 배열에서 부분합의 합이 K인 개수를 찾는 문제.

---

### 3. 코드 설계 흐름
1. **부분합 생성:** 이중 루프를 통해 배열 $A$의 모든 부분합을 구하고 `dict`에 **{합: 개수}** 형태로 저장.
2. **대상 탐색:** 배열 $B$의 모든 부분합을 구하면서, 각 합(`sum_b`)에 대해 `T - sum_b`가 $A$의 `dict`에 있는지 확인.
3. **결과 누적:** 존재한다면 해당 `dict`의 value(개수)를 `answer`에 더해줌.

---

### 4. ☁️ 최종 정답 코드
```python
import sys
from collections import defaultdict

input = sys.stdin.readline

t = int(input())
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

# 1. A의 모든 부분합 개수를 dict에 저장
a_sum_dict = defaultdict(int)
for i in range(n):
    current_sum = 0
    for j in range(i, n):
        current_sum += a[j]
        a_sum_dict[current_sum] += 1

# 2. B의 모든 부분합을 구하며 T를 만드는 짝이 있는지 확인
ans = 0
for i in range(m):
    current_sum = 0
    for j in range(i, m):
        current_sum += b[j]
        # ⭐️ 핵심: B_sum = T - A_sum 관계 이용
        target = t - current_sum
        if target in a_sum_dict:
            ans += a_sum_dict[target]

print(ans)

```

### 5. 수정 전 코드

```python
import sys
from collections import defaultdict

input = sys.stdin.readline

t = int(input())
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

# 1. A의 모든 부분합을 "합 : 개수" 형태로 저장
a_prefix_sum = {}
for i in range(n):          # 시작 인덱스
    current_sum = 0
    for j in range(i, n):   # 끝 인덱스를 늘려가며
        current_sum += a[j] # i ~ j까지의 부분합
        if current_sum not in a_prefix_sum:
            a_prefix_sum[current_sum] = 1
        else:
            a_prefix_sum[current_sum] += 1

# 2. B도 동일하게 저장
b_prefix_sum = {}
for i in range(m):
    current_sum = 0
    for j in range(i, m):
        current_sum += b[j]
        if current_sum not in b_prefix_sum:
            b_prefix_sum[current_sum] = 1
        else:
            b_prefix_sum[current_sum] += 1
            
# 3. A의 부분합을 기준으로 B에서 필요한 값을 찾아 조합 개수 계산
answer = 0
for a_sum, a_count in a_prefix_sum.items():
    # ⭐️ 핵심: B_sum = T - A_sum 관계 이용
    need = t - a_sum
    if need in b_prefix_sum:
        # A에서 해당 합이 나온 횟수 * B에서 해당 합이 나온 횟수
        # → 가능한 모든 조합 수
        answer += b_prefix_sum[need] * a_count
print(answer)

```
