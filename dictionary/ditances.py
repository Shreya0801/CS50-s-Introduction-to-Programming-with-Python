distances = {
    "Voyager 1" : 163,
    "Voyager 2" : 136,
    "Poineer 10" : 80,
    "New Horizons" : 58,
    "Poineer 11" : 44
}

# def main():
#     for name in distances.keys():
#         print(f"{name} is {distances[name]} AU from earth.")

def main():
    for distance in distances.values():
        print(f"{distance} is {convert(distance)} m from the earth.")

def convert(au):
    return au * 149597870700
main()