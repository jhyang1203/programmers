def solution(quiz):
    answer = []
    
    for q in quiz:
        X, op, Y, eq, Z = q.split()  # 공백을 기준으로 분리
        
        X_a, Y_a, Z_a = int(X), int(Y), int(Z)  # 정수 변환

        # 연산 수행
        if op == "+":
            result = X_a + Y_a
        elif op == "-":
            result = X_a - Y_a
        
        # 정답 판별
        if result == Z_a:
            answer.append("O")
        else:
            answer.append("X")

    return answer
