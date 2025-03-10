fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
dirty_dozen=[fruits,vegetables]
print(dirty_dozen)

# Nested list element print
a=dirty_dozen[0][0]
print(a) # fruits[0]
b=dirty_dozen[1][4]
print(b) # vegetables[4]
c=dirty_dozen[-1][-5]
print(c) # vegetables[0]
d=dirty_dozen[-2][-6]
print(d) # fruits[1]
e=dirty_dozen[0][-1]
print(e) # fruits[6]
f=dirty_dozen[-2][5]
print(f)



