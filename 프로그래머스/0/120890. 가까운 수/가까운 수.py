def solution(array, n):
    answer = array[0]
    
    array.sort()
    for i in array:
        if abs(i-n) < abs(answer-n):
            answer = i
        elif abs(i - n) == abs(answer - n):
            if i < answer:  # 더 작은 값을 선택
                answer = i
        
    return answer