name = str(input('Enter your first and last name:'))
weight = int(input('Enter your weight in kilograms:'))
height= int(input('Enter your height in meters:'))

BMI=weight/(height**2)
if BMI<18.5:
    print("Mr/ Mrs" +' ' + name+' ' + "you are underweight.")
elif 18.5 <= BMI <= 24.9:
    print("Mr/ Mrs" +' ' + name+' ' + "you are normalweight.")
elif 25 <= BMI <= 29.9:
    print("Mr/ Mrs" +' ' + name+' ' + "you are overweight.")
elif 30<= BMI <= 34.9:
    print("Mr/ Mrs" +' ' + name+' ' + "you are obese.")
else:
    print("Mr/ Mrs" +' ' + name+' ' + "you are extremely obese.")
