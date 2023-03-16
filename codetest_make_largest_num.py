def solution(numbers):
    answer = ''
    arr_mem = []
    arr_mem2 = []
    for i in range(0, len(numbers)) :
        if numbers[i] // 100 != 0 :
            arr_mem.append((numbers[i], 1))
        elif numbers[i] // 10 != 0 :
            arr_mem.append((numbers[i]*10, 10))
        else :
            arr_mem.append((numbers[i]*100, 100))
    arr_mem.sort(reverse = True)
    
    for i in range(0, len(arr_mem)) :
        arr_mem2.append(str(arr_mem[i][0]//arr_mem[i][1]))
        answer += arr_mem2[i]
    
    return 