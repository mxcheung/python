Problem:
You want to parse a list of such lines, and when a line starts with a tag like /ACC/, /INS/, or /BNF/, treat it as a new field. 
If it doesn't, join it to the previous line.

Example Input:
```
lines = [
    "/BNF/FCC. Account",
    "nr. second line",
    "/ACC/1234567890",
    "Main branch"
]
```

Expected Output:
```
[
    "/BNF/FCC. Account nr. 396fco8",
    "/ACC/1234567890 Main branch"
]
```

```
def join_sri_fields(lines):
    tags = ('/ACC/', '/INS/', '/BNF/')
    result = []
    current = ""

    for line in lines:
        line = line.strip()
        if any(line.startswith(tag) for tag in tags):
            if current:
                result.append(current)
            current = line
        else:
            current += " " + line

    if current:
        result.append(current)

    return result

# Example usage:
lines = [
    "/BNF/FCC. Account",
    "nr. 396fco8",
    "/ACC/1234567890",
    "Main branch"
]

print(join_sri_fields(lines))
```
