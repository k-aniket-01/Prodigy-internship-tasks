import re
import zxcvbn

def is_password_valid(password):
    if len(password) < 8 or len(password) > 64:
        return False

    if re.search(r'[\s]', password):
        return False

    strength = zxcvbn(password)['score']
    if strength < 3:
        return False

    return True

def assess_password_strength(password):
    if not is_password_valid(password):
        return "Invalid password. Please ensure it meets the criteria."

    strength = zxcvbn(password)['score']
    if strength == 0:
        return "Very weak password. Please make it stronger."
    elif strength == 1:
        return "Weak password. Improve it for better security."
    elif strength == 2:
        return "Moderate password. You can make it stronger."
    elif strength == 3:
        return "Strong password. Well done!"
    else:
        return "Unrecognized strength. Please try another password."

test_passwords = [
    "Password1",
    "123456",
    "SecurePassword123",
    "ThisIsASecureP@ssw0rd",
    "password",
    " "
]

for password in test_passwords:
    print(f"Password: {password}\nStrength: {assess_password_strength(password)}\n")