NMAX = 4
XMAX = 10
for n in range(1,NMAX,+1):
    print(f'{n:10}', end='')
print()
for n in range(1,NMAX+1):
    print(f'{"x ":>10}', end='')



'''
for minutes in range(2):
    for seconds in range(60):
        print(minutes,':',seconds)
'''       


'''
total = 0.0
num_tests = 0
testing_score = int(input('Enter a score (negative to end)'))
while testing_score >= 0:
    total += testing_score
    num_tests = num_tests + 1
    testing_score = int(input('Enter a score (negative to end'))
print('The total is ', total)
if num_tests > 0:
    average = total/num_tests
    print('The average is: ', average)
else:
    print('No data for average computation!')


#problem 2

height = float(input('Enter a student\'s height (enter 0 to end: '))
if height > 0:
    shortest = height
    while height > 0:
        height = float(input('Enter a student\'s height (enter 0 to end): '))
        if height > 0 and height < shortest:
            shortest = height
    print('The shortest: '+ str(shortest))
else:
    print('No input for comparison')


#problem 3

score = int(input('What is your score? '))
while score > 100 or score < 0:
    print('Invalid score, must be in the range [0, 100]!')
    score = int(input('What is your score? '))
print('Your valid score: ', score)
'''
