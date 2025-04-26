import re

def check_password_strength(password):
    # Initialize strength score
    strength = 0

    # Check password length
    if len(password) >= 8:
        strength += 1

    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        strength += 1

    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        strength += 1

    # Check for numbers
    if re.search(r"[0-9]", password):
        strength += 1

    # Check for special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1

    # Evaluate strength based on score
    if strength <= 2:
        return "Weak"
    elif strength == 3 or strength == 4:
        return "Moderate"
    else:
        return "Strong"

def main():
    print("🔒 Password Strength Checker 🔒")
    password = input("Enter a password to check: ")
    strength = check_password_strength(password)
    print(f"Password Strength: {strength}")

if __name__ == "__main__":
    main()
