def console_riddle():
    print("Welcome.")
    print("Please follow the following riddle to open the door.\n")

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


console_riddle()
