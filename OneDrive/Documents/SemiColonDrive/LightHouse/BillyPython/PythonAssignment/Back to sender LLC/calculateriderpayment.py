def calculate_rider_payment(successful_deliveries):
    total_deliveries = 100
    collection_rate = (successful_deliveries / total_deliveries) * 100

    if collection_rate < 50:
        amount_per_parcel = 160
    elif 50 <= collection_rate < 60:
        amount_per_parcel = 200
    elif 60 <= collection_rate < 70:
        amount_per_parcel = 250
    else:  # >= 70%
        amount_per_parcel = 500

    base_pay = 5000
    total_payment = (successful_deliveries * amount_per_parcel) + base_pay

    return total_payment

# Test cases
print(calculate_rider_payment(80))  # Expected: 45000
print(calculate_rider_payment(25))  # Expected: 9000

# Tests for different percentage ranges
print(calculate_rider_payment(49))  # Less than 50%
print(calculate_rider_payment(55))  # 50 - 59%
print(calculate_rider_payment(65))  # 60 - 69%
print(calculate_rider_payment(70))  # >= 70%