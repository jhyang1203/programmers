def solution(strlist):
    answer = []
    temp = 0
    
    for i in strlist:
        for j in i:
            temp += 1
        answer.append(temp)
        temp = 0
    return answer