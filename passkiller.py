import argparse
import random

def random_choice(rang=10):
    for i in range(rang):
        password = ""
        for j in range(len(str(arguments.strings.split(":")))):
            password += random.choice(arguments.strings).replace(":", "")

        with open(arguments.filename, "a") as file:
            file.write(f"{password}\n")
    return "complete!"

def brute_force(rang=10):
    for i in range(rang):
        password = ""
        for j in arguments.strings.split(":"):
            while len(password) < 10:
                password += random.choice(arguments.strings.split(":"))
            break
        password = password.replace("brute", "")
        with open(arguments.filename, "a") as file:
            file.write(f"{password}\n")
    return "complete!"

def password_maker(rang=3):
    with open(arguments.filename) as file:
        words = file.readlines()

    password = ""
    for i in range(rang):
        password += f"{random.choice(words).strip()}"

    return f"complete: {password}"

if __name__ == "__main__":
    name = """
                         _    _ _ _
     _ __   __ _ ___ ___| | _(_) | | ___ _ __
    | '_ \ / _` / __/ __| |/ / | | |/ _ \ '__|
    | |_) | (_| \__ \__ \   <| | | |  __/ |
    | .__/ \__,_|___/___/_|\_\_|_|_|\___|_|
    |_|
    """
    parser = argparse.ArgumentParser(prog=name, description=": - used as separation", epilog="Available commands: random, brute, passmaker")
    parser.add_argument("--strings")
    parser.add_argument("--filename")
    parser.add_argument("--count")
    parser.add_argument("method")
    arguments = parser.parse_args()
    if arguments.method == "random":
        print(random_choice(rang=int(arguments.count)))

    elif arguments.method == "brute":
        print(brute_force(rang=int(arguments.count)))
    elif arguments.method == "passmaker":
        print(password_maker())
    else:
        print("What?")
