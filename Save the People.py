import time
import random

player_health = 0
player_attack = 0
player_rechargeTime = 0
    
civs_saved=0


def fight_choice(attack, health, reload):
    print("** A wild alien appears! **")

    time.sleep(2)

    player_choice = input("Flee or Fight?: ")
    player_choice = player_choice.lower()

    flee_chance = random.randint(1, 4)


    if "flee" in player_choice and flee_chance % 2 == 0:
        print("** You ran away! **")

    elif "flee" in player_choice and flee_chance % 2 != 0:
        print("** Failed to flee! **")
        combat_system(attack, health, reload)

    elif "fight" in player_choice:
        combat_system(attack, health, reload)

    else:
        print("** The system decides for you, and the system decides that you must fight! **")
        combat_system(attack, health, reload)
        

def combat_system(attack, health, reload):
    print("** You enganged a fierce battle with the wild alien! **")
    print("Hey, alien! It's time to die!")

    alien_hp = random.randint(150, 300)
    alien_hitchance = 0
        
    while True:
        alien_attack = random.randint(10, 30)
        if health < 25:
            midbattleflee_number = random.randint(1, 10)
            fight_or_flee = input("\n** Do you wish to keep fighting? **")
            if "fight" in fight_or_flee:
                print("** You continue to fight. **")
                continue
            elif "flee" in fight_or_flee and midbattleflee_number % 2 == 0:
                print("** You successfully fled! **")
                break
            elif "flee" in fight_or_flee and midbattleflee_number % 2 >= 1:
                print("** You can't flee right now! **")
                continue
        

        print("\n** You attacked the alien for " + str(attack) + " damage. **")
        alien_hp -= attack
        if alien_hp <= 0:
            print("I killed the alien!")
            print("** You have " + str(health) + " HP left. **")
            break
        time.sleep(reload)   
        print("The alien has " + str(alien_hp) + " HP left. **")
        time.sleep(1)
        alien_hitchance = random.randint(1, 100)
       
        if alien_hitchance % 2 >= 1:
            print("\n** The alien hits you for " + str(alien_attack) + " damage. **")
            health -= alien_attack
                    
            if health <= 0:
                print("** You died. Game over. **")
                sys.exit
            print("** You have " + str(health) + " HP left. **")
            continue
        elif alien_hitchance % 2 == 0:
            print("\n** The alien misses! **")
            continue



def door_code():
    var=random.randint(1,3)

    chances=3

    if var==1:
        print("print(""Open Door? (y/n)"")")
        print("playerInput==input()")
        print("__ playerInput==""y"":")
        print(" print(""Door Opening"")")
        print(" open_door()")
        print(" break")
        print("if playerInput==""n"":")
        print(" continue")

        while chances!=0:
            print("Input Code:")
            playerInput=input()
            if "if" in playerInput:
                print("Code Restored.\nDoor Opening.")
                break
            else:
                chances-=1
                print("Error: "+str(chances)+" chances left")
                
        
    elif var==2:
        print("print(""Open Door? (y/n)"")")
        print("playerInput==input()")
        print("if ___________==""y"":")
        print(" print(""Door Opening"")")
        print(" open_door()")
        print(" break")
        print("if playerInput==""n"":")
        print(" continue")

        while chances!=0:
            print("Input Code:")
            playerInput=input()
            if "playerInput" in playerInput:
                print("Code Restored.\nDoor Opening.")
                break
            else:
                chances-=1
                print("Error: "+str(chances)+" left")

        
    elif var==3:
        print("print(""Open Door? (y/n)"")")
        print("playerInput==input()")
        print("if playerInput==""y"":")
        print(" print(""Door Opening"")")
        print(" open_door()")
        print(" break")
        print("if playerInput==""_"":")
        print(" continue")

        while chances!=0:
            print("Input Code:")
            playerInput=input()
            if "n" in playerInput:
                print("Code Restored.\nDoor Opening.")
                break
            else:
                chances-=chances
                print("Error: "+str(chances)+" left")
                

def weapon_choice():
    global player_attack
    global player_health
    global player_rechargeTime

    print("\n** You walk over to the weapon vault and open it. **")
    time.sleep(2)
    print("\nThere is a plasma rifle with unlimited ammo, but it takes time to recharge and has lower shooting speed.")
    time.sleep(2)
    print("There is also a live ammo assault AR, which does more damage and has a higher firing speed, but there's not a lot of ammo left.\n")

    print("Which weapon do you choose?")
    
    while True:
        weapon_choice = input("Type \"p\" for the plasma rifle and \"l\" for the live ammo rifle: ")
        weapon_choice = weapon_choice.lower()

        if "p" in weapon_choice:
            print("\nYou have chosen the plasma rifle.")
            player_health = random.randint(100, 150)
            player_attack = random.randint(25, 100)
            player_rechargeTime = 4
            break

        if "l" in weapon_choice:
            print("\nYou have chosen the live ammo rifle.")
            player_health = random.randint(50, 100)
            player_attack = random.randint(75, 150)
            player_rechargeTime = 2
            break

        else:
            print("\nAlright, I don't need any weapons. I'm going in with my bare hands.")
            player_health = random.randint(10, 30)
            player_attack = random.randint(1, 10)
            player_rechargeTime = 0
            break


    print("\n** You have " + str(player_health) + " health, " + str(player_attack) + " attack and your reload time is " + str(player_rechargeTime) + ". **")


