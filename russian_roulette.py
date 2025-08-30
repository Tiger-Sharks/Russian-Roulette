import os
import time
import random
import platform

def russian_roulette():
    print(r"""
.---------------------------------------------------------------------------.
|__        __   _                            _                              |
|\ \      / /__| | ___ ___  _ __ ___   ___  | |_ ___                        |
| \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \                       |
|  \ V  V /  __/ | (_| (_) | | | | | |  __/ | || (_) |                      |
| __\_/\_/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/  _      _   _       _ |
||  _ \ _   _ ___ ___(_) __ _ _ __   |  _ \ ___  _   _| | ___| |_| |_ ___| ||
|| |_) | | | / __/ __| |/ _` | '_ \  | |_) / _ \| | | | |/ _ \ __| __/ _ \ ||
||  _ <| |_| \__ \__ \ | (_| | | | | |  _ < (_) | |_| | |  __/ |_| ||  __/_||
||_| \_\\__,_|___/___/_|\__,_|_| |_| |_| \_\___/ \__,_|_|\___|\__|\__\___(_)|
'---------------------------------------------------------------------------'
""")
    print("Rules are simple:")
    print("Guess the number in 6 chances, or loose your system!")
    print("") # Spacer
    print("!! DISCALIMER !!")
    print("This is a serious deal. Incorrect answers will lead to deletion of critical file deletion.")
    print("We are not responsible for any loss happening due to the execution or share of this code!")

    bullet_position = random.randint(1, 6)
    chance = 6

    for attempt in range (1, chance + 1):
        try:
            guess = int(input(f"Attempt {attempt}: Enter your guess (1 to 6):  "))
            if guess < 1 or guess > 6:
                print ("Please enter a number between 1 to 6!")
                continue
            else:
                pass
        except ValueError:
            print ("That's not a valid nuber. Try again!")
            continue

        if guess == bullet_position:
            print("Boom! you guessed it right! You are safe!")
            chance = 0
            break
        else:
            print("You missed it! Let's have another round!")
    
    else:
        print("Game Over! You ran out of chances.")
        print("Time to say goodbye to your system!")

        # Warning!
        # The following code might proove dangerous
        # Again a reminder, we are not responsible for any loss that happens because of the cose

        system = platform.system()

        for _ in range (5, 0, -1):
            print (f"Shutting down system in {_} seconds ...")
            time.sleep(1)

        if system == "Windows":
            os.system("shutdown /s /t 0")
        elif system == "Linux":
            os.system("shutdown -h now")
        elif system == "Darwin":
            os.system("shutdown -h now")
        else:
            pass


russian_roulette()