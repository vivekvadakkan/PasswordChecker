import re  # Regular Expressions Library

# Display strong password tips
def show_password_tips():
    print("### Strongest Password Tips ###")
    print("- The longer your password, the harder it is to break—aim for 16 characters or more.")
    print("- Mix uppercase, lowercase, numbers, and symbols to make your password tougher to crack.")
    print("- Avoid personal details or predictable patterns.")
    print("- A passphrase like 'BlueDog7!JumpsHigh' is both strong and easy to remember.")
    print("- Use a unique password for each account to maximize security.")
    print("- Enable two-factor authentication (2FA) for added protection.")
    print("- Consider a password manager to generate and store secure passwords.")
    print("\n")

# Password strength checker
def check_password_strength(password):
    suggestions = []  # List to hold suggestions for improvement

    # Check length
    if len(password) < 16:
        suggestions.append("The longer your password, the harder it is to break—aim for 16 characters or more.")

    # Check for uppercase letter
    if not re.search("[A-Z]", password):
        suggestions.append("Mix uppercase letters with lowercase letters to make your password tougher to crack.")

    # Check for lowercase letter
    if not re.search("[a-z]", password):
        suggestions.append("Include lowercase letters for added complexity.")

    # Check for numbers
    if not re.search("[0-9]", password):
        suggestions.append("Adding numbers makes your password more unpredictable.")

    # Check for special characters
    if not re.search("[@#$%^&*!]", password):
        suggestions.append("Symbols like '@', '#', and '!' make your password more secure.")

    # Check for personal details and patterns
    if re.search(r"(\d{4}|\bpassword\b|\b1234\b)", password, re.IGNORECASE):
        suggestions.append("Avoid personal details (e.g., your birth year) and predictable patterns.")

    # Response based on suggestions
    if suggestions:
        print("\nWeak Password! Here are some suggestions to make it stronger:")
        for suggestion in suggestions:
            print(f"- {suggestion}")
        return "Try again with a stronger password."
    else:
        print("\nStrong Password!")
        return "Your password is highly secure. Well done!"

# Main function
def main():
    # Show password tips
    show_password_tips()
    
    # Ask user for input
    user_password = input("Enter a password to check: ")
    print(check_password_strength(user_password))

# Run the program
if __name__ == "__main__":
    main()