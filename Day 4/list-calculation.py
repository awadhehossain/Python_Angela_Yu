# We can simply add 2 list in one new list use simple mathmatics Addition
b=["1","2","3","4","5"]
c=["3","4","5","7"]
d=b+c
print(d)

# If you want to remove c from b list 
print(sorted(list(set(b)-set(c))))
# Set function does'nt maintained order

# A intersection B
A=['1','2','3','4','5']
B=['3','4','5','7']
# Filter elements in A that are also in B
filtered_A = list(filter(lambda x: x in B, A))
print(filtered_A)
# Use set Intersect Function
D=list(set(A).intersection(set(B)))
print(sorted(D))
# Use operator
G=list(set(A) & set(B))
print(sorted(G))




# A - B
A=['1','2','3','4','5']
B=['3','4','5','7']
q=list(filter(lambda x: x not in B,A)) # list function convert the data to a list
print(q)
# use Set function
g=list(set(A)-set(B)) 
# list function convert the data to a list 
# set function convert the to a set 
print(g)

# A union B
h=list(filter(lambda x:x not in A,B ))
print(h)
print(A+h)
# Use set union function
l=list(set(A).union(set(B)))
print(sorted(l))
# Use operator
s=list(set(A) | set(B))
print(sorted(s))


