import sys
user_input = input()
nums = []

for values in range(len(user_input)):
    nums.append(user_input[values])

try:
    print(int(nums[0]) // int(nums[1]))
except ZeroDivisionError as e:
    sys.stdout.write('Error Code', e)
except ValueError as err:
    sys.stdout.write('Error Code', err)
