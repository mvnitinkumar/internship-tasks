import re

def assess_password_strength(password):
    # Initialize strength variables
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    number_criteria = bool(re.search(r'\d', password))
    special_char_criteria = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    # Count met criteria
    met_criteria = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_char_criteria])

    # Assess strength based on criteria
    if met_criteria == 5:
        strength = "Strong"
    elif met_criteria >= 3:
        strength = "Moderate"
    else:
        strength = "Weak"

    # Provide feedback to the user
    feedback = []
    if not length_criteria:
        feedback.append("Increase the length to at least 8 characters.")
    if not uppercase_criteria:
        feedback.append("Add at least one uppercase letter.")
    if not lowercase_criteria:
        feedback.append("Add at least one lowercase letter.")
    if not number_criteria:
        feedback.append("Include at least one numeric character.")
    if not special_char_criteria:
        feedback.append("Use at least one special character (e.g., !, @, #, etc.).")

    return strength, feedback

# Main program
if __name__ == "__main__":
    print("Password Strength Checker")
    password = input("Enter a password to assess: ")

    strength, feedback = assess_password_strength(password)

    print(f"Password Strength: {strength}")
    if feedback:
        print("Feedback to improve your password:")
        for suggestion in feedback:
            print(f"- {suggestion}")
