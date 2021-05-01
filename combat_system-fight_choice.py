
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



        
