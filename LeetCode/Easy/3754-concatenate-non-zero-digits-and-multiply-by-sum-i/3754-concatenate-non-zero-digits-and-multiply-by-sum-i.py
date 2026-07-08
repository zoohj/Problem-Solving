class Solution:
    def sumAndMultiply(self, n: int) -> int:
        # 맨 앞 숫자부터 0이 아닌 것만 골라서 남겨놔 -> x로 해서 순서대로 합쳐야돼
        # n//10^i
        sum = 0
        count = 1
        x=0

        while n>0:
            y = n % 10
            if y != 0:
                # 근데 남은 숫자의 합도 중간중간 더해야돼 -> sum 
                sum += y
                x += y * count
                count *= 10
            n //= 10

        # x * n 를 리턴
        return x * sum
        
