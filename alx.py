a = { 'id': 89, 'name': "John" }
print(a.get('age'))


for i in range(0, 3):
    print(i, end=" ")


a = { 'id': 89, 'name': "John", 'projects': [1, 2, 3, 4], 'friends': [ { 'id': 82, 'name': "Bob" }, { 'id': 83, 'name': "Amy" } ] }
print(a.get('friends')[-1].get("name"))

a = { 'id': 89, 'name': "John", 'projects': [1, 2, 3, 4] }
print(a.get('projects')[3])