def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.

    Args:
        price (float): The original price.
        discount_percent (float): The discount percentage.

    Returns:
        float: The final price after applying the discount.
    """
    # Check if the discount is 20% or higher
    if discount_percent >= 20:
        # Calculate the discount amount
        discount_amount = (discount_percent / 100) * price
        # Calculate the final price
        final_price = price - discount_amount
        return final_price
    else:
        # Return the original price if the discount is less than 20%
        return price


def main():
    # Prompt the user for input
    original_price = float(input("Enter the original price: $"))
    discount_percent = float(input("Enter the discount percentage (%): "))
    # discount_percent = float(25)

    # Calculate the final price
    final_price = calculate_discount(original_price, discount_percent)

    # Print the result
    if final_price == original_price:
        print(f"No discount applied. The price remains: ${final_price:.2f}")
    else:
        print(f"Discount applied! The final price is: ${final_price:.2f}")


if __name__ == "__main__":
    main()