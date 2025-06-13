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

def validate_blocks(blocks, max_length=140):
    valid = []
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
        else:
            valid.append(full_text)

    return valid, errors

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
valid_blocks, validation_errors = validate_blocks(parsed)

# Output
print("✅ Valid Blocks:")
for vb in valid_blocks:
    print(vb)

print("\n❌ Validation Errors:")
for
