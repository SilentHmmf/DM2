def commandExecute(s: list, index: int, state: str, commandDict: dict,):
    directionTuple = {'H': 0, 'L': -1, 'R': 1}
    commands = commandDict.get(state)
    endState = state
    if commands:
        for command in commands:
            if s[index] == command[0]:
                endState = command[1]
                s[index] = command[2]
                index += directionTuple[command[3]]
                break
    return s, endState, index


def TuringAlg(input1):
    string1 = ['.'] + [x for x in input1] + ['.']
    index, state, end_state = 1, 'q0', 'q*'
    commandDict = dict()
    #print('Введите правила формата "A B C D E"(Введите stop, чтобы закончить ввод:)')
    fin = open('TuringAlgorithm.txt')
    #fin = open('Turing2.txt')
    while True:
        #s = input()
        s = fin.readline()
        if s == 'stop':
            break
        q1, num1, q2, num2, d = s.split()
        if q1 in commandDict.keys():
            commandDict[q1].append((num1, q2, num2, d))
        else:
            commandDict[q1] = [(num1, q2, num2, d)]
    i = 0
    while state != end_state:
        string1, state, index = commandExecute(string1, index, state, commandDict)
        if string1[-1] != '.':
            string1.append('.')
        i += 1
        #print(string1, state, index)

    ans = ''
    for x in string1[string1.index('=') + 1:-1]:
        ans += x
    #print(ans)
    return ans, i



