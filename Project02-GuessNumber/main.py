import random
def guess(number):
    
    luck_num = random.randint(1,number)
    guess_num = 0
     
    while guess_num != luck_num:
        guess_num = int(input(f"Enter a number between 1 and {number}: "))
         
        if guess_num < luck_num:
            print("Too low, try again")
        elif guess_num > luck_num:
            print("Too high, try again")
        else:
            print("WOOOOOW")
    print(f"Yeah, you guesssed the correct, number is {luck_num} ")

def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        if low != high:
            
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f"Is {guess} is too high (H), too low (L) or correct (C)").lower()
        
        if feedback == "h":
            high = guess - 1
        elif (feedback == "l"):
            low = guess + 1
    print(f"Yay! The computer guessed your number, {guess}, correctly")
        
    
             
computer_guess(11)