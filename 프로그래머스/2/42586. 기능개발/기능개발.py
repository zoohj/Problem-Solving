import math

def solution(progresses, speeds):
    # 완성 일자 계산
    days = []
    for i in range (len(progresses)):
        temp = math.ceil((100 - progresses[i])/speeds[i])
        days.append(temp)       
    
    answer = []
    target_day = days[0]
    count = 0
    
    for day in days:
        if day <= target_day:
            count+=1
        else:
            answer.append(count)
            target_day = day
            count = 1
    
    answer.append(count)
    
    return answer