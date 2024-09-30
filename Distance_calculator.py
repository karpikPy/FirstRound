print("Distance converter. Input distance in feet to convert into: inches, yards or miles")
feet = float(input("Distance in feet: "))

#dst means distance, for those who don't understand lmao.

def Conversion():
    input_dst = str(input("Name of length unit: ")).lower()
    if input_dst == "inch" or input_dst == "inches":
        converted_dst = feet * 12
        print(feet, "feet is equal to", converted_dst, "inches")

    elif input_dst == "foot" or input_dst == "feet":
        converted_dst = feet
        print("NO WAY", feet, "FEET IS EQUAL TO", converted_dst, "FEET")
        print("Who would've guessed?")

    elif input_dst == "yard" or input_dst == "yards":
        converted_dst = feet / 3
        print(feet, "feet is equal to", converted_dst, "yards")

    elif input_dst == "mile" or input_dst == "miles":
        converted_dst = feet * 0.000189393939
        rounded_up = converted_dst.__round__(3)
        print(feet, "feet is equal to", rounded_up, "miles")

    else:
        print("Wrong unit of length or misspelling. Skill issue from your side not gonna lie")

Conversion()