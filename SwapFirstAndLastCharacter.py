s = input("Enter a string: ")
if len(s) <= 1:
    print("Swapped string:", s)
else:
    swapped = s[-1] + s[1:-1] + s[0]
    print("Swapped string:", swapped)
