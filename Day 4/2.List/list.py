#Create list
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia","Connecticut","Connecticut", "Massachusetts", "Maryland", "South Carolina"]
# printing list
print(states_of_america)

# Print list itmes use positive index
# Positive Index counting starts from 0 t0 1,2,3,4.........
print(states_of_america[0])
print(states_of_america[5])

# Print list use negative index
# Negative index start from the last of the list 
# Last list item index =-1
# Then previous one index =-2,then next -3,-4,-5,.........
print(states_of_america[-1])
print(states_of_america[-5])

# Update list 
# if you want to update any item in the list ,simply list name[index]= what you want to update put it here
states_of_america[1]="Pencilvania"
states_of_america[-2]="Marriedland"
# Printing the update list
print(states_of_america)

# Add a itmes end of the list
# Using append function
states_of_america.append("Awadhe's land")
# Print the update list
print(states_of_america)

#Add an item to the end of the list. Similar to a[len(a):] = [x].
states_of_america[len(states_of_america):]=["Hossain's land"]
# Print the update list
print(states_of_america)

# a.insert(len(a), x) is equivalent to a.append(x).
states_of_america.insert(len(states_of_america),"Alabama")
# Print the update list
print(states_of_america)


# Extend list itmes use Extend function
states_of_america.extend(["Angela's land","Yu's land"])
# Print the update list
print(states_of_america)

# Extend the list by appending all the items from the iterable. Similar to a[len(a):] = iterable.
states_of_america[len(states_of_america):]=["Arfan's land","Sifat's land"]
# Print the update list
print(states_of_america)

# Insert item in the list 
states_of_america.insert(0,"Texas")
states_of_america.insert(-1,"Florida")
states_of_america.insert(-2,"Ohio")
# Itmes wii be added before the mentioned index
# Print the update list
print(states_of_america)

# Removes itmes from the list
states_of_america.remove("Texas")
states_of_america.remove("Ohio")

#states_of_america.remove("Bangladesh")
# # It gives us value error because "Bangladesh" is not present in the list
#print(states_of_america)

# Uses of pop function
# Remove the item at the given position in the list, and return it. 
# If no index is specified, a.pop() removes and returns the last item in the list. 
states_of_america.pop(0)
states_of_america.pop()# Supported index -1 always
print(states_of_america)

# It raises an IndexError if the list is empty or the index is outside the list range.
#states_of_america.pop(45)
#print(states_of_america)

# List clear
#states_of_america.clear()
#print(states_of_america)
# For clear the string remove the comment sign

# Return the number of times x appears in the list.
a=states_of_america.count("Connecticut")
print(a)

# List Reverse
states_of_america.reverse()
print(states_of_america)

# List copy
x=states_of_america.copy()
print(x)
z=states_of_america[:]# Return a shallow copy of the list. Similar to a[:]
print(states_of_america)

# Sorting Ascending Order
states_of_america.sort()
print(states_of_america)

# Sorting Descending Order
states_of_america.sort(reverse=True)
print(states_of_america)


























