def heightinchesfeet(cm):
    inches = 0.394 * cm
    feet = 0.0328 * cm
    print("The length in inches", round(inches,2))
    print("The length in feet", round(feet,2))

cm = int(input("Enter the height in centimeters: "))
heightinchesfeet(cm)