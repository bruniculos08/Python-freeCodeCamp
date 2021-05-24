friends = ["Alfred", "John", "Jim", "Nike"] # the list can store multiple types of objects (string, integers, booleans, etc)
#index:      [0]       [1]     [2]    [3]
print(friends[1])  # it will print John
print(friends[-1]) # it will print Jim (when we use a negative number, the list will be scrolled from back to front)
print(friends[1:3]) # it will print the element in index [1], [2] (star printing at index [1] but stop printing at index [3])
friends[1] = "Mike" # Change the object saved in the index [1] from the list