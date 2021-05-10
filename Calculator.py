def add(x,y):
    return x + y
def subtract(x,y):
    return x - y
def multiply(x,y):
    return x * y
def divide(x,y):
    return x/y

print("Selection operation")
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.divide")

while True:
    choice = input("Enter choice(1,2,3,4)")
    if choice in ('1','2','3','4'):
        num1 = float(input("Enter First number "))
        num2 = float(input("Enter second number"))
        if choice== '1':
            print("adition ",add(num1,num2))
        elif choice == '2':
            print("subtract is ",subtract(num1,num2))
        elif choice== '3':
            print("adition ",add(num1,num2))
        elif choice == '1':
            print("adition ", divide(num1, num2))
        break
    else:
        print("Invalid Input")