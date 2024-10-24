'''
Name: Duncan Staats
Date: 10/24/24
Description: For loops
'''
#'''
# for loop style 1 -for i in range(stop)
# this prints 0, 1, 2, 3, 4 each on their own line
# the number in range(stop) is how many nums are printed
# starting at 0 and ending at stop-1

#common use:doing a known number of things
for i in range(5):
    print(i)

#num on the same line
for i in range(5):
    print(i,end=" ")
print()
for i in range(5):
    print(i,end=", ")
print()

#for loop style 2 -for i in range(start, stop)
# this prints start, start+1, ...., stop-1
#loop runs stop - start number of times

for num in range(2,6):
    print("*"*num)

for num in range(2,6):
    print(num,end=" ")
print()
################################################
print(f"--------")
print("x | x^2")
for num_to_square in range(1,6):
    print(f"{num_to_square} | {num_to_square**2}")
print(f"--------")

print(num_to_square)

#for loop style 3 - for i in range(start, stop, step)
#this prints start, start+1, ...., stop-1 but counts by steps
#loop runs ceiling((stop-start)/step) times
for number in range(10,40,4): # want: 10 to 40 counting by 4s
    print(number, end = " ")
print()
# start at 12, count by 7s up to but not past 93
for i in range(12,93,7):
    print(i, end = " ")
print()
########################################
#print the sum of the numbers 1 through n

user_num = int(input("Give me a number: "))
sum = 0 # intialize our sum to 0
for num in range(1,user_num+1):
    sum = sum + num

print(f"The sum is {sum} ")
#'''
###################################################
#ask the user to enter 5 numbers (hint: use a loop
# find the average of those numbers ^
# print the average of your numbers is -----"

# my try
user_num1 = int(input("Give me a number: "))
user_num2 = int(input("Give me a number: "))
user_num3 = int(input("Give me a number: "))
user_num4 = int(input("Give me a number: "))
user_num5 = int(input("Give me a number: "))

sum1 = user_num1 + user_num2 +  user_num3 + user_num4 + user_num5
sum2 = sum1/5
print(f"The average of your numbers is {sum2}.")

# teach's try
user_sum = 0
for i in range(5):
    user_num = int(input("Enter a number: "))
    user_sum = user_num + user_sum
average = user_sum/5

print(f"The average of your numbers is {average}.")