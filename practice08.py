def solution(array, commands):
    print(commands)
    print(array)
    result = []
    process = []
    for i in range(0, len(commands)) :
        for j in range(commands[i][0], commands[i][1]+1):
            process.append(array[j-1])
        result.append(sorted(process)[commands[i][2]-1])
        process = []     
    return result
