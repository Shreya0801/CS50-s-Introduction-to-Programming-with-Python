# def main():
#     spacecraft = {"name": "Voyager 1", "distance" : 163}
#     print(create_report(spacecraft))

# def create_report(spacecraft):
#     return f"""
#     ===================REPORT===================
#     Name: {spacecraft["name"]}
#     Distance: {spacecraft["distance"]}AU
#     """
 
# main()

#=================================================================================================================================================
# def main():
#     spacecraft = {"name":"Voyager 1", "distance":"163"}
#     spacecraft["orbit"] = "sun"
#     print(create_report(spacecraft))


# def create_report(spacecraft_data):
#     return f""" 
#     ==========REPORT===========
#     Name: {spacecraft_data["name"]}
#     Distance: {spacecraft_data["distance"]} AU
#     Orbit: {spacecraft_data["orbit"]}
#     """

# main()

#=================================================================================================================================================

def main():
    spacecraft = {"name" : "James Webb Space Telescope"}
    # spacecraft["distance"] = 0.01
    spacecraft.update({"distance" : 0.01, "orbit" : "sun"})
    print(create_report(spacecraft))

def create_report(spacecraft_data):
    return f"""
    ============REPORT=============
    Name: {spacecraft_data.get("name","unknown")}
    Distance: {spacecraft_data.get("distance", "unknown")} AU
    Orbit: {spacecraft_data.get("orbit", "unknown")}
    """
main()