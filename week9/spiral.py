import logging
logging.basicConfig(level=logging.DEBUG)

# Step 1: Find pattern
# 1
# 3, 5, 7, 9 - odd nums
# 13, 17, 21, 25 - odd nums skipping 1
# top-right diag is all squared numbers

# Step 1: Find last number of max
last_num = 501 ** 2

# Step 2: Generate odd numbers list, all diag numbers are odd
odd_num = range(1,last_num+1,2)

# Step 3: Account for added space between numbers every time we pass 4 corners
skip = 1

# Step 4: While loop until last number, 4 represents the corners
i = 0
answer = 1
while odd_num[i] != last_num:
    for n in range(4):
        i += skip
        answer += odd_num[i]
    skip += 1



print(answer)