def control_room_choices():
    while True:
        print("What do you want to do?")
        time.sleep(1.5)
        print(" 1) Go to the microwave. \n 2) Go to the bridge fridge. \n 3) Go to the star chart. \n 4) Go to the weapon vault. \n (Answer 1, 2, 3, or 4)")
        playerInput=input()

        if playerInput=="1":
            print("The lone object in the microwave is a metal spoon.")
            time.sleep(1)
            print("Turn it on? (y/n)")
            playerInput=input()
            if playerInput== "y":
                time.sleep(0.5)
                print("You turn the microwave on.\n A bright flash is all you see as the ship is rocked by a massive explosion.")
                time.sleep(1)
                print("____    ____  ______    __    __      __        ______        _______. _______ ")
                print("\   \  /   / /  __  \  |  |  |  |    |  |      /  __  \      /       ||   ____|")
                print(" \   \/   / |  |  |  | |  |  |  |    |  |     |  |  |  |    |   (----`|  |__   ")
                print("  \_    _/  |  |  |  | |  |  |  |    |  |     |  |  |  |     \   \    |   __|  ")
                print("    |  |    |  `--'  | |  `--'  |    |  `----.|  `--'  | .----)   |   |  |____ ")
                print("    |__|     \______/   \______/     |_______| \______/  |_______/    |_______|")

                import sys
                sys.exit()

            else:
                continue

        if playerInput=="2":
            time.sleep(1)
            print("You look in the fridge. The only contents are some old bottles of space milk.")
            time.sleep(1)
            continue

        if playerInput=="3":
            time.sleep(1)
            print("You walk over to the star chart. It says the ship is currently in the Alpha Centauri star system and about 0.1 light years from Proxima Centauri b.")
            time.sleep(1)
            continue

        if playerInput=="4":
            time.sleep(1)
            weapon_choice()
            break

print("Do you help your crewmates? (y/n)")
playerInput=input()
playerInput=playerInput.lower()

if playerInput=="y":
    print("You know that your crewmates are being held in the brig.\nThe trick, will be getting there alive.")
    print("Do you want to do anything before you leave? (y/n)")

    playerInput=input()
    playerInput=playerInput.lower()

    if playerInput=="y":
        control_room_choices()

    else:
        print("Alright, I don't need any weapons. I'm going in with my bare hands.")
        player_health = random.randint(10, 30)
        player_attack = random.randint(1, 10)
        player_rechargeTime = 0

time.sleep(1)        
print("You leave the bridge and begin to walk towards the location of the surviving crew.")
time.sleep(1)
print("Soon you reach an intersection. You peer around the corner to see two aliens!\nThey both seem to have some sort of weapon, however, you cannot tell what it is.")
time.sleep(2)
print("Do you want to:\n 1) Try to sneak past them.\n 2) Attack them.\n (Answer 1 or 2)")
playerInput=input()
playerInput=playerInput.lower()

if playerInput=="1":
    time.sleep(0.5)
    print("While their backs are turned, you sprint across the intersection.\nIt seems that they didn't notice you.")
    time.sleep(1)
    print("However, as you continue down the hallway, you reach a malfunctioning blast door.\nAbove it, is a sign reading *Bridge Crew Cabins*\nThe only way to continue is to fix the door.")

if playerInput=="2":
    fight_choice()
    print("You continue down the hallway.")
    
while True:
    print("Access the console? (y/n)")
    playerInput=input()
    if playerInput=="n":
        continue
    if playerInput=="y":
        break

print("As you look at the console, an alert pops up on the screen.")
time.sleep(1)
print("**Error Section of Software Deleted**")
time.sleep(1)
print("The only way to get through the door is to fix the software.\nLet's see what the problem is.")
print("**Fill in the underline(_____) with the correct code.**\n")
time.sleep(1)
door_code()

print("You slip through the door and into the next hallway.\nYou begin to look into the cabins for any survivors.\nAs you reach the last door, you see a scared face staring out at you.")
time.sleep(2)
print("Open the door to save the man? (y/n)")
playerInput==input()

if playerInput=="y":
    print("You access the console to open the door.\n However, you see a similar problem as the previous door that let you have access to the cabin you are currently in.")
    print("You will have to fix the code.")
    print("**Fill in the underline(_____) with the correct code.**\n")
    time.sleep(1)
    door_code()
    print("The man thanks you as the door opens.\nYou tell him to get to the escape pods.")
    civs_saved+=1
    
