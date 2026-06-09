def main():
    due = 50
    

    while True:
        print(f"Amount Due:{due}")
        denomination = int(input("Insert coin: "))
        
        if denomination != 25 and denomination != 10 and denomination != 5:
            continue
    
        due = due - denomination
        
        if due > 0:
            continue
            
        else:
            print(f"Change Owed:{abs(due)}")
            break
    


main()