class Solution:
    def intToRoman(self, num: int) -> str:
        integer_val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        rom_val = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]
        
        roman_numeral = []
        for i in range(len(integer_val)):
            while num >= integer_val[i]:
                num -= integer_val[i]
                roman_numeral.append(rom_val[i])
        return "".join(roman_numeral)