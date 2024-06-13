# Create a set
my_set = {1, 2, 3, 5, 7, "apple"}

print(my_set)

# adding an element
my_set.add(8)

print(my_set)

# remove an element
my_set.remove(5)

print(my_set)

# membership testing
print(2 in my_set)

# Set operations
set_a = {1, 2, 3}
set_b = {3, 4, 5}

# union = {1, 2, 3, 4, 5}
# intersection = {3}
# difference = {1, 2}

# Union
union_value = set_b.union(set_a)
print(union_value)

# Intersection
intersection_value = set_a.intersection(set_b)
print(intersection_value)

# Difference
difference_value = set_a.difference(set_b)
print(difference_value)