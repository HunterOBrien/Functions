def check_status(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Normal"
    elif bmi > 30:
        return "Obese"


# main
get_bmi = int(input("Weight here: "))
print(f"With a bmi of {get_bmi} your status is {check_status(get_bmi)}")
