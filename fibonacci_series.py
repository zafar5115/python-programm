nterm = int(input("How many terms ?"))

n1, n2 = 0, 1
count = 0
if nterm <= 0:
    print("Please enter a positive integer")
elif nterm == 1:
    print("fibonacci sequence upto",nterm, ":")
    print(n1)
else:
    print("fibonacci sequence:")
    while count < nterm:
        print(n1)
        nth = n1 +n2
        n1 = n2
        n2 = nth
        count += 1