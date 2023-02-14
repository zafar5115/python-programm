def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y

print("selecct operation")
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.divide")

while True:
    choice=input("plese select(1/2/3/4):")
    if choice in('1','2','3','4'):
        try:
            n1=float(input("enter first number"))
            n2=float(input("enter second number"))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
            
        if choice =='1':
            print(n1, "+",n2, "=", add(n1,n2))
            
        elif choice =='2':
            print(n1, "-",n2, "=", subtract(n1,n2))
            
        elif choice =='3':
            print(n1, "*",n2, "=", multiply(n1,n2))
            
        elif choice =='4':
            print(n1, "/",n2, "=", devide(n1,n2))
            
        nxt=input("do you next calculation? (yes/no)")
        if next == 'no':
            break
    else:
        print("Invalid Input") 