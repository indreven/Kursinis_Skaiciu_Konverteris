from abc import ABC, abstractmethod

class Converter(ABC):

  @abstractmethod
  def convert_to(self,number):
    pass

class DecimalToRoman(Converter):

  decimal_conversions = [ (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I') ]

  def convert_to(self,number):
    result = ''
    try:
      number = int(number)
      if number > 0:
        for val,sym in self.decimal_conversions:
          while number >= val:
            result += sym
            number -= val
      else:
        print('Number has to be positive')
    except ValueError:
      print("Invalid input. Please provide a valid integer.")
    return result

class RomanToDecimal(Converter):

  roman_conversion = {'I': 1,'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000}

  def convert_to(self, number):
    total = 0
    prev = 0
    for char in reversed(number.upper()):
      value = self.roman_conversion.get(char,0)
      if value >= prev:
        prev = value
        total += value
      else:
        total -= value
        prev = value
    return total

class ConverterApp():

  def __init__(self, converter_type):
    if converter_type == 'DecimalToRoman':
      self._converter = DecimalToRoman()
    elif converter_type == 'RomanToDecimal':
      self._converter = RomanToDecimal()
    else:
      raise ValueError("Invalid mode")

  def convert(self,number):
    return self._converter.convert_to(number)

def main():
  try:
    with open ('input.txt', 'r') as f:
        lines = f.readlines()

        converter_type = lines[0].strip()
        number = lines[1].strip()

        app = ConverterApp(converter_type)
        result = app.convert(number)

        print(f"Conversion result: {result}")

        with  open ('output.txt','w') as f:
          f.write(str(result))

  except FileNotFoundError:
      print('File "input.txt" not found.')
  except IndexError:
      print('File has to have two lines of code: converter type and number')

if __name__ == "__main__":
    main()

