# Exercise 1
dog = dict()

# Exercise 2
dog['name'] = 'puppy'
dog['color'] = 'brown'
dog['breed'] = 'bull'
dog['legs'] = 4
dog['age'] = 6
print(dog)

# Exercise 3
student = {
    'first_name' : 'Auwal',
    'last_name' : 'Sulaiman',
    'gender' : 'male',
    'age' : '23',
    'marital_status' : 'single',
    'skills' : ['developer'],
    'country' : 'Nigeria',
    'city' : 'Kano',
    'address' : {
        'street' : 'here',
        'house_no' : 23334
    }
}

# Exercise 4
print(f'Length of student dictionary is {len(student)}.')

# Exercise 5
print(student.get('skills'))
print(type(student['skills']))

# Exercise 6
student['skills'].append('DataScientist')
print(student)

# Exercise 7
print(student.keys())

# Exercise 8
print(student.values())

# Exercise 9
student_dict = student.items()
print(student_dict)

# Exercise 10
student.pop('last_name')
print(student)

# Exercise 11
del dog
