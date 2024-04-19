import random

def roll_die(number_of_rolls):
    # Roll a six-sided die with float numbers between 0 and 1
    rolls = [random.uniform(0, 1) for _ in range(number_of_rolls)]

    # Increment the frequency of each face based on the generated float numbers
    frequency = [0, 0, 0, 0, 0, 0]  # Initialize frequencies for faces 1 through 6

    for roll in rolls:
        if 0 <= roll <= 1/6:
            frequency[0] += 1  # Increment the frequency of face 1 by 1
        elif 1/6 < roll <= 2/6:
            frequency[1] += 1  # Increment the frequency of face 2 by 1
        elif 2/6 < roll <= 3/6:
            frequency[2] += 1  # Increment the frequency of face 3 by 1
        elif 3/6 < roll <= 4/6:
            frequency[3] += 1  # Increment the frequency of face 4 by 1
        elif 4/6 < roll <= 5/6:
            frequency[4] += 1  # Increment the frequency of face 5 by 1
        else:
            frequency[5] += 1  # Increment the frequency of face 6 by 1

    return frequency

def calculate_stats(rolls):
    # Calculate the percentage of each face
    total_rolls = sum(rolls)
    percentage = {face + 1: (count / total_rolls) * 100 for face, count in enumerate(rolls)}

    return rolls, percentage

def print_stats(rolls, percentage):
    print(f"Face   Frequency   Percentage")
    print("-" * 30)
    for face in range(1, 7):
        print(f"{face:4} {rolls[face - 1]:11} {percentage[face]:11.2f}%")

if __name__ == "__main__":
    # Number of times to roll the die
    num_rolls = 1000

    # Simulate die rolls
    rolls = roll_die(num_rolls)

    # Calculate and print statistics
    rolls, percentage = calculate_stats(rolls)
    print_stats(rolls, percentage)
