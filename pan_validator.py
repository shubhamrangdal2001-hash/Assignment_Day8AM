# pan_validator.py
# Part D: PAN Card Number Format Validator (Improved Version)

# PAN Format: 5 uppercase letters, 4 digits, 1 uppercase letter
# 4th character indicates type of taxpayer:
#   P = Individual, C = Company, H = HUF, F = Firm,
#   A = AOP, B = BOI, G = Govt, J = Artificial Juridical Person, L = Local Authority

TAXPAYER_TYPES = {
    'P': 'Individual',
    'C': 'Company',
    'H': 'Hindu Undivided Family (HUF)',
    'F': 'Firm',
    'A': 'Association of Persons (AOP)',
    'B': 'Body of Individuals (BOI)',
    'G': 'Government',
    'J': 'Artificial Juridical Person',
    'L': 'Local Authority'
}

def validate_pan(pan):
    # check length first
    if len(pan) != 10:
        return False, f"Invalid length: PAN must be exactly 10 characters, got {len(pan)}"

    # first 3 characters must be uppercase letters
    if not pan[:3].isalpha() or not pan[:3].isupper():
        return False, "First 3 characters must be uppercase letters (A-Z)"

    # 4th character: taxpayer type - must be uppercase letter from valid set
    taxpayer_char = pan[3]
    if not taxpayer_char.isalpha() or not taxpayer_char.isupper():
        return False, "4th character must be an uppercase letter indicating taxpayer type"

    if taxpayer_char not in TAXPAYER_TYPES:
        return False, f"4th character '{taxpayer_char}' is not a valid taxpayer type code"

    # 5th character must be an uppercase letter
    if not pan[4].isalpha() or not pan[4].isupper():
        return False, "5th character must be an uppercase letter"

    # characters 6 to 9 (index 5-8) must be digits
    if not pan[5:9].isdigit():
        return False, "Characters 6-9 must be digits (0-9)"

    # last character (10th) must be an uppercase letter
    if not pan[9].isalpha() or not pan[9].isupper():
        return False, "Last character (10th) must be an uppercase letter"

    taxpayer_type = TAXPAYER_TYPES[taxpayer_char]
    return True, f"Valid PAN. Taxpayer type: {taxpayer_type}"


def main():
    print("===== PAN Card Validator =====\n")

    # test cases
    test_pans = [
        "ABCDE1234F",   # valid individual
        "AAAPC1234C",   # valid company
        "abcde1234f",   # lowercase - invalid
        "ABCDE123F",    # too short
        "ABCDE12345F",  # too long
        "ABC1E1234F",   # digit at 4th position
        "ABCXE1234F",   # invalid taxpayer type at 4th char
        "ABCDE123AF",   # letter where digit expected
        "ABCPE123AF",   # letter in digit section
        "",             # empty string
    ]

    for pan in test_pans:
        is_valid, message = validate_pan(pan)
        status = "VALID" if is_valid else "INVALID"
        print(f"PAN: '{pan:<12}' => {status} | {message}")

    print("\n--- Manual Input ---")
    user_pan = input("Enter a PAN number to validate: ").strip().upper()
    is_valid, message = validate_pan(user_pan)
    status = "VALID" if is_valid else "INVALID"
    print(f"Result: {status} | {message}")

main()
