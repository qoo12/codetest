def solution(citations):
    answer = 0
    citations.sort(reverse = True)
    for i in range(0, len(citations)) :
        if i+1 >= citations[i] :
            answer = citations[i]
            break
    return answer