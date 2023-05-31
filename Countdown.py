import time
import random
import os
import hashlib
from tqdm import tqdm

# Salt random generator with system information
def salted_random():
    system_info = f"{os.uname()}-{time.time()}"
    salt = hashlib.sha256(system_info.encode('utf-8')).hexdigest()
    random.seed(salt)

# Number generator function
def generate_number():
    salted_random()
    random_number = random.randint(1, 1000)
    return random_number

if __name__ == "__main__":
    timer_length = int(input("Enter the length of the timer in seconds: "))
    print("Starting the random number generator with built-in timer and salt...")

    # Display progress bar
    for _ in tqdm(range(timer_length), desc="Running timer"):
        time.sleep(1)

    random_number = generate_number()
    print(f"Generated number: {random_number}")
    print("Stopping the random number generator...")
