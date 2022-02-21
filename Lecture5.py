#bonus
'''
sales = float(input('What are your sales? '))
bonus = 0
if sales>50000:
    bonus = 500
print('Your bonus:',bonus)


#Averaging test scores 
test1 = int(input('What is the score of your first test? '))
test2 = int(input('What is the score of your second test? '))

average = (test1 + test2) / 2
print('Your average test score is: ', average ,"%")

if average <= 95:
    print('You suck')
else:
    print('Congratulations! You are super smart!')
    
#Temperature

temp = float(input('What is the temperature? '))
if temp>40:
    print('It is nice outside!')
    print('Let\'s go outside!')
else:
    print('It is cold outside!')
    print('You need to wear a coat NOW!')

#Employee


hours = float(input('How many hours did you work this week? '))
rate = float(input('What is your hourly pay rate? '))
pay = 0

if hours <= 40:
             pay = hours * rate
else:
    pay = 40*rate +(hours-40) * 1.5 * rate
print('Your pay:',pay)

#Strings

#Name order
name1 = input('What is your name? ')
name2 = input('What is your friend\'s name? ')
if name1<name2:
    print(name1)
    print(name2)
else:
    print(name2)
    print(name1)
'''
#Passwords

password = input('What is your stored password? ')
typed_password = input('Please enter the password NOW! ')
if password == typed_password:
    print('You can successfully log in!')
else:
    print('The password you entered is not correct')

