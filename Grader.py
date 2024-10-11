total = float(input("Total points possible: "))

score = float(input("Enter The Score: "))

answer = score / total * 100

if answer <= 50:
    print("F")
elif answer <= 51:
    print("D")
elif answer <= 61:
    print("C")
elif answer <= 76:
    print("B")
elif answer <= 89:
    print("A")