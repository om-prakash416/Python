def LeapYear(Year):
    
    if (Year % 400 == 0) or (Year % 100 != 0 and Year % 4 == 0):
        print(" the given year ia an leap year")
        
    else:
        print("the given year is not a leap year")


Year = int(input("Enter the year to check wheather a leap year or not: "))

LeapYear(Year)