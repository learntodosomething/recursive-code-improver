def format_number1(n):
    if isinstance(n, int):
        n = float(n)
    if n < 0:
        sign = '-'
        n = -n
    else:
        sign = ''
    integer_part = str(int(n))
    fractional_part = f"{n:.2f}".split('.')[1]
    formatted_integer = []
    for i, digit in enumerate(integer_part[::-1]):
        if i > 0 and (i % 3 == 0):
            formatted_integer.append("'")
        formatted_integer.append(digit)
    formatted_integer.reverse()
    return sign + ''.join(formatted_integer) + '.' + fractional_part

def format_number2(n):
    if isinstance(n, int):
        n = float(n)
    sign = '-' if n < 0 else ''
    abs_n = abs(n)
    integer_part = f"{abs_n:.2f}".split('.')[0]
    decimal_part = f"{abs_n:.2f}".split('.')[1]
    formatted_integer = []
    for i in range(len(integer_part), 0, -3):
        formatted_integer.append(integer_part[max(i-3, 0):i])
    formatted_number = sign + "'".join(formatted_integer[::-1]) + '.' + decimal_part
    return formatted_number

def format_number3(n):
    if isinstance(n, int):
        n = float(n)
    sign = '-' if n < 0 else ''
    n = abs(n)
    integer_part = '{:,.2f}'.format(n).replace(',', "'")
    return f"{sign}{integer_part}"

def format_number4(n):
    sign = '-' if n < 0 else ''
    abs_n = abs(n)
    formatted_integer = '{:,.2f}'.format(abs_n).replace(',', "'")
    return sign + formatted_integer


print(format_number1(11))
print(format_number2(11))
print(format_number3(11))
print(format_number4(11))
