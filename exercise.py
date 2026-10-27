username=input("enter the name")
if len(username)>12:
    print("the username length should be less than 12")

elif username.isalpha()==False:
    print("the username should not contain space and digit")
else:
    print("validate username")


