import re
import random
import string
from datetime import datetime

def check_password_strength(password):
    feedback = []
    strength = 0

    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("- Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("- Add at least one uppercase letter (A-Z).")

    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("- Add at least one lowercase letter (a-z).")

    if re.search(r"[0-9]", password):
        strength += 1
    else:
        feedback.append("- Include at least one number (0-9).")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        feedback.append("- Add at least one special character (!@#$%^&* etc.).")

    if strength <= 2:
        rating = "Weak"
    elif strength == 3 or strength == 4:
        rating = "Moderate"
    else:
        rating = "Strong"

    return rating, feedback

def generate_strong_password(length=16):
    if length < 8:
        length = 8
    characters = string.ascii_letters + string.digits + "!@#$%^&*()_+-=[]{}|;:,.<>?"
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def save_password_to_file(service_name, password):
    with open("saved_passwords.txt", "a") as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}] {service_name}: {password}\n")
    print("✅ Password saved to 'saved_passwords.txt' successfully!\n")

def main():
    print("🔒 Password Strength Checker, Generator & Saver 🔒")
    print("\n1. Check your own password strength")
    print("2. Generate a random strong password and save it\n")
    
    choice = input("Choose an option (1 or 2): ").strip()

    if choice == '1':
        password = input("\nEnter a password to check: ")
        rating, feedback = check_password_strength(password)

        print(f"\nPassword Strength: {rating}\n")
        if feedback:
            print("Suggestions to improve your password:")
            for suggestion in feedback:
                print(suggestion)
    elif choice == '2':
        service = input("\nEnter the name of the website/app this password is for (e.g., Gmail, Facebook): ").strip()
        length = input("Enter desired password length (minimum 8, default 16): ").strip()
        if not length.isdigit() or int(length) < 8:
            length = 16
        else:
            length = int(length)

        password = generate_strong_password(length)
        print(f"\nGenerated Strong Password for {service}: {password}")
        save_password_to_file(service, password)
    else:
        print("\n❌ Invalid choice. Please select option 1 or 2.")

if __name__ == "__main__":
    main()
