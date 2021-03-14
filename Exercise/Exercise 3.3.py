score = float(input("Enter Score: "))

if 0.0 <= score <= 1.0:
    if score < 0.6:
        print("F")
    elif score < 0.7:
        print("D")
    elif score < 0.8:
        print("C")
    elif score < 0.9:
        print("B")
    else:
        print("A")
else:
    print("The input is incorrect.")
    
quit()
