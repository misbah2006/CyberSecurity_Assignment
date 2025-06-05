
---

## 🐍 `brute_force_simulator.py`

```python
import itertools
import string
import time

def brute_force_attack(target_password, charset):
    print("\nTrying combinations...")
    attempt_count = 0
    start_time = time.time()

    for password_length in range(1, len(target_password) + 1):
        for attempt in itertools.product(charset, repeat=password_length):
            attempt_count += 1
            guess = ''.join(attempt)
            if guess == target_password:
                end_time = time.time()
                print("\nCracked! ✅")
                print(f"Password: {guess}")
                print(f"Attempts: {attempt_count}")
                print(f"Time taken: {round(end_time - start_time, 2)} seconds")
                return

    print("Failed to crack the password.")

if __name__ == "__main__":
    print("🔐 Brute Force Attack Simulator (Educational Use Only)")
    target_password = input("Enter the password to simulate brute-force: ")

    # You can modify charset based on use-case
    charset = string.ascii_letters + string.digits  # abc...XYZ0123

    brute_force_attack(target_password, charset)
