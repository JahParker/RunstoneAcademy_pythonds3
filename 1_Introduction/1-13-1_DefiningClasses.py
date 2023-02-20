class Fraction:
    def __init__(self, top, bottom) -> None:
        self.numerator = top
        self.denominator = bottom

    def greatest_common_divisor(self, first_number, second_number):
        # This is a version of the Euclidean Algorithm
        # The loop will continue to run until the remainder of the 
        # first number divided by the second number is 0
        # In cases of non-like numbers, the answer is usually 1
        while first_number % second_number != 0:
            first_number, second_number = second_number, first_number % second_number
        return second_number    
    
    # String representation of the class
    def __str__(self) -> str:
        return f"{self.numerator}/{self.denominator}"
    
    def __add__(self, other_fraction):
        new_num = self.numerator * other_fraction.denominator + \
                 self.denominator * other_fraction.numerator
        new_den = self.denominator * other_fraction.denominator
        common = self.greatest_common_divisor(new_num, new_den)

        return Fraction(new_num // common, new_den // common)

    def __mul__(self, other_fraction):
        new_num = self.numerator * other_fraction.numerator
        new_den = self.denominator * other_fraction.denominator
        common = self.greatest_common_divisor(new_num, new_den)

        return Fraction(new_num // common, new_den // common)
    
    def __sub__(self, other_fraction):
        new_num = self.numerator * other_fraction.denominator - \
                  self.denominator * other_fraction.numerator
        new_den = self.denominator * other_fraction.denominator
        common = self.greatest_common_divisor(new_num, new_den)
        
        if new_num == 0:
            return Fraction(0, 0)

        return Fraction(new_num // common, new_den // common)

    def __truediv__(self, other_fraction):
        new_num = self.numerator * other_fraction.denominator
        new_den = self.denominator * other_fraction.numerator
        common = self.greatest_common_divisor(new_num, new_den)

        return Fraction(new_num // common, new_den // common)

    def __lt__(self, other_fraction):
        first_number = self.numerator * other_fraction.denominator
        second_number = other_fraction.numerator * self.denominator

        return first_number < second_number
    
    def __gt__(self, other_fraction):
        first_number = self.numerator * other_fraction.denominator
        second_number = other_fraction.numerator * self.denominator

        return first_number > second_number
    
    def __eq__(self, other_fraction) -> bool:
        first_number = self.numerator * other_fraction.denominator
        second_number = other_fraction.numerator * self.denominator

        return first_number == second_number
    
    def __ne__(self, other_fraction) -> bool:
        first_number = self.numerator * other_fraction.denominator
        second_number = other_fraction.numerator * self.denominator

        return first_number != second_number

    


first_fraction = Fraction(10, 15)
second_fraction = Fraction(2, 3)

print(first_fraction + second_fraction)
print(first_fraction - second_fraction)
print(first_fraction * second_fraction)
print(first_fraction / second_fraction)
print(first_fraction < second_fraction)
print(first_fraction > second_fraction)
print(first_fraction == second_fraction)
print(first_fraction != second_fraction)
