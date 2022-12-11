import random

roll_again = ""
score = 0

print(r"""  
  ____
 /\' .\    _____
/: \___\  / .  /\
\' / . / /____/..\
 \/___/  \'  '\  /
          \'__'\/ 
                  """)

name = input(">>>Enter your name: ")

print(f"\n Welcome {name} to the dice game!!!")

print("  ---------------------------------- \n")

while roll_again == "":
    n = int(input("   >>Predict the number between 1 to 6: "))
    r = random.randint(1, 6)
    print("    Dice shows:        ", r, "\n")
    if (r == n):
        score += 1
        print("    Congrats. Your score is >>>", score)

    else:
        print("   Sorry, Your Prediction is Wrong. Your score is >>>", score)

    print("\n")
    print(">>> Press Enter to try again or press any alphabet to exit: ")
    roll_again = input()

print("\n   ---------------------------- ")
print("   ", name, "Your total score is >>>", score)