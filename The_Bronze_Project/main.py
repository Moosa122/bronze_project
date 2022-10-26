#!C:\Users\Swati\AppData\Local\Programs\Python\Python311\python.exe

from sys import argv


if len(argv) >= 2:
    # Getting name of file
    name = argv[1]

    # Getting module type
    module = argv[2]

    # Modules
    modules = [
        "pygame"
    ]

    # Module templates
    templates = {
        "pygame": "import pygame\n\npygame.init()\n\nWIDTH, HEIGHT = 600, 800\nSCREEN = pygame.display.set_mode((WIDTH, HEIGHT))\n\nrunning = True\nwhile running:\n  for event in pygame.event.get():\n    if event.type == pygame.QUIT:\n      running = False"
    }

    # Looping through all of the module types
    for a_module in modules:
        if module != a_module:
            print(f"No module found with name {module}.")

        else:
            with open(f"{name}.py", "w") as file:
                file.write(str(templates["pygame"]))

            print(f"Done Making/Editing file of name {name}.py")

else:
    print("Please enter 2 arguments.\n\nbronze <name of file to made or edited> <module>\n")