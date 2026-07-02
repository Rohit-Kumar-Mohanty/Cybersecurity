import re
common_passwords = [
    "password", "123456", "123456789", "qwerty",
    "admin", "welcome", "abc123", "password123"
]
print("====================================")
print("     PASSWORD STRENGTH ANALYZER")
print("====================================")
password = input("Enter your password: ")
score = 0
suggestions = []
if len(password) >= 12:
    score += 2
elif len(password) >= 8:
    score += 1
else:
    suggestions.append("Increase password length to at least 8 characters.")
if re.search(r"[A-Z]", password):
    score += 1
else:
    suggestions.append("Add at least one uppercase letter.")
if re.search(r"[a-z]", password):
    score += 1
else:
    suggestions.append("Add at least one lowercase letter.")
if re.search(r"\d", password):
    score += 1
else:
    suggestions.append("Add at least one number.")
if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
    score += 1
else:
    suggestions.append("Add at least one special character.")
if password.lower() in common_passwords:
    print("\n❌ This is a very common password!")
    print("Please choose a different password.")
    score = 0
print("\n========== RESULT ==========")

if score <= 2:
    print("Password Strength : WEAK")
elif score <= 5:
    print("Password Strength : MEDIUM")
else:
    print("Password Strength : STRONG")

print("\nPassword Length :", len(password))

if suggestions:
    print("\nSuggestions to Improve:")
    for item in suggestions:
        print("-", item)
else:
    print("\nExcellent! Your password is secure.")

print("\n============================")
