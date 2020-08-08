# Building a car

command = ""
started = False
while command!= "quit":
    command = input("> ").lower()
    if command == "start":
        if started:
            print('Car is already started!')
        else:
            started = True
            print("Start the game")
    elif command == "stop":
        if not started:
            print('Car is already stopped!')
        else:
            started = False
            print("Stop the game")
    elif command == "help":
        print("""
start
stop
quit
        """)
    elif command == "quit":
        break
    else:
        print("I Can't understand")


