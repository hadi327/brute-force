import itertools
import string
import time

# Character sets
lower = string.ascii_lowercase
upper = string.ascii_uppercase
digits = string.digits
symbols = "!@#$%^&*"
r=time
q=itertools

def estimate_search_space(password_length, charset_size):
    return charset_size ** password_length

def estimate_time(search_space, guesses_per_second):
    seconds = search_space / guesses_per_second
    return seconds

def format_time(seconds):
    if seconds < 1:
        return "less than 1 second"
    elif seconds < 60:
        return f"{seconds:.2f} seconds"
    elif seconds < 3600:
        return f"{seconds/60:.2f} minutes"
    elif seconds < 86400:
        return f"{seconds/3600:.2f} hours"
    elif seconds < 31536000:
        return f"{seconds/86400:.2f} days"
    else:
        return f"{seconds/31536000:.2f} years"

def simulate(password):
    print("\n=== Brute Force Simulation ===")

    # Detect charset used
    charset = ""
    if any(c in lower for c in password):
        charset += lower
    if any(c in upper for c in password):
        charset += upper
    if any(c in digits for c in password):
        charset += digits
    if any(c in symbols for c in password):
        charset += symbols

    charset_size = len(set(charset))
    length = len(password)

    # Assume modern GPU guessing speed (safe approximation)
    guesses_per_second = 1e9  # 1 billion guesses/sec (theoretical)

    search_space = estimate_search_space(length, charset_size)
    time_needed = estimate_time(search_space, guesses_per_second)

    print(f"Password length: {length}")
    print(f"Charset size: {charset_size}")
    print(f"Total combinations: {search_space:e}")
    print(f"Estimated crack time: {format_time(time_needed)}")

    # Strength label
    if time_needed < 60:
        print("🔴 Very Weak")
    elif time_needed < 86400:
        print("🟠 Weak")
    elif time_needed < 31536000:
        print("🟡 Moderate")
    else:
        print("🟢 Strong / Very Strong")

if __name__ == "__main__":
    pwd = input("Enter a sample password (for simulation only): ")
    simulate(pwd)