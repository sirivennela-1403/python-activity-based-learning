```python
# Employee Payroll and Deduction Analysis System

def calculate_progressive_deduction(gross_salary):
    deduction = 0

    # First slab: 0% on the first Rs. 20,000
    first_slab = min(gross_salary, 20000)
    deduction += first_slab * 0.00

    # Second slab: 5% on the next Rs. 15,000
    second_slab = min(max(gross_salary - 20000, 0), 15000)
    deduction += second_slab * 0.05

    # Third slab: 10% on amounts above Rs. 35,000
    third_slab = max(gross_salary - 35000, 0)
    deduction += third_slab * 0.10

    return round(deduction, 2)


def generate_salary_statement(employee):
    # Validate employee information
    if not employee["employee_id"].strip():
        raise ValueError("Employee ID is required.")

    if not employee["name"].strip():
        raise ValueError("Employee name is required.")

    salary_components = [
        employee["basic_pay"],
        employee["allowances"],
        employee["overtime"],
        employee["incentives"]
    ]

    # Validate salary inputs
    for amount in salary_components:
        if (
            isinstance(amount, bool)
            or not isinstance(amount, (int, float))
            or amount < 0
        ):
            raise ValueError(
                "Salary components must be non-negative numbers."
            )

    # Calculate gross salary
    gross_salary = sum(salary_components)

    # Calculate deductions
    total_deductions = calculate_progressive_deduction(
        gross_salary
    )

    # Calculate net salary
    net_salary = gross_salary - total_deductions

    return {
        "gross_salary": round(gross_salary, 2),
        "deductions": total_deductions,
        "net_salary": round(net_salary, 2)
    }


# Sample employee information
employee = {
    "employee_id": "E101",
    "name": "Ravi",
    "basic_pay": 30000,
    "allowances": 8000,
    "overtime": 2000,
    "incentives": 3000
}

try:
    salary = generate_salary_statement(employee)

    print("=" * 45)
    print("         EMPLOYEE SALARY STATEMENT")
    print("=" * 45)

    print(f"Employee ID       : {employee['employee_id']}")
    print(f"Employee Name     : {employee['name']}")
    print("-" * 45)

    print(f"Basic Pay         : Rs. {employee['basic_pay']:.2f}")
    print(f"Allowances        : Rs. {employee['allowances']:.2f}")
    print(f"Overtime Pay      : Rs. {employee['overtime']:.2f}")
    print(f"Incentives        : Rs. {employee['incentives']:.2f}")

    print("-" * 45)
    print(f"Gross Salary      : Rs. {salary['gross_salary']:.2f}")
    print(f"Total Deductions  : Rs. {salary['deductions']:.2f}")
    print(f"Net Salary        : Rs. {salary['net_salary']:.2f}")
    print("=" * 45)

except ValueError as error:
    print("Payroll Error:", error)
```
