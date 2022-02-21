first = int(input('First Integer: '))
second = int(input('Second Integer: '))
sum_result = first + second
diff_result = first - second
product_result = first * second
integer_division = first//second
average = sum_result / 2
remainder = first % second
exponent = first ** second
STR_SUM = 'Sum'
STR_DIFFERENCE = 'Difference'
STR_PRODUCT = 'Product'
STR_DIVISION = 'Integer Division'
STR_AVERAGE = 'Average'
STR_REMAINDER = 'Remainder'
STR_EXPONENT = 'Exponent'
print(f'{STR_SUM+":":20}',f'{sum_result:5}')
print(f'{STR_DIFFERENCE+":":20}',f'{diff_result:5}')
print(f'{STR_PRODUCT+":":20}',f'{product_result:5}')
print(f'{STR_DIVISION+":":20}',f'{integer_division:5}')
print(f'{STR_AVERAGE+":":20}',f'{average:8.2f}')
print(f'{STR_REMAINDER+":":20}',f'{remainder:5}')
print(f'{STR_EXPONENT+":":20}',f'{exponent:5}')

print(f'{STR_SUM:>5}',end='')
print(f'{STR_DIFFERENCE:>12}',end='')
print(f'{STR_PRODUCT:>9}',end='')
print(f'{STR_DIVISION:>18}',end='')
print(f'{STR_AVERAGE:>9}',end='')
print(f'{STR_REMAINDER:>11}',end='')
print(f'{STR_EXPONENT:>10}')

print(f'{sum_result:5}',end='')
print(f'{diff_result:12}',end='')
print(f'{product_result:9}',end='')
print(f'{integer_division:18}',end='')
print(f'{average:9.2f}',end='')
print(f'{remainder:11}',end='')
print(f'{exponent:10}',end='')

