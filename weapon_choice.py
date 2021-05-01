player_health = 0
player_attack = 0
player_rechargeTime = 0

def weapon_choice():
    global player_attack
    global player_health
    global player_rechargeTime

    print("\nI need to save these guys. I can't just leave them here to die! I need to do something! I'm going to try and save them!")
    time.sleep(2)
    print("\nThere should be a weapon vault here in the control room in case of emergencies.")
    time.sleep(2)
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

    



