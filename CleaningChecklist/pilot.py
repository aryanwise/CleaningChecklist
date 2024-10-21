# Cleaning Checklist Prototype

# Basic checklist for Dust and Arrangements
dusting_checklist = ["Floor", "Bathroom", "Under the Bed", "Wooden Racks"]

arrangement_checklist = ["Bedsheets", "Pillows", "Blankets"]

# Checklist according to room size (Big or Small)
big_room_checklist = [
    ("Big Towels", 5),
    ("Hand Towels", 5),
    ("Foot Towel", 1),
    ("Bathroom Glasses", 4),
    ("Pillows", 5),
    ("Blankets", 5),
    ("Bed Sheets", 3),
]

small_room_checklist = [
    ("Big Towels", 2),
    ("Hand Towels", 2),
    ("Foot Towel", 1),
    ("Bathroom Glasses", 2),
    ("Pillows", 2),
    ("Blankets", 2),
    ("Bed Sheet", 1),
]


# Function to check if the task is completed (for yes/no tasks)
def check_task(task):
    response = str(input(f"Is '{task}' done? (yes/no): ")).strip().lower()
    return response == "yes" or response == "y"


# Function to check the quantity of items and return how many are missing
def check_quantity_task(task, required_quantity):
    available_quantity = int(
        input(f"How many '{task}' are present? (Required: {required_quantity}): ")
    )
    if available_quantity < required_quantity:
        missing = required_quantity - available_quantity
        return missing
    return 0


# Asking for the cleaner's name and their assigned room numbers
name = str(input("Enter name of the cleaner: "))
list_room_number = []
room_info = {}  # To store room number and room size (big/small)
max_room_number = int(input("Room number limit: "))

for _ in range(max_room_number):
    room_number = int(input(f"Enter room number: "))
    room_size = (
        str(input(f"Enter size of room {room_number} (big/small): ")).strip().lower()
    )
    list_room_number.append(room_number)
    room_info[room_number] = room_size

# Dictionary to store unchecked tasks for each room
unchecked_tasks_per_room = {}

# Go through each room, ask for the size and display corresponding checklist
for room_number in list_room_number:
    print(f"\nChecking tasks for room {room_number} ({room_info[room_number]} room):")
    unchecked_tasks = []  # Initialize list to store unchecked tasks for this room

    # Dusting tasks
    print("\nDusting Checklist:")
    for task in dusting_checklist:
        if not check_task(f"dusting {task}"):
            unchecked_tasks.append(f"Dusting - {task} not completed")

    # Arrangement tasks
    print("\nArrangement Checklist:")
    for task in arrangement_checklist:
        if not check_task(f"arranging {task}"):
            unchecked_tasks.append(f"Arrangement - {task} not completed")

    # Room-specific tasks (big/small room checklist)
    print("\nRoom Specific Checklist:")
    if room_info[room_number] == "big":
        checklist = big_room_checklist
    elif room_info[room_number] == "small":
        checklist = small_room_checklist
    else:
        print("Invalid room size! Skipping this room.")
        continue

    # Check each task in the room checklist
    for task, required_quantity in checklist:
        if required_quantity > 1:  # If the task requires multiple items (like towels)
            missing = check_quantity_task(task, required_quantity)
            if missing > 0:
                unchecked_tasks.append(f"{task} - {missing} required")
        else:
            if not check_task(task):  # If it's a simple yes/no task
                unchecked_tasks.append(f"{task} - not completed")

    # If there are any unchecked tasks, store them in the dictionary
    if unchecked_tasks:
        unchecked_tasks_per_room[room_number] = unchecked_tasks

# Summary of unchecked tasks
print(f"\n{name} has completed checking {list_room_number}.")

if unchecked_tasks_per_room:
    print(f"\n{name} did not finish the following tasks in each room:")
    for room_number, tasks in unchecked_tasks_per_room.items():
        print(f"Room {room_number} ({room_info[room_number]} room):")
        for task in tasks:
            print(f"- {task}")
else:
    print(f"\n{name} has completed all tasks in all rooms!")
