name = input("What is your name? ")

# if name == 'Harry' or name =='Hermione' or name =='Ron':
#     print("Greyffindor")
# elif name == 'Draco':
#     print("Slytherin") 
# else:
#     print("Who ? ")      

# match name:
#     case 'Harry':
#         print("Greyffindor")
#     case 'Hermione':
#         print("Greyffindor")   
#     case 'Ron':
#         print('Greyffindor')
#     case 'Draco':
#         print('Slytherin')
#     case _:
#         print('Who ?')    


# another way......

match name:
    case 'Harry' | 'Hermione' | 'Ron':
        print("Greyffindor")
    case  'Draco':
        print("Slytherin")
    case _:
        print("Who ?")    
