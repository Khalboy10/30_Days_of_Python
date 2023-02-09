# Exercises: Level 1
# Exercise 1
age = int(input('Enter your age: '))
if age >= 18:
    print('You are old enough to learn to drive.')
else:
    print(f'You need {18 - age} more years to learn to drive.')

# Exercise 2
my_age = int(input('Enter age: '))
your_age = int(input('Enter your age: '))
if your_age > my_age:
    if (your_age - my_age) == 1:
        print(f'You are {1} year older than me.')
    else:
        print(f'You are {your_age - my_age} years older than me.')
elif your_age == my_age:
    print('We have the same age.')
else:
    print('I am older than you.')

# Exercise 3
a = int(input('Enter first Number: '))
b = int(input('Enter second Number: '))
if a > b:
    print(f'{a} is greater than {b}')
elif a < b:
    print(f'{a} is smaller than {b}')
else:
    print(f'{a} is equal to {b}')

# Exercises: Level 2
# Exercise 1
scores = int(input('Enter Scores: '))
if scores > 100:
    print('Insert valid scores')
elif scores >= 80:
    print('Grade = A')
elif scores >= 70:
    print('Grade = B')
elif scores >= 60:
    print('Grade = C')   
elif scores >= 50:
    print('Grade = D')
elif scores >= 0:
    print('Grade = F')
else:
    print('Insert valid scores')

# Exercise 2
autumn = ['September', 'October', 'November']
winter = ['December', 'January', 'February']
spring = ['March', 'April', 'May']
summer = ['June', 'July', 'August']
month = input('Enter Month: ').title()
if month in autumn:
    print('The season is Autumn.')
elif month in winter:
    print('The season is Winter.')
elif month in spring:
    print('The season is Spring.')
elif month in summer:
    print('The season is Summer.')
else:
    print('You entered invalid month.')

# Exercise 3
fruits = ['banana', 'orange', 'mango', 'lemon']
add_fruits = input('Add Fruit: ')
if add_fruits in fruits:
    print('That fruit already exist in the list')
else:
    fruits.append(add_fruits)
    print(fruits)


# Exercises: Level 3
person={
    'first_name': 'Auwal ',
    'last_name': 'Auwal Sulaiman',
    'age': 250,
    'country': 'Nigeria',
    'is_marred': False,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
if 'skills' in person.keys():
    print(person['skills'][len(person['skills'])//2])

if 'skills' in person.keys():
    print('Python' in person['skills'])

if person['skills'] == ['JavaScript', 'React']:
    print('He is a Frontend Developer.')
elif person['skills'] == ['Node', 'MongoDB', 'Python']:
    print('He is a Backend Developer.')
elif person['skills'] == ['React', 'Node', 'MongoDB']:
    print('He is Fullstack Developer.')
else:
    print('unknown title')

if person['is_marred'] == False and person['country'] == 'Nigeria':
    print(f'{person["first_name"]+person["last_name"]} lives in {person["country"]}. He is not married')

