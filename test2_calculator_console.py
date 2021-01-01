print("Hello It's Calculator")
print("Press ENTER if you want to continue")
input()

while True:
    try:
        a = float(input("Insert First Number: "))
        operator = input("Choose the operator. (+, -, *, /): ")
        b = float(input("Insert Second Number: "))
    except:
        print("It is not a number")
    else:
        if operator == "+":
            print("\n%.2f + %.2f \n= %.2f"%(a, b, a+b))

        elif operator == "-":
            print("\n%.2f - %.2f = \n%.2f"%(a, b, a-b))

        elif operator == "*":
            print("\n%.2f * %.2f = \n%.2f"%(a, b, a*b))

        elif operator == "/":
            if b == 0:
                print("You can't devide by 0")
            else:
                print("\n%.2f / %.2f = \n%.5f"%(a, b, a/b))
            
        else:
            print("Wrong operator...")
            
    finally:    
        print('If you want to quit, tell me "quit"')
        print("Press Enter to try again")
        if input() == "quit":
            break

print("==========END===========")
input("Press ENTER to exit")
