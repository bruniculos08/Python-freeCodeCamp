# Working with strings
phrase = ("Giraffe\n\"Academy\"") # "\n" is used to jump to a new line. '\"' is used to print quotes(")
print(phrase.lower() + "is cool")
print(phrase.upper() + "is cool")
print(phrase.islower()) # it will print return (and print in this case) true or false if the text is all lower case (se o texto estiver todo em letra minúscula)
print(phrase.upper().isupper()) # it will printe always true
print (len(phrase)) # it will print the length of the string phrase
print(phrase[0]) # it will print the first character (G), it begin counting at position 0
print(phrase.index("Acad")) # it will print the position where the given parameter "Acad" starts inside of the string (9 in this case)
print(phrase.index("z")) # it will print a error because the given parameter "z" does not exist in the string phrase
print(phrase.replace("Giraffe", "Elephant")) #it will print the phrase changing the word "Giraffe" by "Elephant"