else:
    print("You decide to leave the man behind.\n He bangs on the door to get your attention, but you just continue on.")

print("You continue on to the brig.")
time.sleep(1.5)
print("**5 minutes later**")
time.sleep(1.5)
print("You stare down the hallway, in front of the brig's door is an alien.")
time.sleep(1)
print("There is no way you will be able to sneak past him.")
time.sleep(1)
print("Your only options are to:\n 1)Run and leave your crewmates behind.\n 2)Fight the alien.\n Answer(1 or 2)")

playerInput=input()

if playerInput=="1":
    user_leaves()
    
else:
    print("You decide to fight the alien.")
    fight_choice()

    print("You go to open the door... t doesn't open.")
    print("However did the coding on this ship is really bad.")
    print("**Fill in the underline(_____) with the correct code.**\n")
    door_code()
    print("You enter the room to see 10 of your crew mates.")
    print("You all run to the nearest escape pod.")
    print("However as you open the secape pod door, you see that the maximum capacity is 10.")
    print("Do you leave someone behind or stay behind yourself?\n (Remember, JIM stole your orange juice the day before.)")
    time.sleep(1)
    print(" 1)Stay behind. 2)Leave JIM behind. Answer(1 or 2)")
    playerInput==input()

    if playerInput=="1":
        civs_saved+=10
        print("You decide to stay behind.")
        time.sleep(1)
        print("You saved " + str(civs_saved) + "people.")
        time.sleep(1)
        print(".___________. __    __       ___      .__   __.  __  ___      _______.    _______   ______   .______         .______    __          ___   ____    ____  __  .__   __.   _______ ")
        print("|           ||  |  |  |     /   \     |  \ |  | |  |/  /     /       |   |   ____| /  __  \  |   _  \        |   _  \  |  |        /   \  \   \  /   / |  | |  \ |  |  /  _____|")
        print("`---|  |----`|  |__|  |    /  ^  \    |   \|  | |  '  /     |   (----`   |  |__   |  |  |  | |  |_)  |       |  |_)  | |  |       /  ^  \  \   \/   /  |  | |   \|  | |  |  __  ")
        print("    |  |     |   __   |   /  /_\  \   |  . `  | |    <       \   \       |   __|  |  |  |  | |      /        |   ___/  |  |      /  /_\  \  \_    _/   |  | |  . `  | |  | |_ | ")
        print("    |  |     |  |  |  |  /  _____  \  |  |\   | |  .  \  .----)   |      |  |     |  `--'  | |  |\  \----.   |  |      |  `----./  _____  \   |  |     |  | |  |\   | |  |__| | ")
        print("    |__|     |__|  |__| /__/     \__\ |__| \__| |__|\__\ |_______/       |__|      \______/  | _| `._____|   | _|      |_______/__/     \__\  |__|     |__| |__| \__|  \______| ")
        print("                                                                                                                                                                                ")
        
    if playerInput=="2":
        civs_saved+=9
        print("You throw JIM out of the escape pod.\n This is what you get for stealing my orange juice!")
        print("The escape pod ejects from the ship.")
        time.sleep(1)
        print("You saved " + str(civs_saved) + "people.")
        time.sleep(1)
        print(".___________. __    __       ___      .__   __.  __  ___      _______.    _______   ______   .______         .______    __          ___   ____    ____  __  .__   __.   _______ ")
        print("|           ||  |  |  |     /   \     |  \ |  | |  |/  /     /       |   |   ____| /  __  \  |   _  \        |   _  \  |  |        /   \  \   \  /   / |  | |  \ |  |  /  _____|")
        print("`---|  |----`|  |__|  |    /  ^  \    |   \|  | |  '  /     |   (----`   |  |__   |  |  |  | |  |_)  |       |  |_)  | |  |       /  ^  \  \   \/   /  |  | |   \|  | |  |  __  ")
        print("    |  |     |   __   |   /  /_\  \   |  . `  | |    <       \   \       |   __|  |  |  |  | |      /        |   ___/  |  |      /  /_\  \  \_    _/   |  | |  . `  | |  | |_ | ")
        print("    |  |     |  |  |  |  /  _____  \  |  |\   | |  .  \  .----)   |      |  |     |  `--'  | |  |\  \----.   |  |      |  `----./  _____  \   |  |     |  | |  |\   | |  |__| | ")
        print("    |__|     |__|  |__| /__/     \__\ |__| \__| |__|\__\ |_______/       |__|      \______/  | _| `._____|   | _|      |_______/__/     \__\  |__|     |__| |__| \__|  \______| ")
        print("                                                                                                                                                                                ")
        


    

    


    
    
    
    
    
