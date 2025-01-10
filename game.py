import os
import random
import time


with open("life.txt", "w") as file:
    file.write("Your heart beats. It's still alive... be careful out there.")

#----- STARTING SCREEN -----
print('|---------------------------------|')
print('| You are sitting in a dark room. |')
print('|  A gun is pointed at your face. |')
print('|    In front of you, a table.    |')
print('|    And on the table, a gun.     |')
print('|---------------------------------|')

time.sleep(2)
print("Well well well...")
time.sleep(2)
print("Let's have some fun, shall we?")
time.sleep(2)
print("                                  Terrified, you pick the gun.")
time.sleep(2)
print("                                     You know what comes next.")
time.sleep(2)
print("                                                    This is...")

time.sleep(3)
ascii_art = """
  ___            _             ___          _     _   _       
 | _ \_  _ _____(_)__ _ _ _   | _ \___ _  _| |___| |_| |_ ___ 
 |   / || (_-<_-< / _` | ' \  |   / _ \ || | / -_)  _|  _/ -_)
 |_|_\\_,_/__/__/_\__,_|_||_| |_|_\___/\_,_|_\___|\__|\__\___|
"""

print(ascii_art)

time.sleep(1)




def russian_roulette():
    global guessamount
    guessamount = 0
    death = random.randint(1, 6)

    def tries():
        global guessamount
        guess = input(f'Enter a number between 1 and 6. You already tried {guessamount} slots out of 6.\n> ')
        
        if not guess.isdigit():
            print("Don't try to escape your faith.")
            return tries()

        guess = int(guess)
        if guess < 1 or guess > 6:
            print("Don't try to escape your faith.")
            return tries()
        
        
        guessamount += 1
        if guessamount == 4:
            print("Two bullets left.")
            time.sleep(2)
            return tries()

        if guessamount == 5 and guess != death:
            print("One bullet left.")
            time.sleep(2)
            print("... You won.")
            time.sleep(2)
            print("How do it feel? To win?")
            time.sleep(2)
            print("It's okay. You can go now.")
            time.sleep(2)
            exit()


        if guess == death and guessamount != 5:
            print("Oops! Too bad... as you press the shoot button, the bullet shoots you right in your head, and blood appears in the air.")
            time.sleep(1)
            print("You died. And will now face the consequences.")
            time.sleep(1)
            os.remove("life.txt")

        elif guess == death and guessamount == 5:
            print("Oh no...")
            time.sleep(2)
            print("How sad.")
            time.sleep(2)
            print("You were so close, yet you lost.")
            time.sleep(2)
            print(".. Thanks for playing with me.")
            time.sleep(2)
            print("As you press the shoot button, the bullet shoots you right in your head, and blood appears in the air.")
            time.sleep(2)
            os.remove("life.txt")
            exit()
        else:
            print("The bullet didn't shoot. You are still alive.\n----------")
            time.sleep(1)
            return tries()

    tries()
russian_roulette()
