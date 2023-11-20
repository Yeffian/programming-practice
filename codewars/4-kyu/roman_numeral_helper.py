class RomanNumerals:
    @staticmethod
    def to_roman(val : int) -> str:
            result = ""
            if val >= 1000:
                result += "M"
                result += RomanNumerals.to_roman(val - 1000)
            elif val >= 900:
                result += "CM"
                result += RomanNumerals.to_roman(val - 900)
            elif val >= 500:
                result += "D"
                result += RomanNumerals.to_roman(val - 500)
            elif val >= 400:
                result += "CD"
                result += RomanNumerals.to_roman(val - 400)
            elif val >= 100:
                result += "C"
                result += RomanNumerals.to_roman(val - 100)
            elif val >= 90:
                result += "XC"
                result += RomanNumerals.to_roman(val - 90)
            elif val >= 50:
                result += "L"
                result += RomanNumerals.to_roman(val - 50)
            elif val >= 40:
                result += "XL"
                result += RomanNumerals.to_roman(val - 40)
            elif val >= 10:
                result += "X"
                result += RomanNumerals.to_roman(val - 10)
            elif val >= 9:
                result += "IX"
                result += RomanNumerals.to_roman(val - 9)
            elif val >= 5:
                result += "V"
                result += RomanNumerals.to_roman(val - 5)
            elif val >= 4:
                result += "IV"
                result += RomanNumerals.to_roman(val - 4)
            elif val >= 1:
                result += "I"
                result += RomanNumerals.to_roman(val - 1)
            
            return result


    @staticmethod
    def from_roman(roman_num : str) -> int:
        numeral_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        result = 0
    
        for i in range(len(roman_num)):
            if i > 0 and numeral_map[roman_num[i]] > numeral_map[roman_num[i-1]]:
                result += numeral_map[roman_num[i]] - 2 * numeral_map[roman_num[i-1]]
            else:
                result += numeral_map[roman_num[i]]

        return result