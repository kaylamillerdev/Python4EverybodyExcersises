#!/usr/bin/env python3
exersiseChoice = input("Choose an excersise to test: \n 1) Hours and rate calculation \n 2) Hours and rate try except \n 3) Grading system \n")

choice = int(exersiseChoice)
if choice == 1:
    
    # Exersise 1
    hoursInput = input('Enter Hours: ')
    rateInput = input('Enter Rate: ')
    hours = float(hoursInput)
    rate = float(rateInput)

    if hours <= 40:
        pay = hours * rate
        print("Pay:", pay)
    else:
        overTimeHours = hours - 40
        overtimeRate = rate * 1.5
        pay = (overTimeHours * overtimeRate) + (hours * rate) 
        print("Pay:", pay)

if choice == 2:
    
    # Exersise 2
    hoursInput = input('Enter Hours: ')
    rateInput = input('Enter Rate: ')
    
    try:
        hours = int(hoursInput)
        rate = int(rateInput)
    except:
        print("Error, please enter numeric input")
        quit()
        
    if hours <= 40:
        pay = hours * rate
        print("Pay:", pay)
    else:
        overTimeHours = hours - 40
        overtimeRate = rate * 1.5
        pay = (overTimeHours * overtimeRate) + (hours * rate) 
        print("Pay:", pay)

# Exersize 3
if choice == 3:
    
    scoreInput = input("Please enter a score between 0.0 and 1.0: ")
    try:
        score = float(scoreInput)
    except:
        print("Please input a numerical value!")
        quit()

    if score >= 0.9:
        print("A")
    elif score >= 0.8:
        print("B")
    elif score >= 0.7:
        print("C")
    elif score >= 0.6:
        print("D")
    elif score < 0.6:
        print("F")