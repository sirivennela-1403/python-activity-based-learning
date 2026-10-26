```python
# Multi-Plan Telecommunications Cost Optimization

plans = [
    {
        "name": "Plan A",
        "price": 299,
        "data_per_day": 2,
        "validity": 28,
        "excess_rate": 10,
        "unlimited_calls": True
    },
    {
        "name": "Plan B",
        "price": 349,
        "data_per_day": 2.5,
        "validity": 28,
        "excess_rate": 8,
        "unlimited_calls": True
    },
    {
        "name": "Plan C",
        "price": 399,
        "data_per_day": 3,
        "validity": 28,
        "excess_rate": 5,
        "unlimited_calls": True
    },
    {
        "name": "Plan D",
        "price": 249,
        "data_per_day": 1,
        "validity": 24,
        "excess_rate": 12,
        "unlimited_calls": True
    }
]

# User requirements
required_data = 60
required_validity = 28
budget = 400
requires_unlimited_calls = True


def evaluate_plan(plan):
    # Calculate included data
    included_data = (
        plan["data_per_day"] * plan["validity"]
    )

    # Calculate excess usage and charges
    excess_data = max(
        0, required_data - included_data
    )

    excess_charge = (
        excess_data * plan["excess_rate"]
    )

    total_cost = plan["price"] + excess_charge

    # Check eligibility conditions
    eligible = (
        plan["validity"] >= required_validity
        and total_cost <= budget
        and included_data >= required_data
        and (
            not requires_unlimited_calls
            or plan["unlimited_calls"]
        )
    )

    return {
        "name": plan["name"],
        "base_price": plan["price"],
        "included_data": included_data,
        "excess_data": excess_data,
        "excess_charge": round(excess_charge, 2),
        "total_cost": round(total_cost, 2),
        "eligible": eligible
    }


# Evaluate all plans
results = [evaluate_plan(plan) for plan in plans]

print("MOBILE PLAN COMPARISON")
print("-" * 78)

for result in results:
    status = (
        "Eligible" if result["eligible"]
        else "Not Eligible"
    )

    print(
        f"{result['name']}: "
        f"Base Price = Rs.{result['base_price']}, "
        f"Included Data = {result['included_data']} GB, "
        f"Excess Data = {result['excess_data']} GB, "
        f"Excess Charge = Rs.{result['excess_charge']}, "
        f"Total Cost = Rs.{result['total_cost']}, "
        f"Status = {status}"
    )

# Find the lowest-cost eligible plan
eligible_plans = [
    result for result in results
    if result["eligible"]
]

print("-" * 78)

if eligible_plans:
    best_plan = min(
        eligible_plans,
        key=lambda plan: (
            plan["total_cost"],
            plan["base_price"],
            plan["name"]
        )
    )

    print("MOST ECONOMICAL ELIGIBLE PLAN")
    print("Plan Name:", best_plan["name"])
    print("Total Estimated Cost: Rs.", best_plan["total_cost"])
else:
    print("No plan satisfies all the requirements.")
```
