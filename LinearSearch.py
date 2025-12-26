arr = list(map(int, input("Enter number:").split()))
key = int(input("Enter key:"))
found = False   
for i in arr:  
    if i == key:
        found = True
        break
if found:      
    print("Found")
else:
    print("Not Found")
