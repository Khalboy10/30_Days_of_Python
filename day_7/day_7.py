# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Exercises: Level 1
# Exercise 1
print(f'Length of it_companies is {len(it_companies)}.')

# Exercise 2
it_companies.add('Twitter')
print(it_companies)

# Exercise 3
it_companies.update(['Space X', 'Tesla', 'Meta'])
print(it_companies)

# Exercise 4
it_companies.remove('Facebook')
print(it_companies)

# Exercise 5
# If the item is not in the set the remove() method raise an errors While the discard() method doesn't raise an errors.

# Exercises: Level 2
# Exercise 1
print(A.union(B))

# Exercise 2
print(A.intersection(B))

# Exercise 3
print(A.issubset(B))

# Exercise 4
print(A.isdisjoint(B))

# Exercise 5
print(A.union(B))
print(A.union(B))

# Exercise 6
print(A.symmetric_difference(B))

# Exercise 7
del it_companies, A, B

# Exercises: Level 3
# Exercise 1
age_set = set(age)
print(f'Length of age list is {len(age)} and Length of age set is {len(age_set)}')

# Exercise 2
a_string = """A String is a combination of characters and spaces (a String can be one character),
            that are written between two single, double or triple quotations"""

a_list = """A List is a collection of items of the same or different data types that are written inside
          open and close square brackets. The items in a List are ordered and mutable."""

a_tuple = """A Tuple is a collection of items of the same or different data types that are written inside
          open and close brackets. The items in a Tuple are ordered and immutable."""

a_set = """A Set is a collection of items of the same or different data types that are written inside
          open and close curly brackets. The items in a Set are unordered, mutable and unique"""

# Exercise 3
sentence = 'I am a teacher and I love to inspire and teach people'
lst = sentence.split(' ')
unique_words = set(lst)
print(unique_words)

