import re

def check_password_strength(password):
    feedback = []

    if len(password) < 8:
        feedback.append("❌ Password must be at least 8 characters long.")

    if not re.search(r"[A-Z]", password):
        feedback.append("❌ Password must contain at least one uppercase letter.")

    if not re.search(r"[a-z]", password):
        feedback.append("❌ Password must contain at least one lowercase letter.")

    if not re.search(r"\d", password):
        feedback.append("❌ Password must contain at least one number.")

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        feedback.append("❌ Password must contain at least one special character.")

    if " " in password:
        feedback.append("❌ Password must not contain spaces.")

    if feedback:
        print("\nPassword Strength: Weak ❌")
        print("\nSuggestions:")
        for item in feedback:
            print(item)
    else:
        print("\nPassword Strength: Strong ✅")
        print("Your password meets all recommended security requirements.")

def main():
    print("=" * 45)
    print("        Password Strength Checker")
    print("=" * 45)

    password = input("Enter your password: ")

    check_password_strength(password)

if __name__ == "__main__":
    main()
