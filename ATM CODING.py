print("Welcome To The ATM ! ")

print("Please Enter Card ! For Further Transaction ! ")

print("Okay Entered ! It Takes Some Time For Processing ! ")

print("Succesfull ! ")

lr = ['2222']

Card = input("Please Input Your Card ! ")

pin = input("Enter Your Pin !")

itr = 0
cnt = 3

while itr < cnt :
    if pin in lr :
        print("Processing Your card %s of  pin %d is succesful and your cash  Will Given !"%(Card,2222))
        break

    else :
        print("Sorry Wrong Pin ! ")    
itr = itr + 1


