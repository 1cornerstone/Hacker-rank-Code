
# Given an integer, , perform the following conditional actions:
#
# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5 , print Not Weird
# If n is even and in the inclusive range of 6 to 20 , print Weird
# If  n is even and greater than 20 , print Not Weird


print(2 // 2)

n = input("enter the number: ")

if int(n) % 2 > 0:
    print("Weird")
else:
    if int(n) <= 5:
        print('Not Weird')
    elif int(n) <= 20:
        print("Weird")
    else:
        print("Not Weird")
