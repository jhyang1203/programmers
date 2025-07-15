def solution(num, total):
    answer = []
    
    # 시작 숫자 계산 (앞서 설명한 공식 기반)
    start = (total - (num * (num - 1) // 2)) // num

    # 연속된 수 num개를 answer 리스트에 추가
    for i in range(num):
        answer.append(start + i)

    return answer
