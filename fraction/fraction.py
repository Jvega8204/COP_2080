class Fraction:
    def __init__(self, numerator=0, denominator=1):
        self._numerator = numerator
        self._denominator = denominator

    # Getters
    @property
    def numerator(self):
        return self._numerator

    @property
    def denominator(self):
        return self._denominator

    # Setters
    @numerator.setter
    def numerator(self, value):
        self._numerator = value

    @denominator.setter
    def denominator(self, value):
        if value == 0:
            print("Incorrect input: denominator cannot be 0")
            self._denominator = 1  # Avoid zero denominator
        else:
            self._denominator = value

    # String representation of the fraction
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
    
    def __mul__(self, other):
        return Fraction(self.numerator * other.numerator,self.denominator * other.denominator)

# Example usage:
f1 = Fraction(2, 3)
print(f1.numerator)  # Access through getter
print(f1.denominator)  # Access through getter

print(f1)  # Uses the __str__ method

f1.numerator = 7  # Setter for numerator
print(f1)

print(f"{f1}")

