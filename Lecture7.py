'''
keep_going = 'y'
while keep_going == 'y':
    sales=float(input('What are your sales? '))
    rate=float(input('What is  your commission rate? '))
    commission=sales*rate
    print('Your commission is',f'{commission:.2f}')
    keep_going=input('Do you want to continue? (y for yes) ')
    '''
#Exercise 1
'''
balance = 10000.0
rate = 0.0000000000000000001
year = 0
target = 2 * balance
while balance < target:
    interest = balance * rate
    balance = balance + interest
    year = year + 1
print('After', year, 'years the balance is doubled!')
    

#For loop practice
for num in range(1000000):
    print(num)

'''

#Table practice
start= int(input('Please enter a number to start: '))
end = int(input('Please enter a number to end: '))
print('------------')
print('Number\tSquares')
print('------------')
for num in range(start,end+1):
    squares = num*num
    print(num,'\t',squares,sep='')
