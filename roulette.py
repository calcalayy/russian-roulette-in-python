import random, time
#user input
name1 = input("Enter your name Player 1: ")
print("Hello", name1 + "!")

time.sleep(2)

#defining killed player
killed_p = random.randint(0, 6)

#the killing
if killed_p  == 1:
    print(name1 + " has died.")
else:
    print(f"Player {killed_p} has died.")

