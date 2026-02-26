# 모든 경우의 수를 다 세야함 => 완전탐색

def solution(numbers, target):
    
    #index: 처리해야하는 인덱스 / current_sum: 이전까지의 합
    def dfs(index, current_sum): 
        # 종료 조건
        if index == len(numbers):
            # target일 경우, 방법의 수 +1
            if current_sum == target:
                return 1
            return 0
        
        return(
        # 덧셈인 경우 + 뻴셈인 경우, ans
        dfs(index+1, current_sum+numbers[index]) 
        + dfs(index+1, current_sum-numbers[index])
        )
    
    return dfs(0, 0)



