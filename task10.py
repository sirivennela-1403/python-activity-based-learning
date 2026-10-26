```python
# Campus Event Financial Planning

import math

print("=== Campus Event Financial Planning ===")

# Get fixed costs
venue_cost = float(input("Enter venue cost: Rs. "))
equipment_cost = float(input("Enter equipment cost: Rs. "))
transport_cost = float(input("Enter transport cost: Rs. "))

# Get variable costs
catering_cost = float(input("Enter catering cost per participant: Rs. "))
certificate_cost = float(input("Enter certificate cost per participant: Rs. "))

# Get planning details
participants = int(input("Enter expected number of participants: "))
sponsorship = float(input("Enter confirmed sponsorship amount: Rs. "))
registration_fee = float(input("Enter proposed registration fee: Rs. "))

# Validate inputs
if (
    venue_cost < 0
    or equipment_cost < 0
    or transport_cost < 0
    or catering_cost < 0
    or certificate_cost < 0
    or participants <= 0
    or sponsorship < 0
    or registration_fee < 0
):
    print("Error: Enter valid non-negative costs and positive participants.")

else:
    # Calculate costs
    fixed_cost = venue_cost + equipment_cost + transport_cost

    variable_cost = catering_cost + certificate_cost

    total_event_cost = (
        fixed_cost + variable_cost * participants
    )

    # Sponsorship analysis
    sponsorship_shortfall = max(
        0, total_event_cost - sponsorship
    )

    sponsorship_surplus = max(
        0, sponsorship - total_event_cost
    )

    # Required registration fee for expected attendance
    amount_per_participant = max(
        0, total_event_cost - sponsorship
    ) / participants

    required_fee = math.ceil(amount_per_participant)

    # Break-even analysis
    contribution_per_participant = (
        registration_fee - variable_cost
    )

    fixed_cost_after_sponsorship = max(
        0, fixed_cost - sponsorship
    )

    if sponsorship >= fixed_cost:
        break_even = 0

    elif contribution_per_participant <= 0:
        break_even = None

    else:
        break_even = math.ceil(
            fixed_cost_after_sponsorship
            / contribution_per_participant
        )

    # Financial summary
    print("\n--- Event Cost Summary ---")
    print(f"Fixed Cost              : Rs. {fixed_cost:.2f}")
    print(f"Variable Cost/Person    : Rs. {variable_cost:.2f}")
    print(f"Expected Participants   : {participants}")
    print(f"Total Event Cost        : Rs. {total_event_cost:.2f}")

    print("\n--- Sponsorship Analysis ---")
    print(f"Sponsorship Received    : Rs. {sponsorship:.2f}")
    print(f"Sponsorship Shortfall   : Rs. {sponsorship_shortfall:.2f}")
    print(f"Sponsorship Surplus     : Rs. {sponsorship_surplus:.2f}")

    print("\n--- Registration Analysis ---")
    print(f"Minimum Fee Required    : Rs. {required_fee}")
    print(f"Proposed Registration Fee: Rs. {registration_fee:.2f}")

    if break_even is None:
        print("Break-even Registrations: Not possible at this fee.")
    else:
        print(f"Break-even Registrations: {break_even}")

    # Check financial feasibility at expected attendance
    total_funding = (
        sponsorship + registration_fee * participants
    )

    balance = total_funding - total_event_cost

    print("\n--- Financial Feasibility ---")
    print(f"Total Funding           : Rs. {total_funding:.2f}")
    print(f"Financial Balance       : Rs. {balance:.2f}")

    if balance > 0:
        print("Status: Event generates a surplus.")
    elif balance == 0:
        print("Status: Event breaks even.")
    else:
        print("Status: Additional funding is required.")
```
