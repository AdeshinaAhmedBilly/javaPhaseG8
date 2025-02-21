def digits_list(number):
    return [int(digit) for digit in str(number)]

number = 2342
print("Digits list:", digits_list(number))