

 Example: Validation Using Predicate
```
def is_valid_email(email):
    return "@" in email and "." in email

def is_strong_password(pwd):
    return len(pwd) >= 8 and any(char.isdigit() for char in pwd)

email = "user@example.com"
password = "pass1234"

if is_valid_email(email) and is_strong_password(password):
    print("Valid input")
else:
    print("Invalid input")

```

If-Else Inside Validation (Not Ideal)


```
# Less reusable
def validate_user(email, pwd):
    if "@" not in email or "." not in email:
        return False
    if len(pwd) < 8 or not any(char.isdigit() for char in pwd):
        return False
    return True
```
This works, but it’s harder to reuse or test individual parts (email vs password logic).
