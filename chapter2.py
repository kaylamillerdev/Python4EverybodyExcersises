choice = input("Pick an excersize: \n 2) Simply Named \n 3) Calculate PayRate \n 4) Width and Height  \n 5) Celcius to Farenheight \n")

if choice == 2:
    # Excersise 2
    name = input('Enter your name: ')
    print("Hello",name)
    
if choice == 3:
    # Excersise 3
    hours = input('Enter Hours: ')
    rate = input('Enter Rate: ')
    pay = float(hours) * float(rate)
    print("Pay:", pay)
    
if choice == 4:
    # Excersise 4
    width = 17
    height = 12.0

    print(type(width//2), width//2)
    print(type(width/2.0), width/2.0)
    print(type(height/3), height/3)

if choice == 5:
    # Excersise 5
    celcius = input('Enter the tempurature in Celcius: ')
    print("The tempurature in farenheight is: " + ((celcius * 9/5) + 32))