from Turing import *
from Markov import *
from graph import *

ans = True
strT, strM = '', ''
for a in range(1, 101):
    for b in range(5, 6):
        ansT = TuringAlg('1'*a + '*' + '1'*b + '=')
        ansT = [len(ansT[0]), ansT[1]]
        strT += str(ansT[1]) + ' '

        ansM = MarkovAlg('1'*a + '*' + '1'*b)
        ansM = [len(ansM[0]), ansM[1]]
        strM += str(ansM[1])+ ' '

        if ansT != ansM:
            ans = False
fout = open('ans.txt', 'w')
fout.write(strT + '\n' + strM)
fout.close()

writeFromFile('ans.txt')
