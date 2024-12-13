## Unit Testing

# Function 1
def Multiply_Numbers(a,b):
    return a * b

def Test_Multiply_Numbers():
    try:
        assert Multiply_Numbers(2,3) == 6
        assert Multiply_Numbers(3,0) == 0
        assert Multiply_Numbers(-1,-2) == 2
        assert Multiply_Numbers(-1,2) == -2
        print("Testing of Multiply_Numbers passed")
    except:
        print("Testing of Multiply_Numbers failed")



# Function 2
def Reverse_list(list):
    return list[::-1]

def Test_Reverse_list():
    try:
        assert Reverse_list([1,2,3]) == [3,2,1]
        assert Reverse_list([1]) == [1]
        assert Reverse_list([]) == []
        print("Testing of Reverse_list passed")
    except:
        print("Testing of Reverse_list failed")


## Testing
if __name__ == "__main__":
    Test_Multiply_Numbers()
    Test_Reverse_list()