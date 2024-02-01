import random

print("Welcome to the Guessing-Ground Game")
print("")
a = input("Enter player 1 name: ")
b = input("Enter player 2 name: ")
p1 = 0
p2 = 0
print("")
print("RULES: GUESS THE NUMBER FROM 1 TO 100")
print("If you guess the number CORRECTLY, +20 points")
print("If the number you guessed is at most distance of 10, +10 points")
print("If the number you guessed is at most distance of 20, +5 points")
print("And if you failed the above conditions, -5 points")

r = input("So are you ready: (Y/N)")
print("")
print("LET'S BEGIN THE FUN")
print("")
s = int(input("Select the number of rounds, you want to play (Only Even Number of RoundS Accepted): "))

for round_num in range(1, s + 1):
    num = random.randint(1, 100)
    print("ROUND",round_num,": It is the turn of",a)
    print("")
    g = int(input("GUESS (SELECT) THE NUMBER FROM 1 TO 100: "))

    if g == num:
        print("Perfect, +20 points")
        p1 += 20
    elif abs(num - g) <= 10:
        print("Ooohh...it was a close miss, +10 points")
        p1 += 10
    elif 20 >= abs(num - g) > 10:
        print("Keep trying, you may get it, +5 points")
        p1 += 5
    else:
        print("Noooo...bad hit, -5 points")
        p1 -= 5

    print("After this round, the score is:")
    print(a+":",p1)
    print(b+":",p2)

    a, b = b, a
    p1, p2 = p2, p1

print("")
print("Game Over")
print("")
print("And the Final scores are-")
print(a+":",p1)
print(b+":",p2)

print("")
if p1>p2:
    print("THE WINNER IS:",a)
elif p1==p2:
    print("IT'S A TIE, wanna play more!?")
else:
    print("THE WINNER IS:",b, "CONGRATULATIONS!")        
