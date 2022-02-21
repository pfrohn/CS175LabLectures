#Salary
'''
MIN_SALARY = 30000.0
MIN_YEARS = 2

salary = float(input('Enter your salary: '))
year = int(input('Enter your working years: '))

if salary >= MIN_SALARY:
    if year >= MIN_YEARS:
        print('You qualify for a loan!')
    else:
        print('You have to have at least a',MIN_YEARS,'year working history.')
else:
    print(f'You must have at least a ${MIN_SALARY:.2f} salary!')

#Grades

grade = float(input('Please enter your grade: '))

if grade>=0 and grade <= 100:
    if grade >= 90:
        print('You got an A!')
    elif grade >= 80:
        print('You got a B!')
    elif grade >= 70:
        print('You got a C')
    elif grade >= 60:
        print('You got a D...')
    else:
        print('You failed bro...')
else:
    print('Your grade must be between 0 and 100! YOU LIED!')
    '''
#
