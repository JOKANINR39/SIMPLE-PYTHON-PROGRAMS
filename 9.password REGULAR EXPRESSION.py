import re
# Function to validate password
def validate_password(password):
# Regular expression pattern to check the password conditions
# ^: start of the string
# (?=.*[A-Z]): at least one uppercase letter
# (?=.*[a-z]): at least one lowercase letter
# (?=.*\d): at least one digit
# (?=.*[!@#$%^&*()_+]): at least one special character
# .{8,}: the length should be at least 8 characters
pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*()_+]).{8,}$'
if re.match(pattern, password):
return True
else:
return False
# Sample passwords to test
passwords = [
"Password123!", # valid
"password", # invalid: no uppercase, no special character
"PASSWORD123!", # invalid: no lowercase letter
"Pass123", # invalid: too short
"P@ssw0rd!", # valid
"12345678", # invalid: no uppercase, no special character
]
# Check and validate each password
for password in passwords:
if validate_password(password):
print(f"'{password}' is a valid password.")
else:
print(f"'{password}' is an invalid password.")