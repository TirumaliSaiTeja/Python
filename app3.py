# Building a car

command = ""
while command.lower()!= "quit":
    command = input("> ")
    if command == "start":
        print("Start the game")
    elif command == "stop":
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


