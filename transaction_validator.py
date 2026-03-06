# transaction_validator.py
# Part E: Smart Transaction Validator - Fraud Detection Rule Engine

def validate_transaction(amount, category, hour, daily_spent, is_vip=False):
    # VIP flag doubles all limits using ternary operator
    vip_multiplier = 2 if is_vip else 1

    single_limit   = 50000  * vip_multiplier
    daily_limit    = 100000 * vip_multiplier

    category_limits = {
        'food':        5000  * vip_multiplier,
        'electronics': 30000 * vip_multiplier,
        'travel':      None,   # no specific cap mentioned
        'other':       None
    }

    # --- BLOCKING RULES (override everything) ---
    if amount > single_limit:
        return "BLOCKED", f"Exceeds single transaction limit of Rs {single_limit:,.0f}"

    if daily_spent + amount > daily_limit:
        return "BLOCKED", f"Would exceed daily spending limit of Rs {daily_limit:,.0f} (already spent Rs {daily_spent:,.0f})"

    # --- FLAGGING RULES ---
    flag_reasons = []

    # unusual hours check
    if hour < 6 or hour >= 23:
        flag_reasons.append(f"Unusual transaction hour ({hour}:00)")

    # category-specific limits
    if category in category_limits and category_limits[category] is not None:
        cat_limit = category_limits[category]
        if amount >= cat_limit:
            flag_reasons.append(f"{category.capitalize()} transaction exceeds category limit of Rs {cat_limit:,.0f}")

    if flag_reasons:
        return "FLAGGED", "; ".join(flag_reasons)

    return "APPROVED", "Transaction meets all criteria"


def get_inputs():
    print("\n===== Smart Transaction Validator =====\n")

    while True:
        try:
            amount = float(input("Transaction amount (Rs): "))
            if amount <= 0:
                print("Amount must be positive.")
                continue
            break
        except ValueError:
            print("Enter a valid number.")

    while True:
        category = input("Category (food/travel/electronics/other): ").strip().lower()
        if category in ['food', 'travel', 'electronics', 'other']:
            break
        print("Invalid category. Choose from: food, travel, electronics, other")

    while True:
        try:
            hour = int(input("Hour of transaction (0-23): "))
            if 0 <= hour <= 23:
                break
            print("Hour must be between 0 and 23.")
        except ValueError:
            print("Enter a valid integer.")

    while True:
        try:
            daily_spent = float(input("Amount already spent today (Rs): "))
            if daily_spent < 0:
                print("Daily spent cannot be negative.")
                continue
            break
        except ValueError:
            print("Enter a valid number.")

    while True:
        vip_input = input("Is this a VIP account? (yes/no): ").strip().lower()
        if vip_input in ['yes', 'no']:
            is_vip = vip_input == 'yes'
            break
        print("Enter yes or no.")

    return amount, category, hour, daily_spent, is_vip


def main():
    amount, category, hour, daily_spent, is_vip = get_inputs()

    status, reason = validate_transaction(amount, category, hour, daily_spent, is_vip)

    print(f"\nTransaction: Rs{amount:,.2f} at {category} shop at {hour:02d}:00")
    if is_vip:
        print("Account Type: VIP (limits doubled)")
    print(f"Result: {status}: {reason}")


# --- Demo runs without user input ---
if __name__ == "__main__":
    print("===== Demo Test Cases =====\n")

    demo_cases = [
        (3000,  'food',        14, 0,     False, "Rs 3000 food at 14:00"),
        (60000, 'electronics',  2, 0,     False, "Rs 60000 electronics at 02:00"),
        (4500,  'food',         7, 0,     False, "Rs 4500 food - under food limit"),
        (5500,  'food',        10, 0,     False, "Rs 5500 food - over food limit"),
        (5500,  'food',        10, 0,     True,  "Rs 5500 food - VIP account"),
        (2000,  'travel',       2, 0,     False, "Rs 2000 travel at 02:00 - odd hour"),
        (1000,  'other',       15, 99500, False, "Rs 1000 - would exceed daily limit"),
    ]

    for amount, cat, hour, daily, vip, desc in demo_cases:
        status, reason = validate_transaction(amount, cat, hour, daily, vip)
        print(f"Case : {desc}")
        print(f"Result: {status} | {reason}\n")
