# Exrecise 1
thirty = 'Thirty'
days = 'Days'
of = 'Of'
python = 'Python'
space = ' '
print(thirty + space + days + space + of + space + python)

# Exercise 2
coding = 'Coding'
_for = 'For'
all = 'All'
space = ' '
print(coding + space + _for + space + all)

# Exercise 3
company = "Coding For All"

# Exercise 4
print(company)

# Exercise 5
print(len(company))

# Exercise 6
print(company.upper())

# Exercise 7
print(company.lower())

# Exercise 8
print(company.capitalize())
print(company.title())
print(company.swapcase())

# Exercise 9
print(company[7:])

# Exercise 10
print(company.find('Coding'))

# Exercise 11
print(company.replace('Coding', 'Python'))

# Exercise 12
print(company.replace(company, 'Python For Everyone'))

# Exercise 13
print(company.split())

# Exercise 14
print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(','))

# Exercise 15
print(company[0])

# Exercise 16
print(company.rindex('l'))

# Exercise 17
print(company[10]) # The character at index 10 is ' '

# Exercise 18
python = 'Python For Everyone'
python_abr = python[0] + python[7] + python[11]
print(python_abr)

# Exercise 19
coding = 'Coding For All'
coding_abr = coding[0] + coding[7] + coding[11]
print(coding_abr)

# Exercise 20
print(coding.index('C'))

# Exercise 21
print(coding.index('F'))

# Exercise 22
print('Coding For All People'.rfind('l'))

# Exercise 23
print('You cannot end a sentence with because because because is a conjunction'.find('because'))

# Exercise 24
print('You cannot end a sentence with because because because is a conjunction'.rindex('because'))

# Exercise 25
print('You cannot end a sentence with because because because is a conjunction'[ :31])

# Exercise 26
print('You cannot end a sentence with because because because is a conjunction'.index('because'))

# Exercise 27
print('You cannot end a sentence with because because because is a conjunction'[ :31])

# Exercise 28
print(coding.startswith('Coding'))

# Exercise 29
print(coding.endswith('coding'))

# Exercise 30
print('   Coding For All      '[3:17])

# Exercise 31
print('30DaysOfPython'.isidentifier())
print('thirty_days_of_python'.isidentifier())

# Exercise 32
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('# '.join(libraries))

# Exercise 33
print('I am enjoying \nthis challenge.')
print('I just wonder \nwhat is next.')

# Exercise 34
print('Name\t\tAge\tCountry\t\tCity')
print('Asabeneh\t250\tFinland\t\tHelsinki')

# Exercise 35
radius = 10
area = 3.14 * radius ** 2
print(f'The area of a circle with radius {radius} is {area} meters square.')

# Exercise 36
x = 8
y = 6
print(f'{x} + {y} = {x + y}')
print(f'{x} - {y} = {x - y}')
print(f'{x} * {y} = {x * y}')
print(f'{x} / {y} = {x / y:.2f}')
print(f'{x} % {y} = {x % y}')
print(f'{x} // {y} = {x // y}')
print(f'{x} ** {y} = {x ** y}')
