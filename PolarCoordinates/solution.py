# Enter your code here. Read input from STDIN. Print output to STDOUT

from math import *

from test_cases.py import tests, answers

#compNumber = input()

def main(compNumber):

    #Needs to deal with negative numbers - turn string into negative number
    if(compNumber.find('+')):
        compNumber = compNumber.split('+')
        compNumber[1] = compNumber[1].replace('j','')
        
    elif(compNumber.find('-')):
        compNumber = compNumber.split('-')
        compNumber[1] = compNumber[1].replace('j','')

    re = int(compNumber[0])
    im = int(compNumber[1])

    mag = sqrt(re**2 + im**2)
    arg = atan2(im, re)

    if(arg > pi):
        arg = -1 * arg - pi
        
    return mag, arg

    #print(mag)
    #print(arg)
    
for index, test in enumerate(tests):
    main(test)
    if main(test) == answers[index]:
        print(f'Passed test {index}: {main(test)}')
    
    if main(test) != answers[index]:
        print(f'Failed test {index}\nExpected answer: {answers[index]}\nGiven answer: {main(test)}')