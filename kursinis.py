from abc import ABC, abstractmethod


class Converter(ABC):

    @abstractmethod
    def convert_to(self, number):
        pass


class DecimalToRoman(Converter):

    decimal_conversions = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]

    def convert_to(self, number):
        number = int(number)
        if number <= 0:
            raise ValueError("Number must be a positive integer.")
        if number > 3999:
            raise ValueError(
                "Number must be 3999 or less. Roman numerals go up to 3999."
            )

        result = ''
        for val, sym in self.decimal_conversions:
            while number >= val:
                result += sym
                number -= val
        return result


class RomanToDecimal(Converter):

    roman_conversion = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    def is_valid_roman(self, number):
        number = number.upper()

        invalid_repeats = [
            'IIII', 'VV', 'XXXX', 'LL',
            'CCCC', 'DD', 'MMMM'
        ]

        invalid_numbers = [
            'IIV', 'IIX', 'IL', 'IC', 'ID', 'IM',
            'VX', 'VL', 'VC', 'VD', 'VM',
            'XXL', 'XXC', 'XD', 'XM',
            'LC', 'LD', 'LM',
            'CCD', 'CCM', 'CDM',
            'DM',
            'IVX', 'IXC', 'XCM', 'ICM'
        ]

        for pattern in invalid_repeats + invalid_numbers:
            if pattern in number:
                return False
        return True

    def convert_to(self, number):
        number = number.upper()

        if not self.is_valid_roman(number):
            raise ValueError(f"Invalid number: {number}")

        for char in number:
            if char not in self.roman_conversion:
                raise ValueError(f"Invalid symbol: '{char}'")

        total = 0
        prev = 0
        for char in reversed(number):
            value = self.roman_conversion[char]
            if value >= prev:
                total += value
            else:
                total -= value
            prev = value

        if total > 3999:
            raise ValueError(
                "Converted number is too large. "
                "Roman numerals go up to 3999."
            )

        return total


class ConverterApp:

    def __init__(self, converter_type):
        if converter_type == 'DecimalToRoman':
            self._converter = DecimalToRoman()
        elif converter_type == 'RomanToDecimal':
            self._converter = RomanToDecimal()
        else:
            raise ValueError(
                "Invalid converter, choose "
                "(DecimalToRoman) or (RomanToDecimal)"
            )

    def convert(self, number):
        return self._converter.convert_to(number)


def main():
    try:
        with open('input.txt', 'r') as f:
            lines = f.readlines()

        converter_type = lines[0].strip()
        number = lines[1].strip()

        app = ConverterApp(converter_type)
        result = app.convert(number)

        print(f"Conversion result: '{converter_type}': {number} → {result}")

        with open('output.txt', 'w') as f:
            f.write(str(result))

    except ValueError as ve:
        print(ve)
    except FileNotFoundError:
        print('File "input.txt" not found.')
    except IndexError:
        print('File must contain two lines: converter type and number.')


if __name__ == "__main__":
    main()
