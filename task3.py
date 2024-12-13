# Encapsulate in a class
import unittest
# class of functions 
class MathOperations:
    def Is_prime(self, n):
        if n == 1 or n == 0:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    
    def Factorial(self, n):
        if(n < 0):
            return "Invalid Input"
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result


# class of testing
class Test_MathOperations(unittest.TestCase):
    def Test_Is_Prime(self):
        math_operations = MathOperations()
        try:
            self.assertEqual(math_operations.Is_prime(23),True)
            self.assertEqual(math_operations.Is_prime(24),False)
            self.assertEqual(math_operations.Is_prime(1),False)
            self.assertEqual(math_operations.Is_prime(0),False)
            print("Prime Test Passed")
        except:
            print("Prime Test Failed")
    
    def Test_Factorial(self):
        math_operations = MathOperations()
        try:
            self.assertEqual(math_operations.Factorial(5),120)
            self.assertEqual(math_operations.Factorial(0),1)
            self.assertEqual(math_operations.Factorial(-1),"Invalid Input")
            print("Factorial Test Passed")
        except:
            print("Factorial Test Failed")


if __name__ == "__main__":
    Test_MathOperations().Test_Is_Prime()
    Test_MathOperations().Test_Factorial()