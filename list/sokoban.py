def main():
    histroy = []

    while True:
        action = input("Action: ")

        if action == "Undo":
            undone = histroy.pop()
            print(f"Undone: {undone}")
        elif action == "Restart":
            histroy.clear()
        else:
            histroy.append(action)
            
        print(histroy)
main()