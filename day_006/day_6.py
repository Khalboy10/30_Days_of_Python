# EXERCISES: LEVEL 1
# EXERCISE 1
my_tuple = tuple()

# EXERCISE 2
tpl = ('Abba','Kawu','Waleeda','Nafisat')

# EXERCISE 3
bro_tuple = ('Abba','Kawu')
sis_tuple = ('Waleeda','Nafisat')
siblings = bro_tuple + sis_tuple
print(siblings)

# EXERCISE 4
print('Number of siblings is ',len(siblings))

# EXERCISE 5
siblings = list(siblings)
siblings.insert(0, 'Dad')
siblings.insert(1, 'mum')
family_members = tuple(siblings)
print(family_members)

# EXERCISES: LEVEL 2
# EXERCISE 1
dad,mum,*sibling = family_members
print(dad)
print(mum)
print(sibling)

# EXERCISE 2
fruits = ('Apple', 'banana', 'Orange')
vegetables = ('Onion', 'Cabage', 'Tomato')
animal_products = ('Meat', 'Egg', 'Milk')
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)

# EXERCISE 3
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

# EXERCISE 4
middle_item = food_stuff_tp[4:5]
print(middle_item)

# EXERCISE 5
first_3_items = food_stuff_lt[0:3]
last_3_items = food_stuff_lt[6: ]
print(f'First 3 items are {first_3_items}')
print(f'Last 3 items are {last_3_items}')

# EXERCISE 6
del food_stuff_tp

# EXERCISE 7
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)
