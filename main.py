
#common temperature units: C, F--> K

#Setting up important variables
value1 = input("Pressure: ")
unit1 = input("Pressure Unit: ")
value2 = input("Volume: ")
unit2 = input ("Volume Unit: ")
value3 = input("Number of moles: ")
value4 = input("Temperature: ")
unit4 = input ("Temperature Unit: ")

#ensuring that unknown values can be left blank by the user
if value1 != "":
    num1 = float(value1)
else: num1 = 0
if value2 != "":
    num2 = float(value2)
else: num2 = 0
if value3 != "":
    num3 = float(value3)
else:
    num3 = 0
if value4 != "":
    num4 = float(value4)
else:
    num4 = 0

#conversion options for pressure
if unit1 == "Pa" or "pa":
    num1 = num1/101325
else: num1 = num1
if unit1 == "mmHg" or "mmhg":
    num1 = num1/760
else: num1 = num1
if unit1 == "Torr" or "torr":
    num1 = num1/760
else: num1 = num1

#conversion options for volume
if unit2 == "mL" or "ml" or "Ml" or "ML":
    num2 = num2/1000
else: num2 = num2

#conversion options for temperature

if unit1 == "C" or "c":
    num4 = num4+273.15
else: num4 = num4
if unit1 == "F" or "f":
    num4 = (num4*(5/9)) + 273.15

#final calculations given the computed values
if value1 == "":
    out = (num3*0.0821*num4)/num2
    print(float(out))
elif value2 == "":
    out = (num3*0.0021*num4)/num1
    print(float(out))
elif value3 == "":
    out = (num1*num2)/(0.0821*num4)
    print(float(out))
elif value4 == "":
    out = (num1*num2)/(0.0821*num3)
    print(float(out))
