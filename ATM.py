balance=2
def deposit(amount):
    global balance
    balance+=amount   
def withdraw(amount):
    global balance
    if amount<=balance:
        balance-=amount
    else:
        print("Insufficient amount")
deposit(0)
withdraw(200)
print("Balance:", balance)
