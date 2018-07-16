import os
os.system("clear")

stopPoint = int(input("Enter a number"))
FB_file = open("fizzbuzz.txt", "w+")

for nums in range(1, stopPoint):
    if nums%5==0 and nums%3==0:
        print("FIZZBUZZ",nums, FB_file.write(str(nums)+ "\n"))
    elif nums%5 == 0:
        print("BUZZ", nums)
    elif nums%3 == 0:
        print("FIZZ", nums)
    else:
        print(nums)


