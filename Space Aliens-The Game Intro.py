def control_room():
    print("As you enter the bridge, you look around you see the main control panel, the bridge fridge, the star chart.\nHowever, the captain and bridge crew are no where to be seen.\n")

    while True:
        print("What do you do?")
        print(" 1) Go to the control panel. \n 2) Go to the bridge fridge. \n 3) Go to the star chart. \n (Answer 1, 2 or 3)")
        playerInput=input()

        if playerInput=="2":
            print("You look in the fridge. The only contents are some old bottles of space milk.")
            continue

        if playerInput=="3":
            print("You walk over to the star chart. It says the ship is currently in the Alpha Centauri star system and about 0.1 light years from Proxima Centauri b.")
            continue

        if playerInput=="1":
            break
    

def console_riddle():

    print("Welcome.")
    print("Please follow the following riddle access the control panel.\n")

    import time
    time.sleep(1)

    print("A man dies and needs to go to heaven, but an angel and devil is blocking his way. The man needs to say something to both of them at the same")
    print("time in order to reach heaven, but the devil does the opposite of what the man says and the angel does what the man asks.")
    print("What does the man need to say to both of them in order to go to heaven?") 

    for i in range(3, 0, -1):
        time.sleep(1)
        user_answer = input("\nPlease type in your answer: ")
        user_answer = user_answer.lower()

        if "where you live" in user_answer:
            print("Access granted, human identified. Good day, Rob Boss.")
            break

        else:
            print("Acess denied.")
            print("Chances left: " + str(i-1) + "\n")

            if i - 1 == 0:
                print("Releasing organism killing gas to remove non human objects...\n")
                time.sleep(1)
                print("GAME OVER.")

                import sys
                sys.exit

            continue




#-----------------------------------------------------------------------------------------Start Screen-----------------------------------------------------------------------------------------

print("     _______..______      ___       ______  _______         ___       __       __   _______ .__   __.      _______.      .___________. __    __   _______      _______      ___      .___  ___.  _______ ")
print("    /       ||   _  \    /   \     /      ||   ____|       /   \     |  |     |  | |   ____||  \ |  |     /       | _    |           ||  |  |  | |   ____|    /  _____|    /   \     |   \/   | |   ____|")
print("   |   (----`|  |_)  |  /  ^  \   |  ,----'|  |__         /  ^  \    |  |     |  | |  |__   |   \|  |    |   (----`(_)   `---|  |----`|  |__|  | |  |__      |  |  __     /  ^  \    |  \  /  | |  |__   ")
print("    \   \    |   ___/  /  /_\  \  |  |     |   __|       /  /_\  \   |  |     |  | |   __|  |  . `  |     \   \              |  |     |   __   | |   __|     |  | |_ |   /  /_\  \   |  |\/|  | |   __|  ")
print(".----)   |   |  |     /  _____  \ |  `----.|  |____     /  _____  \  |  `----.|  | |  |____ |  |\   | .----)   |    _        |  |     |  |  |  | |  |____    |  |__| |  /  _____  \  |  |  |  | |  |____ ")
print("|_______/    | _|    /__/     \__\ \______||_______|   /__/     \__\ |_______||__| |_______||__| \__| |_______/    (_)       |__|     |__|  |__| |_______|    \______| /__/     \__\ |__|  |__| |_______|")
print("                                                                                                                                                                                                         ")

while True:
    
    print("Ready to Play? (y/n)")
    playerInput=input()
    
    playerInput = playerInput.lower()

    if "n" in playerInput:
        continue
    elif "y" in playerInput:
        break

import time

time.sleep(1)
        
#-----------------------------------------------------------------------------------------Start of Game-----------------------------------------------------------------------------------------

print("You wake to see the green glow of your alarm clock, it is almost time to get to your station.\nYou are an engineer on the spaceship Lambent Light, your job is to make sure the ships fusion drive runs smoothly.")
print("However, as you leave your cabin and begin to walk to you station, you notice that something is wrong...\nThe regular hustle and bustle of a ship is no where to be found.\nWhere are all of the people?\n")

print("What do you do?")

print(" 1) Walk to your station.\n 2) Walk to the bridge. \n (Answer 1 or 2)")

playerInput=input()

if playerInput=="1":
    time.sleep(0.5)
    print("You decide to head to your station, simply putting off the fact that there are no humans to be seen during one of the busiest times of the day.\n")
    time.sleep(1.4)
    print("***2 minutes later***\n")
    time.sleep(1)
    print("As you walk through the engine room's blast door, the sounds of tearing of metal and depressurization alarms rip through the air.  \nYour training tells you that none of these sounds are positive.\n")

    print("If you do not make a decision quickly, you have a high likelyhood of being sucked out into space!!")
    print(" 1) Run out of the engine room and shut the blast door. \n 2) Run into the engine room. \n 3) Ignore it. These things malfunction occasionaly. \n (Answer 1,2 or 3)")

    
    playerInput=input()

    if playerInput=="1":
        print("You shut the door just in time to save yourself. Remembering protocol, you head to the bridge to inform the captain of the hull breach.\n")
        time.sleep(1.4)
        control_room()

    elif playerInput== "2" or "3":
        time.sleep(1)
        print("Time seems to slow down as the wall in front of you buckles and tears open. You are sucked into the endless void known as space, never to be seen again")
        time.sleep(1)
        print("____    ____  ______    __    __      __        ______        _______. _______ ")
        print("\   \  /   / /  __  \  |  |  |  |    |  |      /  __  \      /       ||   ____|")
        print(" \   \/   / |  |  |  | |  |  |  |    |  |     |  |  |  |    |   (----`|  |__   ")
        print("  \_    _/  |  |  |  | |  |  |  |    |  |     |  |  |  |     \   \    |   __|  ")
        print("    |  |    |  `--'  | |  `--'  |    |  `----.|  `--'  | .----)   |   |  |____ ")
        print("    |__|     \______/   \______/     |_______| \______/  |_______/    |_______|")

        import sys
        sys.exit()

if playerInput=="2":
    print("You walk to the bridge.\n")
    time.sleep(1)
    control_room()

console_riddle()
            

