from test_cases.py import tests, answers

def main():
    pass

for index, test in enumerate(tests):
    main(test)
    if main(test) == answers[index]:
        print(f'Passed test {index}: {main(test)}')
    
    if main(test) != answers[index]:
        print(f'Failed test {index}\nExpected answer: {answers[index]}\nGiven answer: {main(test)}')