import re

def parse_iso15022_sender_receiver_lines(lines):
    parsed_blocks = []
    current_code = None
    current_block = ""

    for line in lines:
        match = re.match(r"^(/[^/]+/)(.*)", line.strip())
        if match:
            if current_code:
                parsed_blocks.append((current_code, current_block.strip()))
            current_code = match.group(1)
            current_block = match.group(2).strip() + " "
        else:
            current_block += line.strip() + " "

    if current_code:
        parsed_blocks.append((current_code, current_block.strip()))

    return parsed_blocks

def validate_iso15022_sender_receiver_lines(blocks, max_length=140):
    errors = []

    for code, value in blocks:
        full_text = f"{code}{value}"
        if len(full_text) > max_length:
            errors.append({
                "code": code,
                "value": full_text,
                "length": len(full_text),
                "error": "Exceeds 140 character limit"
            })

    return errors

# Example input
input_lines = [
    "/BNF/John Doe",
    "123 Street Name,",
    "Melbourne VIC, Australia. This address continues for a while just to simulate a long address field that may exceed character limits.",
    "/INS/ABC Bank",
    "456 Bank Road",
    "Sydney NSW"
]

# Run
parsed = parse_iso15022_sender_receiver_lines(input_lines)
validation_errors = validate_iso15022_sender_receiver_lines(parsed)

# Output
if validation_errors:
    print("❌ Validation Errors:")
    for err in validation_errors:
        print(f"{err['code']} ({err['length']} chars): {err['value']}")
else:
    print("✅ All lines are within the 140 character limit.")


# Example dictionary
data = {
    "key1": "short text",
    "key2": "x" * 150,
    "key3": "y" * 80,
    "key4": "z" * 200
}

# Filter key-value pairs where value length > 140
filtered = {k: v for k, v in data.items() if len(v) > 140}

print(filtered)
