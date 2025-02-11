def solution(l, r):
    answer = []
    
     
    for i in range(l,r+1):
        if all(digit in "05" for digit in str(i)):
            answer.append(i)
        
        
    answer.sort()
    
    return answer if answer else [-1]