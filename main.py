while True:
    height = float(input("Sizning boyingiz m: "))
    weight = float(input("Sizning vazningiz kg: "))

    bmi = weight / (height ** 2)
    # bmi = round(bmi, 1)

    if bmi < 18.5:
        print("Sizning BMI " + format(bmi, ".1f") + " Vazningiz kam")
    elif bmi > 18.5 and bmi < 24.9:
        print(f"BMI {bmi} Vazningiz o'rtacha")
    elif bmi > 25.0 and bmi < 29.9:
        print(f"BMI {bmi} Vazningiz o'rtiqcha")
    elif bmi == 30.0:
        print(f"BMI {bmi} Vazningiz semizlik darajasida")
    else:
        print(f"BMI {bmi} Siz Filsiz !!!")  


    # return "Your BMI is " + format(bmi, ".1f") + "(Obesity)"