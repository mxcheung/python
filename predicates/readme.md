For validation logic, you should generally use predicates — not raw if-else blocks — because predicates make your code more modular, reusable, and testable.


Why Predicates Are Better for Validation
```
| Reason                       | Explanation                                                                                     |
| ---------------------------- | ----------------------------------------------------------------------------------------------- |
| ✅ **Reusability**            | Predicates can be reused across multiple parts of your app (e.g., form validation, API checks). |
| ✅ **Testability**            | Easy to write unit tests for small, focused predicate functions.                                |
| ✅ **Separation of concerns** | Keeps validation logic separate from control flow (like user interaction or logging).           |
| ✅ **Composability**          | You can combine multiple predicates for more complex rules.                                     |

```

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
