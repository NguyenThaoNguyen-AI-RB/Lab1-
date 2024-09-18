class Integer:
    def __init__(self, value):
        self.value = value
    @classmethod
    def from_float(cls, value):
        if isinstance(value, float):
            return cls(math.floor(value))
        else:
            return "value is not a float"
    @classmethod
    def from_roman(cls, value):
        roman_to_int = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
            'D': 500, 'M': 1000
        }
        def roman_to_integer(s):
            total = 0
            prev_value = 0
            for char in reversed(s):
                if char not in roman_to_int:
                    return "invalid roman numeral"
                value = roman_to_int[char]
                if value < prev_value:
                    total -= value
                else:
                    total += value
                prev_value = value
            return total
        if isinstance(value, str):
            result = roman_to_integer(value.upper())
            return cls(result) if result != "invalid roman numeral" else result
        else:
            return "invalid roman numeral"
    @classmethod
    def from_string(cls, value):
        if isinstance(value, str):
            try:
                return cls(int(value))
            except ValueError:
                return "wrong type"
        else:
            return "wrong type"
    def add(self, integer):
        if isinstance(integer, Integer):
            return self.value + integer.value
        else:
            return "number should be an Integer instance"
first_num = Integer(10)
second_num = Integer.from_roman("IV")
print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))
print(first_num.add(second_num))