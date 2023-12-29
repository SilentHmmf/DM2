def commandExecute(s: str, command: [str, str]):
    return s.replace(command[0], command[1], 1).replace('v', '')


def MarkovAlg(input1):
    string1 = input1
    commands = []
    # print('Введите правила формата "A B"(Введите stop, чтобы закончить ввод:)')
    fin = open('MarkovAlgorithm.txt')
    while True:
        # s = input()
        s = fin.readline()
        if s == 'stop':
            break
        s = s.split()
        commands.append(s)
    i = 0
    while True:
        startpoint = string1
        for command in commands:
            string1 = commandExecute(string1, command)
            i += 1
            if string1 != startpoint:
                break
        if startpoint == string1:
            break

    #print(f'ans: {string1}')
    return string1, i
