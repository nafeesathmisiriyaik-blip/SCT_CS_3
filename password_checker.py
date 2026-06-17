import string

while True:
    print("\n===== Password Strength Checker =====")

    password = input("Enter your password: ")

    score = 0
    suggestions = []

    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters")

    # Uppercase Check
    if any(char.isupper() for char in password):
        score += 1
    else:
        suggestions.append("Add an uppercase letter")

    # Lowercase Check
    if any(char.islower() for char in password):
        score += 1
    else:
        suggestions.append("Add a lowercase letter")

    # Number Check
    if any(char.isdigit() for char in password):
        score += 1
    else:
        suggestions.append("Add a number")

    # Special Character Check
    if any(char in string.punctuation for char in password):
        score += 1
    else:
        suggestions.append("Add a special character")

    # Strength Rating
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    print("\nPassword Strength:", strength)

    if suggestions:
        print("\nSuggestions:")
        for item in suggestions:
            print("-", item)

    choice = input("\nDo you want to check another password? (yes/no): ").lower()

    if choice != "yes":
        print("Thank you for using Password Strength Checker.")
        break