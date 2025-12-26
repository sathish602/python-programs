text = input("Enter a string: ")
result = ""
for ch in text:
    duplicate = False
    for r in result:
        if ch == r:
            duplicate = True
            break
    if not duplicate:
        result = result + ch

print("String without duplicate:", result)
