import time  # This is for delay

def washing_messages(seconds):
    messages = [
        "Still washing...",
        "You guessed it, still washing...",
        "Take it easy, it's still washing...",
        "NO WAY",
        "Nah, I am just messing with you",
        "Maybe someday it will finish...",
        "Patience is key... and soap.",
        "Washing machine goes brrr",
        "Don't worry, it should be done... eventually.",
        "Good things take time... or at least clean clothes do.",
        "Washing machines have their own sense of time."
    ]


    print("Washing your clothes... Please wait.")
    time.sleep(1)

    for i in range(seconds):
        print(messages[i % len(messages)])  # Looping messages
        time.sleep(1.5)

    print("For real tho, just a few minutes")
    time.sleep(5)
    print("And you're good to go")


# Program starts here
print("Washing machine simulator", end="\n\n")

clothes = str(input("Write what clothes you want to wash, dividing with spacebar: ").split())
length_clothes = len(clothes)

washing_modes = {
    "1": ("Normal/Cotton", [40, 50, 60]),  # these numbers are just minutes, depending on the amount of clothes the user washes
    "2": ("Delicate/Gentle", [30, 40, 50]), #names of the modes and time are from ChatGPT
    "3": ("Heavy Duty", [60, 75, 90]),
    "4": ("Quick Wash", [10, 20, 30]),
    "5": ("Wool/Hand Wash", [30, 45, 60]),
    "6": ("Rinse and Spin", [10, 20, 30])
}

for number, (name, _) in washing_modes.items():  # _ is to ignore unnecessary variable
    print(f"{number} -- {name}")

print(" ")

mode = input("Choose mode (number): ")

if mode not in washing_modes:
    print("Invalid mode selected. Do better bozo")
    exit()

mode_name, time_ranges = washing_modes[mode]

# Calculate wash time based on the number of clothes
if length_clothes < 3:
    wash_time = time_ranges[0]
elif 3 < length_clothes < 7:
    wash_time = time_ranges[1]
else:
    wash_time = time_ranges[2]

print(f"{mode_name} mode will take {time_ranges[0]}-{time_ranges[2]} minutes to wash your clothes.")
time.sleep(2)
print(f"It will take {wash_time} minutes. Starting now...")
time.sleep(2)

washing_messages(wash_time)
