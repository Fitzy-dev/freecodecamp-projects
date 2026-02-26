# Jordan Fitzgerald
# 2/26/2026
# Functions Usage and Conditionas
def apply_discount(price, discount):
    # Type Checks
    if not isinstance(price, (int, float)):
        return "The price should be a number"
    if not isinstance(discount, (int, float)):
        return "The discount should be a number"
    
    if price <= 0:
        return "The price should be greater than 0"
    if discount < 0 or discount > 100:
        return "The discount should be between 0 and 100"
    # Calculate the final price after pre checks 
    final_price = price - (price * (discount / 100))
    return final_price
    


result_1 = apply_discount(100, 20)
print(result_1)

result_2 = apply_discount(200, 50)
print(result_2)


result_3 = apply_discount(50, 0)
print(result_3)

