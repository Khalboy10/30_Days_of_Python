# EXERCISES: LEVEL 1
# Exercise 1
lst = list()

# Exercise 2
lst = [1,5,3,9,7,5,4,6]

# Exercise 3
print(len(lst))

# Exercise 4
print(lst[0])
print(lst[4])
print(lst[-1])

# Exercise 5
mixed_data_types = ['Auwal', 23, 1.85, 'single', 'No 149 Tudun Wada B']

# Exercise 6
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# Exercise 7
print(it_companies)

# Exercise 8
print(len(it_companies))

# Exercise 9
print(it_companies[0])
print(it_companies[3])
print(it_companies[-1])

# Exercise 10
it_companies[4] = 'Instagram'
print(it_companies)

# Exercise 11
it_companies.append('Space X')
print(it_companies)

# Exercise 12
it_companies.insert(4, 'Hubook')
print(it_companies)

# Exercise 13
it_companies[2] = it_companies[2].upper()
print(it_companies)

# Exercise 14
print('#; '.join(it_companies))

# Exercise 15
print(it_companies.index('Oracle'))

# Exercise 16
it_companies.sort()
print(it_companies)

# Exercise 17
it_companies.reverse()
print(it_companies)

# Exercise 18
print(it_companies[ : 3])

# Exercise 19
print(it_companies[6: ])

# Exercise 20
print(it_companies[3:5])

# Exercise 21
it_companies.remove(it_companies[0])
print(it_companies)

# Exercise 22
del it_companies[3:5]
print(it_companies)

# Exercise 23
it_companies.remove(it_companies[-1])
print(it_companies)

# Exercise 24
it_companies.clear()
print(it_companies)

# Exercise 25
del it_companies

# Exercise 26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end.extend(back_end)
print(front_end)

# Exercise 27
full_stack = front_end.copy()
full_stack.insert(5, 'Python')
full_stack.insert(6, 'SQL')
print(full_stack)

# EXERCISE: LEVEL 2
# Exercise 1
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort() # 1
print(ages)
print('Minimum age is', min(ages)) # 2
print('maximum age is', max(ages)) # 3
print((ages[4] + ages[5]) // 2) # 4
average = sum(ages) / len(ages)
print('Average age is', average) # 5
print('Range is', max(ages) - min(ages)) # 6
print('(min - average) is ',abs(min(ages)-average), 'and (max - average) is ',abs(max(ages)-average)) #7

# Exercise 1
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]
print(countries[97])

# Exercise 2
countries_first_half = countries[ : 98]
countries_second_half = countries[98: ]
print(countries_first_half)
print(countries_second_half)

# Exercise 3
some_countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
ch, ru, us, *scandic = some_countries
print(ch)
print(ru)
print(us)
print(scandic)