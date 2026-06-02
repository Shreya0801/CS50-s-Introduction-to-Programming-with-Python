def hello():
    print("Hello")


name = input("What's your name ? ")
hello()
print(name)


#We can further improve our code....

def hello(to="world"):
    print("hello "+to)

name = input("What's your name?")
hello(name)


# we need to tell the interpreter that we have a main function and a separate hello function.....

def main():
    name = input("What's name? ")
    hello(name)

def hello(to):
    print("hello", to)   

main()