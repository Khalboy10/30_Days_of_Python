from math import sqrt
# Exercise 1 - 3 
age = 23
height = 1.85
_complex = 23 + 85j

# Exercise 4
b = int(input('Enter base of triangle: '))
h = int(input('Enter height of triangle: '))
area = 0.5 * b * h
print('The Area of Triangle is ', area)

# Exercise 5
a = int(input('Enter side A of triangle: '))
b = int(input('Enter side B of triangle: '))
c = int(input('Enter side C of triangle: '))
perimeter = (a + b + c)
print('perimeter of Triangle is ', perimeter)

# Exercise 6
lenght = int(input('Enter lenght of Rectangle: '))
width = int(input('Enter width of Rectangle: '))
area = lenght * width
perimeter = 2 * (lenght + width)

# Exercise 7
radius = int(input('Enter radius of circle: '))
area3 = 3.14 * (radius ** 2)
circumference = 2 * 3.14 * radius

# Exercise 8
x = int(input('Enter X: '))
y = 2 * (x) - 2

# Exercise 9
x1 = int(input('Enter X1: '))
x2 = int(input('Enter X2: '))
y1 = int(input('Enter Y1: '))
y2 = int(input('Enter Y2: '))
m = (y2 - y1)/(x2 - x1)

ed_a = (2 - 2) ** 2
ed_b = (6 - 10) ** 2
print(sqrt(ed_a + ed_b))

# Exercise 10
print(y == m)
print(y != m)
print(y > m)
print(y >= m)
print(y < m)
print(y <= m)

# Exercise 11
x = int(input('Enter x: '))
y = (x^2) + (6 * x) + 9
print(y)

# Exercise 12
print('python: ',len('python'))
print('dragon: ', len('dragon'))
print(len('python') > len('dragon'))

# Exercise 13
print('on' in ('python' and 'dragon'))

# Exercise 14
sentence = 'I hope this course is not full of jargon.'
print('jargon' in sentence)

# Exercise 15
print('on' not in ('python' and 'dragon'))

# Exercise 16
python = len('python')
print('lenght of python: ', python)
print('lenght of python in float: ', float(python))
print('lenght of python in string: ', str(python))

# Exercise 17
number = int(input('Enter number: '))
print(number % 2 == 0)

# Exercise 18
print((7//3) == int(2.7))

# Exercise 19
print(type(10) == type('10'))

# Exercise 20
print(int(9.8) == 10)

# Exercise 21
hours = int(input('Enter hours: '))
rate_per_hour = int(input('Enter rate per hour: '))
print('your weekly earning:',(hours * rate_per_hour))

# Exercise 22
number = int(input('Enter number of years you have lived: '))
print(f'You have lived for {number * 31536000} seconds.')

# Exercise 23
print(1, 1**0, 1**1, 1**2, 1**3)
print(2, 2**0, 2**1, 2**2, 2**3)
print(3, 3**0, 3**1, 3**2, 3**3)
print(4, 4**0, 4**1, 4**2, 4**3)
print(5, 5**0, 5**1, 5**2, 5**3)
