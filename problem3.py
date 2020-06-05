num1 = int(input("first num: "))
num2 = int(input("second num: "))
num3 = int(input("third num: "))

if((num1 > num2) & (num1 > num3)):
    print("largest number is :", num1)


if((num2 > num1) & (num2 > num3)):
    print("largest number is :", num2)

if((num3 > num2) & (num3 > num1)):
    print("largest number is :", num3)


if((num1 < num2) & (num1 < num3)):
    print("smallest number is :", num1)

if((num2 < num1) & (num2 < num3)):
    print("smallest number is :", num2)
if((num3 < num2) & (num3 < num1)):
    print("smallest number is :", num3)
