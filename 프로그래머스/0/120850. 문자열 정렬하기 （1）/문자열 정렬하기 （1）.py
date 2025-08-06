def solution(my_string):
    answer = []
    for i in my_string:
        if '0'<= i <='9':
            answer.append(i)
    
    answer.sort()
    
    answer = list(map(int,answer))
    return answer