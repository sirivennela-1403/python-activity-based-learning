```python
# Retail Billing with Multiple Discount Rules

TAX_RATES = {
    "Groceries": 5,
    "Clothing": 12,
    "Electronics": 18,
    "Books": 0
}

MAX_DISCOUNT = 2000

products = [
    {
        "name": "Rice Bag",
        "category": "Groceries",
        "price": 1000,
        "quantity": 2
    },
    {
        "name": "Shirt",
        "category": "Clothing",
        "price": 800,
        "quantity": 2
    },
    {
        "name": "Headphones",
        "category": "Electronics",
        "price": 2000,
        "quantity": 2
    },
    {
        "name": "Notebook",
        "category": "Books",
        "price": 100,
        "quantity": 5
    }
]


def get_discount_rate(subtotal):
    """Return discount percentage based on subtotal."""

    if subtotal >= 10000:
        return 15
    elif subtotal >= 5000:
        return 10
    elif subtotal >= 1000:
        return 5
    else:
        return 0


def generate_invoice(products):
    if not products:
        raise ValueError("Cart cannot be empty.")

    subtotal = 0

    # Validate products and calculate subtotal
    for product in products:
        if not product["name"].strip():
            raise ValueError("Product name is required.")

        if product["category"] not in TAX_RATES:
            raise ValueError(
                f"Unknown category: {product['category']}"
            )

        price = product["price"]
        quantity = product["quantity"]

        if (
            isinstance(price, bool)
            or not isinstance(price, (int, float))
            or price < 0
        ):
            raise ValueError("Price must be non-negative.")

        if (
            isinstance(quantity, bool)
            or not isinstance(quantity, int)
            or quantity <= 0
        ):
            raise ValueError(
                "Quantity must be a positive integer."
            )

        product["amount"] = round(price * quantity, 2)
        subtotal += product["amount"]

    # Calculate threshold discount
    discount_rate = get_discount_rate(subtotal)

    discount = min(
        subtotal * discount_rate / 100,
        MAX_DISCOUNT
    )

    # Allocate discount proportionally
    total_tax = 0

    for product in products:
        share = product["amount"] / subtotal if subtotal else 0

        product["discount"] = round(
            discount * share, 2
        )

        product["taxable_amount"] = round(
            product["amount"] - product["discount"], 2
        )

        tax_rate = TAX_RATES[product["category"]]

        product["tax"] = round(
            product["taxable_amount"] * tax_rate / 100,
            2
        )

        total_tax += product["tax"]

    # Calculate final payable amount
    total_discount = round(
        sum(p["discount"] for p in products), 2
    )

    total_tax = round(total_tax, 2)

    final_amount = round(
        subtotal - total_discount + total_tax, 2
    )

    return {
        "subtotal": round(subtotal, 2),
        "discount_rate": discount_rate,
        "discount": total_discount,
        "tax": total_tax,
        "final_amount": final_amount
    }


try:
    invoice = generate_invoice(products)

    print("=" * 95)
    print("                         RETAIL INVOICE")
    print("=" * 95)

    print(
        f"{'Product':15} {'Category':15} {'Qty':>4} "
        f"{'Amount':>10} {'Discount':>10} "
        f"{'Tax':>10}"
    )

    print("-" * 95)

    for product in products:
        print(
            f"{product['name']:15} "
            f"{product['category']:15} "
            f"{product['quantity']:>4} "
            f"{product['amount']:>10.2f} "
            f"{product['discount']:>10.2f} "
            f"{product['tax']:>10.2f}"
        )

    print("-" * 95)
    print(f"Subtotal          : Rs. {invoice['subtotal']:.2f}")
    print(
        f"Discount Rate     : "
        f"{invoice['discount_rate']}%"
    )
    print(f"Total Discount    : Rs. {invoice['discount']:.2f}")
    print(f"Total Tax         : Rs. {invoice['tax']:.2f}")
    print("=" * 95)
    print(
        f"FINAL PAYABLE AMOUNT: "
        f"Rs. {invoice['final_amount']:.2f}"
    )
    print("=" * 95)

except (ValueError, TypeError, KeyError) as error:
    print("Billing Error:", error)
```
