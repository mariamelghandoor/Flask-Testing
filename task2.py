## Extend Code

# Function 3
def Calculate_Discount(price, discount_percentage):
    if(discount_percentage > 100 or discount_percentage < 0):
        return "Invalid Discount Percentage"
    discount = price * (discount_percentage / 100)
    discounted_price = price - discount
    return discounted_price

def Test_Calculate_Discount():
    try:
        assert Calculate_Discount(100, 10) == 90
        assert Calculate_Discount(100, 30) == 70
        assert Calculate_Discount(100, 101) == "Invalid Discount Percentage"
        assert Calculate_Discount(100, -10) == "Invalid Discount Percentage"
        print("Testing of Calculate_Discount passed")
    except:
        print("Testing of Calculate_Discount failed")



## Testing 
if __name__ == "__main__":
    Test_Calculate_Discount()
    