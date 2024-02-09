import random

def guess(x):
    random_number = random.randint(1, x)
    low = 1
    high = x

    while low <= high:
        guess = (low + high) // 2  # Efficiently calculate the middle guess
        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)?: ").lower()
        if feedback == 'c':
            print(f"Yay, congrats. You have guessed the number {random_number} correctly!!")
            return
        elif feedback == 'h':
            high = guess - 1
        else:
            low = guess + 1

    print("Incorrect feedback. Could not guess the number.")

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # could also be high b/c low = high
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'Yay! The computer guessed your number, {guess}, correctly!')


guess(10)
