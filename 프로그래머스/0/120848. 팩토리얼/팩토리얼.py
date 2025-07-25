def solution(n):
    answer = 1
    for i in range(2,11):
        answer *= i
        if answer > n:
            answer = i-1
            break
            
        elif answer == n:
            answer = i
            break
        

    return answer