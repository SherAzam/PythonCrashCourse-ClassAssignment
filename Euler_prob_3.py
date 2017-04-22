#num = 407
# take input from the user
# num = int(input("Enter a number: "))
# prime numbers are greater than 1
"""The prime factors of 13195 are 5, 7, 13 and 29.

problem: What is the largest prime factor of the number 600851475143 ?"""
my_num = 600851475143
factors = []
for num in range(2,600851475143):
    #factors = []
    if (my_num % num) == 0:
        if num > 1:
            for i in range(2,num):
                if (num % i) == 0:
                    break
            else:
                factors.append(num)
                print(factors)
 

       