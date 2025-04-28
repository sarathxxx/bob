currect_password = "sarath@32"
chance = 0
while chance < 4:
    input_password = input("Enter your password: ")
    if input_password != currect_password:
        chance += 1
        print("Incorrect password, please try again.")
    else:
        print("Access granted!")
        break
else:
    print("try again after 1 hour")
