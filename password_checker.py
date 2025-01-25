def check_password_strength(password):
    if len(password) < 8:
        return "Password must be at least 8 characters."

    has_upper =has_lower=has_digit =  has_special =False
     

    for char in password:
        if char.isupper():
            has_upper = True
        if char.islower():
            has_lower = True
        if char.isdigit():
            has_digit = True
        if not char.isalnum():
            has_special = True

    if has_upper and has_lower and has_digit and has_special:
        return "Your password is strong!"
    else:
        return "Password must include uppercase, lowercase, digits, and special characters."


password = input("Enter your password: ")
result = check_password_strength(password)
print(result)
