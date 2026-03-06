# tax_calculator.py
# Part B: Indian Income Tax Calculator - New Regime FY 2024-25

def calculate_tax(annual_income):
    STANDARD_DEDUCTION = 75000

    # apply standard deduction
    taxable_income = max(0, annual_income - STANDARD_DEDUCTION)

    # tax slabs for new regime FY 2024-25
    slabs = [
        (300000,  0.00, "0 – 3L"),
        (400000,  0.05, "3L – 7L"),
        (300000,  0.10, "7L – 10L"),
        (200000,  0.15, "10L – 12L"),
        (300000,  0.20, "12L – 15L"),
        (float('inf'), 0.30, "Above 15L"),
    ]

    total_tax = 0
    breakdown = []
    remaining = taxable_income
    slab_start = 0

    for slab_size, rate, label in slabs:
        if remaining <= 0:
            break

        income_in_slab = min(remaining, slab_size)
        tax_in_slab = income_in_slab * rate

        breakdown.append({
            'slab': label,
            'income_in_slab': income_in_slab,
            'rate': rate * 100,
            'tax': tax_in_slab
        })

        total_tax += tax_in_slab
        remaining -= income_in_slab

    effective_rate = (total_tax / annual_income * 100) if annual_income > 0 else 0

    return taxable_income, breakdown, total_tax, effective_rate


def main():
    print("===== Indian Income Tax Calculator (New Regime FY 2024-25) =====\n")

    while True:
        try:
            income_str = input("Enter your annual income (in Rs): ").replace(',', '')
            annual_income = float(income_str)
            if annual_income < 0:
                print("Income cannot be negative.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    taxable_income, breakdown, total_tax, effective_rate = calculate_tax(annual_income)

    print(f"\n--- Tax Calculation Breakdown ---")
    print(f"Gross Income        : Rs {annual_income:,.2f}")
    print(f"Standard Deduction  : Rs 75,000.00")
    print(f"Taxable Income      : Rs {taxable_income:,.2f}")
    print(f"\n{'Slab':<15} {'Income in Slab':>18} {'Rate':>8} {'Tax':>15}")
    print("-" * 60)

    for entry in breakdown:
        if entry['income_in_slab'] > 0:
            print(f"{entry['slab']:<15} Rs {entry['income_in_slab']:>14,.2f} {entry['rate']:>6.0f}%  Rs {entry['tax']:>12,.2f}")

    print("-" * 60)
    print(f"{'Total Tax':<15} {'':>18} {'':>8}  Rs {total_tax:>12,.2f}")
    print(f"\nEffective Tax Rate  : {effective_rate:.2f}%")

main()
