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
    required_suggestions = []  # Failures that make a password weak
    optional_tips = []         # Extra suggestions to improve already strong passwords

    # Required checks
    if len(password) < 8:
        required_suggestions.append("Your password should be at least 8 characters long.")
    if not re.search("[A-Z]", password):
        required_suggestions.append("Mix uppercase letters with lowercase letters to make your password tougher to crack.")
    if not re.search("[a-z]", password):
        required_suggestions.append("Include lowercase letters for added complexity.")
    if not re.search("[0-9]", password):
        required_suggestions.append("Adding numbers makes your password more unpredictable.")
    if not re.search("[@#$%^&*!]", password):
        required_suggestions.append("Symbols like '@', '#', and '!' make your password more secure.")
    if re.search(r"(\d{4}|\bpassword\b|\b1234\b)", password, re.IGNORECASE):
        required_suggestions.append("Avoid personal details (e.g., your birth year) and predictable patterns.")

    # Optional tip
    if len(password) >= 8 and len(password) < 16:
        optional_tips.append("Consider using 16 or more characters or use more special characters for even stronger protection.")

    # Output
    if required_suggestions:
        print("\nWeak Password! Here are some suggestions to make it stronger:")
        for suggestion in required_suggestions:
            print(f"- {suggestion}")
        return "Try again with a stronger password."
    else:
        print("\nStrong Password!")
        if optional_tips:
            print("Optional tips to make it even stronger:")
            for tip in optional_tips:
                print(f"- {tip}")
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