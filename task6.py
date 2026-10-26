```python
# Railway Fare and Reservation Calculator

CLASS_MULTIPLIERS = {
    "Sleeper": 1.0,
    "AC 3-Tier": 1.5,
    "AC 2-Tier": 2.0,
    "AC First Class": 3.0
}

RESERVATION_FEE = 40
CANCELLATION_RATE = 25  # Percentage


def calculate_distance_fare(distance):
    """Calculate fare using progressive distance slabs."""

    if distance <= 0:
        raise ValueError("Distance must be positive.")

    first_slab = min(distance, 100)
    second_slab = min(max(distance - 100, 0), 200)
    third_slab = max(distance - 300, 0)

    fare = (
        first_slab * 1.50
        + second_slab * 1.20
        + third_slab * 1.00
    )

    return fare


def get_age_concession(age):
    """Return illustrative age-based concession percentage."""

    if age < 0:
        raise ValueError("Age cannot be negative.")

    if age < 60:
        return 0
    elif age < 75:
        return 20
    else:
        return 30


def calculate_passenger_fare(passenger):
    """Calculate fare for one passenger."""

    name = passenger["name"].strip()
    age = passenger["age"]
    distance = passenger["distance"]
    travel_class = passenger["travel_class"]

    if not name:
        raise ValueError("Passenger name is required.")

    if (
        isinstance(age, bool)
        or not isinstance(age, int)
        or age < 0
    ):
        raise ValueError("Age must be a non-negative integer.")

    if (
        isinstance(distance, bool)
        or not isinstance(distance, (int, float))
        or distance <= 0
    ):
        raise ValueError("Distance must be positive.")

    if travel_class not in CLASS_MULTIPLIERS:
        raise ValueError("Invalid travel class.")

    # Calculate distance fare
    base_fare = calculate_distance_fare(distance)

    # Apply travel-class multiplier
    class_fare = (
        base_fare * CLASS_MULTIPLIERS[travel_class]
    )

    # Apply age-based concession
    concession_rate = get_age_concession(age)
    concession = class_fare * concession_rate / 100

    fare_after_concession = class_fare - concession

    # Add reservation fee
    total_fare = fare_after_concession + RESERVATION_FEE

    # Calculate illustrative cancellation refund
    cancellation_penalty = (
        fare_after_concession
        * CANCELLATION_RATE / 100
    )

    refund = total_fare - cancellation_penalty

    return {
        "name
