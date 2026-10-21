rooms = {"A" : "dirty", "B": "dirty"}
location = "A"

while True:
    if rooms[location]=="dirty":
        print("room", location, "is dirty")
        print("action: suck")
        rooms[location] = "clean"

    elif location == "A":
        print("move: right")
        location = "B"

    else:
        print("move: left")
        location = "A"

    if rooms["A"] == "clean" and rooms["B"] == "clean":
        print("all clean")
        break
