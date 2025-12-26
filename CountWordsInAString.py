text = input("Enter string: ")
count = 0
in_word = False
for char in text:
    if char != " " and not in_word:
        count = count + 1
        in_word = True
    elif char == " ":
        in_word = False
print("Number of words:", count)
