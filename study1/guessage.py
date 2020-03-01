# Author:Fuhong Gao

age_of_gfh = 21
count = 0
while count < 3:
    guess_age = int(input("please guess age:"))
    if age_of_gfh == guess_age:
        print("Yes,you are right!")
        break
    elif age_of_gfh > guess_age:
        print("Think bigger..")
    else:
        print("Think smaller..")
    count += 1
    if count == 3:
        continue_confirm = input("Do you want to keep guessing?")
        if continue_confirm != "n":
            count = 0