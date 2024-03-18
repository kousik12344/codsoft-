n=int(input("Enter a number: "))
m=int(input("Enter a number: "))
choice=input("Enter an operation to perform : ")
match choice:
    case "+":
        print("The addition is:",n+m)
    case "-":
        print("The subtraction is:",n-m)
    case "*":
        print("The product is:",n*m)
    case "/":
        print("the division is:",n/m)
    case _:
        print("not valid operation try again")
        
