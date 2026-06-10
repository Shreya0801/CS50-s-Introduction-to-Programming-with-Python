def main():
    names = ["Luigi","Daisy","Mario","Yoshi"]

    # for i in range(len(names)):
    #     print(letters_from(names[i],"Shreya"))

    for name in names:
        print(letters_from(name,"Sakshi"))

def letters_from(sender, receiver):
    return """
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Dear {receiver},
    You are cordially invited to a ball at
    Peach's Castle this evening, 7:00 PM.

    Sincerely,
    {sender}
"""

main()