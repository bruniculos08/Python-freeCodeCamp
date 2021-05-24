lucky_numbers = [4, 8, 15, 16, 23, 42, 7]
friends = ["Alfred", "John", "Jim", "Nike", "Mike", "James", "Jorge"]
print(friends) # just print the item friends' list
friends.extend(lucky_numbers) # adding the objects of the lucky numbers list at the end of the friends list
print(friends) # because of the previous used comand (friends.extend(lucky_numbers)) the list will be print together with the lucky numbers list in sequence 
friends.append("New") # it will add the string "New" in the actual end of the list
friends.insert(1, "Ben") # it will add the string "Ben" in the index 1 (the string "John" and the other will be pushed to the right) ; friends.insert(index, object)
friends.remove("James") # it will remove the string "James" from the list
friends.clear() # remove all the objects from the list
friends.pop() # remove the last object from the list (in this case the string "Jorge")
print(friends.index("Nike")) # show if the object is in the list (if it is not there will be returned a error messege) and in what index number is the object string "Nike"
friends = ["Alfred", "John", "Jim", "Jorge", "Nike", "Mike", "James", "Jorge"] # just to rebuild with 2 strings "Jorge" (there is anything new here)
print(friends.count("Jorge")) # it will print the number of objects like "Jorge"
friends.sort() # it will sort the list in ascending order (in this case it will be the same as alphabetical order)