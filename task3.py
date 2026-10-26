```python
# Hospital Billing and Patient Classification System

def generate_bill(patient):
    # Validate patient ID
    if not patient["patient_id"]:
        raise ValueError("Patient ID is required.")

    # Validate charges
    charges = [
        patient["consultation"],
        patient["diagnostic"],
        patient["treatment"]
    ]

    if any(not isinstance(c, (int, float)) or isinstance(c, bool)
           or c < 0 for c in charges):
        raise ValueError("Charges must be non-negative numbers.")

    # Validate concession percentage
    concession_rate = patient["concession_rate"]

    if not isinstance(concession_rate, (int, float)) \
            or isinstance(concession_rate, bool) \
            or not 0 <= concession_rate <= 100:
        raise ValueError("Concession must be between 0 and 100.")

    # Calculate total charges
    subtotal = sum(charges)

    # Apply concession only to eligible patients
    if patient["eligible"]:
        concession = subtotal * concession_rate / 100
    else:
        concession = 0

    final_bill = subtotal - concession

    # Classify patient according to final bill
    if final_bill <= 2000:
        category = "Low Payment Category"
    elif final_bill <= 5000:
        category = "Moderate Payment Category"
    else:
        category = "High Payment Category"

    return {
        "subtotal": round(subtotal, 2),
        "concession": round(concession, 2),
        "final_bill": round(final_bill, 2),
        "category": category
    }


# Sample patient information
patient = {
    "patient_id": "P101",
    "consultation": 500,
    "diagnostic": 1500,
    "treatment": 3000,
    "eligible": True,
    "concession_rate": 10
}

try:
    bill = generate_bill(patient)

    print("HOSPITAL BILL")
    print("------------------------------")
    print("Patient ID:", patient["patient_id"])
    print("Consultation Charges: Rs.", patient["consultation"])
    print("Diagnostic Charges: Rs.", patient["diagnostic"])
    print("Treatment Charges: Rs.", patient["treatment"])
    print("Total Charges: Rs.", bill["subtotal"])
    print("Concession: Rs.", bill["concession"])
    print("Final Bill: Rs.", bill["final_bill"])
    print("Payment Category:", bill["category"])

except ValueError as error:
    print("Billing Error:", error)
```
