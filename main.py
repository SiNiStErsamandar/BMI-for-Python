while True:
    height = float(input("Sizning boyingiz m: "))
    weight = float(input("Sizning vazningiz kg: "))

    bmi = weight / (height ** 2)

    if bmi < 18.5:
        print(str(bmi) + " Vazningiz kam")
    elif bmi > 18.5 and bmi < 24.9:
        print(str(bmi) + " Vazningiz o'rtacha")
    elif bmi > 25.0 and bmi < 29.9:
        print(str(bmi) + " Vazningiz o'rtiqcha")
    elif bmi == 30.0:
        print(str(bmi) + " Vazningiz semizlik darajasida")
    else:
        print(str(bmi) + " Siz Filsiz !!!")  