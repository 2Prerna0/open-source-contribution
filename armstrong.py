#  18. Write a program that will check whether the number is armstrong
#  number or not

num = int(input("Enter a number: "))

num_digits = len(str(num))

armstrong_sum = sum(int(digit)** num_digits for digit in str(num))

if armstrong_sum == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
    


#  BY using function

def is_armstrong(num):
    original_num = num
    num_digits = 0
    temp = num
    
    #count number of digits
    while temp > 0:
        num_digits += 1
        temp //= 10

    #calculate Armstrong sum
    temp = num
    armstrong_sum = 0
    while temp > 0:
        digit = temp % 10
        armstrong_sum += digit ** num_digits
        temp //= 10
        
    return armstrong_sum == original_num

number = int(input("Enter the number. "))
if is_armstrong(number):
    print(f"{number} is an Armstrong number")
else:
    print(f"{number} is not an Armstrong number.")
