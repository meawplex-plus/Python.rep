print("Welcome to I Aged....")

age = int(input("Input your age - INTEGERS ONLY! Age: "))
if age < 0:
    print("Invalid value   Program failed")
else:
    name = input("Input your name. Name: ")
    adder = int(input("How much would you like to add to your age? Added years: "))
    if adder >= 2:
        age=age+adder
        print(name,"in",adder,"years, you will be",age)
    if adder == 0:
       print(name,", you will still be",age,"if you don't add any years!")
    if adder == 1:
        print(name,"In",adder,"year, you will be",age)
        
    if adder < 0:
        print("Error: Cannot add -x   Program failed")

