###--- Narcissistic Number Checker ---###

'''BACKGROUND:
In number theory, a narcissistic number (also known as a pluperfect digital invariant (PPDI), an Armstrong
number (after Michael F. Armstrong) or a plus perfect number) in a given number base b is
a number that is the sum of its own digits each raised to the power of the number of digits.

Examples:
1, 153, 370, 371, 407'''
import time

# A simple function to add "loading" times
def loading(num):
    for i in range(3):
        print (".", end = " ")
        time.sleep(num)
        
# Takes user input and responds   
userNum = (input("Enter a number and I'll check if it's truly narcissistic: "))
loading(0.5)
print ("\n" + (userNum) + " you say? Okay. I'll be right on it.")
loading(1)

# A function to check whether a number is narcissistic or not
def narcNumCheck():
    # Gets the number of digits in the user's number
    numLength = len(str(userNum))
    
    # Creates a place holder for the sum of all digits raised to the power of the number of total digits in the number
    numSum = int()
    
    # Iterates through each digit in the number
    for i in userNum:
        
        # Casts the current number (string) to an integer
        cur = int(i)
        
        # Stores the sum of all digits raised to the power of the number of total digits in the number
        numSum += (cur**numLength)
    
    # if the number is narcissistic, function returns true, and if not, it returns false
    if int(userNum) == numSum:
        return True
    else:
        return False
        
if (narcNumCheck()==True):
    print("\nYes! "+ (userNum) +" is a narcissistic number!")
else:
    print("\nNope. "+ (userNum) +" is  not a narcissistic number.")
