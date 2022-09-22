users = [
    {'name': 'Celina',
     'age': 21,
     'gender': 'female',
     'username': 'Celine',
     'is_verified': True,
     'tweets': [
         {'content': 'PO for President', 'likes': 450, 'retweets': 233},
         {'content': 'Atiku is our own', 'likes': 4, 'retweets': 2}
     ]},

    {
        'name': 'Banke',
        'age': 30,
        'gender': 'female',
        'username': 'Banks',
        'is_verified': 'False',
        'tweets': [
            {'content': 'The importance of music in the society', 'likes': 450, 'retweets': 233},
            {'content': 'Music in a solemn environment', 'likes': 4, 'retweets': 2}
        ]},

    {
        'name': 'Celina',
        'age': 29,
        'gender': 'female',
        'username': 'Celine',
        'is_verified': True,
        'tweets': [
        ]
    },

    {
        'name': 'Adesua',
        'age': 27,
        'gender': 'female',
        'username': 'Susu',
        'is_verified': True,
        'tweets': [
            {'content': 'Love is a beautiful thing', 'likes': 450, 'retweets': 233},
            {'content': 'Roses are red', 'likes': 4, 'retweets': 13}
        ]},

    {
        'name': 'Bankole',
        'age': 21,
        'gender': 'male',
        'username': 'Banky',
        'is_verified': False,
        'tweets': [
            {'content': 'PO for President', 'likes': 450, 'retweets': 233},
            {'content': 'Our vote counts', 'likes': 4, 'retweets': 2}
        ]}

]

no_of_users = len(users)

usernames = {user['username'] for user in users}

female_users = [user for user in users if user['gender'] == 'female']

inactive_users = [user for user in users if len(user['tweets']) == 0]

name_and_age = [{'name': user['name'], 'age': user['age']} for user in users]

avg_age_of_users = round(sum(user['age'] for user in users) / len(users))

print(inactive_users)

print(female_users)

print(name_and_age)

print(avg_age_of_users)

# Max
print(max(users, key=lambda x: len(x['tweets'])))

# zip is just like concatenation, it joins elements
iterable1 = (1, 2, 3, 4, 5, 6, 7)
iterable2 = ('hello', 'how', 'are', 'you', 'doing', 'my', 'sweetheart')
print(zip(iterable2, iterable1))
print(list(zip(iterable2, iterable1)))
print(dict(zip(iterable2, iterable1)))

# sorted
print(sorted(iterable2))
print(sum(user['age'] for user in users) / len(users))

print(any(user['is_verified'] for user in users))
print(all(user['is_verified'] for user in users))