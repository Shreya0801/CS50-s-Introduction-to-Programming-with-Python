import sys


def main():
    # coordinates = (42.376, -71.115)
# print("Latitude: ", coordinates[0])
# print("Longitude: ", coordinates[1])

#############################################################
# longitude, latitude = coordinates
# print(f"Latitude: {latitude}")
# print(f"Latitude: {longitude}")

#############################################################
    coordinates_tupal = (42.376, -71.115)
    coordinates_list = [42.376, -71.115]

    print(f"{sys.getsizeof(coordinates_tupal)} bytes")
    print(f"{sys.getsizeof(coordinates_list)} bytes")




main()