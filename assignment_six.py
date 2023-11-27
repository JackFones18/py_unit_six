import random

def get_birthdays():
    """Generate a list of 23 random numbers representing birthdays."""
    return [random.randint(1, 365) for _ in range(23)]

def is_duplicates(birthdays):
    """Check if there are duplicate birthdays in the given list."""
    for x in range(len(birthdays)):
        for y in range(x + 1, len(birthdays)):
            if birthdays[x] == birthdays[y]:
                return True
    return False

def main():
    """Run the birthday simulation and calculate the percentage of times with duplicates."""
    duplicate_count = 0

    try:
        simulation_count = int(input("How many times would you like to simulate this problem? "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    for z in range(simulation_count):
        birthdays = get_birthdays()
        if is_duplicates(birthdays):
            duplicate_count += 1

    percentage = round((duplicate_count / simulation_count) * 100,2)
    print(duplicate_count,"times there were two of the same birthday.")
    print(f"This is about",percentage,"percent of the time.")

if __name__ == "__main__":
    main()
