while True:
    n = int(input("What are the numbers: "))

    if n <= 0:
        continue
    else:
        break 

for _ in range(n):
    print(n)

# another way.................. 
while True:
    x = int(input("How many times ? "))
    if x > 0:
        break

for _ in range(x):
    print("Good morning")