```python
# Progressive Electricity Billing System

FIXED_CHARGE = 50
SURCHARGE_RATE = 0.05
REBATE_RATE = 0.10
INCREASE_THRESHOLD = 20  # Percentage

monthly_data = [
    {"month": "January", "units": 150},
    {"month": "February", "units": 170},
    {"month": "March", "units": 260},
    {"month": "April", "units": 280}
]


def calculate_bill(units):
    # Progressive slab calculation
    if units < 0:
        raise ValueError("Units cannot be negative.")

    energy_charge = 0

    first_slab = min(units, 100)
    energy_charge += first_slab * 2

    second_slab = min(max(units - 100, 0), 100)
    energy_charge += second_slab * 3

    third_slab = max(units - 200, 0)
    energy_charge += third_slab * 5

    subtotal = energy_charge + FIXED_CHARGE

    surcharge = subtotal * SURCHARGE_RATE
    amount_before_rebate = subtotal + surcharge

    rebate = amount_before_rebate * REBATE_RATE

    final_bill = amount_before_rebate - rebate

    return round(final_bill, 2)


# Calculate bills
for record in monthly_data:
    record["bill"] = calculate_bill(record["units"])

# Display monthly report
print("PROGRESSIVE ELECTRICITY BILLING REPORT")
print("-" * 65)

for i, record in enumerate(monthly_data):
    print(
        f"{record['month']:10} | "
        f"Units: {record['units']:3} | "
        f"Bill: Rs. {record['bill']:.2f}"
    )

    # Compare with the previous month
    if i > 0:
        previous = monthly_data[i - 1]
        current = record

        previous_bill = previous["bill"]
        current_bill = current["bill"]

        previous_units = previous["units"]
        current_units = current["units"]

        if previous_bill > 0:
            bill_change = (
                (current_bill - previous_bill)
                / previous_bill
            ) * 100
        else:
            bill_change = 0

        if previous_units > 0:
            unit_change = (
                (current_units - previous_units)
                / previous_units
            ) * 100
        else:
            unit_change = 0

        print(f"  Bill change: {bill_change:.2f}%")
        print(f"  Usage change: {unit_change:.2f}%")

        if bill_change > INCREASE_THRESHOLD:
            print("  ALERT: Unusual increase in electricity bill!")

        if unit_change > INCREASE_THRESHOLD:
            print("  ALERT: Unusual increase in electricity usage!")

    print("-" * 65)
```
