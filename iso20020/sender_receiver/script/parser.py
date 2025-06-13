import re

def parse_iso15022_lines(lines):
    parsed_blocks = []
    current_code = None
    current_block = ""

    for line in lines:
        match = re.match(r"^(/[^/]+/)(.*)", line.strip())
        if match:
            # New code segment found
            if current_code:
                # Save the previous one
                final_block = f"{current_code}{current_block.strip()}"
                parsed_blocks.append(final_block)
            current_code = match.group(1)  # e.g., "/BNF/"
            current_block = match.group(2).strip() + " "
        else:
            # Continuation line
            current_block += line.strip() + " "

    if current_code:
        final_block = f"{current_code}{current_block.strip()}"
        parsed_blocks.append(final_block)

    return parsed_blocks

def validate_blocks(blocks, max_length=140):
    errors = []
    for i, block in enumerate(blocks):
        if len(block) > max_length:
            errors.append({
                "index": i,
                "block": block,
                "length": len(block),
                "error": "Exceeds 140 character limit"
            })
    return errors

# Example usage
input_lines = [
    "/BNF/John Doe",
    "123 Street Name,",
    "Melbourne VIC",
    "/INS/ABC Bank",
    "456 Bank Road",
    "Sydney NSW"
]

parsed = parse_iso15022_lines(input_lines)
errors = validate_blocks(parsed)

print("Parsed Blocks:")
for p in parsed:
    print(p)

if errors:
    print("\nValidation Errors:")
    for e in errors:
        print(e)
else:
    print("\nAll blocks are within the 140 character limit.")
