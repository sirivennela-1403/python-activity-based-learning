```python
# Manufacturing Cost and Profitability Analysis

print("=== Manufacturing Cost and Profitability Analysis ===")

# Get input values
units = int(input("Enter number of units produced: "))

if units <= 0:
    print("Error: Number of units must be greater than zero.")

else:
    material_cost = float(input("Enter material cost per unit: "))
    wastage_percent = float(input("Enter material wastage percentage: "))
    labour_cost = float(input("Enter labour cost per unit: "))
    machine_cost = float(input("Enter machine cost per unit: "))
    other_cost = float(input("Enter other cost per unit: "))
    selling_price = float(input("Enter selling price per unit: "))
    target_margin = float(input("Enter target profit margin (%): "))

    # Validate cost and percentage inputs
    if (
        material_cost < 0
        or not 0 <= wastage_percent <= 100
        or labour_cost < 0
        or machine_cost < 0
        or other_cost < 0
        or selling_price < 0
        or not 0 <= target_margin <= 100
    ):
        print("Error: Enter valid non-negative costs and percentages.")

    else:
        # Calculate wastage cost
        wastage_cost = material_cost * wastage_percent / 100

        # Calculate manufacturing cost per unit
        cost_per_unit = (
            material_cost
            + wastage_cost
            + labour_cost
            + machine_cost
            + other_cost
        )

        # Calculate batch costs and revenue
        total_production_cost = cost_per_unit * units
        total_revenue = selling_price * units

        # Calculate profit
        total_profit = total_revenue - total_production_cost
        profit_per_unit = selling_price - cost_per_unit

        # Calculate profit margin
        if total_revenue > 0:
            profit_margin = (total_profit / total_revenue) * 100
        else:
            profit_margin = None

        # Display results
        print("\n--- Manufacturing Cost Report ---")
        print(f"Number of Units       : {units}")
        print(f"Material Cost/Unit    : Rs. {material_cost:.2f}")
        print(f"Wastage Cost/Unit     : Rs. {wastage_cost:.2f}")
        print(f"Labour Cost/Unit      : Rs. {labour_cost:.2f}")
        print(f"Machine Cost/Unit     : Rs. {machine_cost:.2f}")
        print(f"Other Cost/Unit       : Rs. {other_cost:.2f}")
        print(f"Total Cost/Unit       : Rs. {cost_per_unit:.2f}")
        print(f"Total Production Cost : Rs. {total_production_cost:.2f}")
        print(f"Selling Price/Unit    : Rs. {selling_price:.2f}")
        print(f"Total Revenue         : Rs. {total_revenue:.2f}")
        print(f"Profit/Unit           : Rs. {profit_per_unit:.2f}")
        print(f"Total Profit          : Rs. {total_profit:.2f}")

        if profit_margin is not None:
            print(f"Profit Margin         : {profit_margin:.2f}%")
        else:
            print("Profit Margin         : Undefined (zero revenue)")

        # Check profitability target
        print("\n--- Profitability Decision ---")

        if total_profit < 0:
            print("Result: Production is running at a loss.")
        elif total_profit == 0:
            print("Result: Production is at the break-even point.")
        else:
            print("Result: Production is profitable.")

        if profit_margin is not None:
            if profit_margin >= target_margin:
                print("Target Status: TARGET ACHIEVED")
            else:
                print("Target Status: TARGET NOT ACHIEVED")
        else:
            print("Target Status: Cannot evaluate margin with zero revenue.")
```
