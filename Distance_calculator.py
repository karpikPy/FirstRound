print("Distance converter. Input distance in feet to convert into: inches, yards, or miles")
feet = float(input("Distance in feet: "))

#dst is distance

conversions = {
    "inch": feet * 12,
    "inches": feet * 12,
    "foot": feet,
    "feet": feet,
    "yard": feet / 3,
    "yards": feet / 3,
    "mile": feet * 0.000189393939,
    "miles": feet * 0.000189393939 # nah man wth is this number :skull:
}

def conversion():
    input_dst = str(input("Name of length unit: ")).lower()

    if input_dst in conversions:
        converted_dst = conversions[input_dst]
        if input_dst in ["mile", "miles"]: # since feet to miles gives idiotic number it get it's own if to round it up
            rounded_up = round(converted_dst, 2)
            print(feet, "feet is equal to", rounded_up, input_dst)
        elif input_dst in ["foot", "feet"]:
            print("NO WAY", feet, "FEET IS EQUAL TO", converted_dst, input_dst) # just a little joke from me, don't really think I should explain it
            print("wow, who would've guessed?")
        else:
            print(feet, "feet is equal to", converted_dst, input_dst)
    else:
        print("Mistake. Skill issue from your side not gonna lie")

conversion()
