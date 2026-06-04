def main():
    num = int(input("number: "))

    if is_even(num):
        print("even")
    else:
        print("odd")    

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False  

main()

