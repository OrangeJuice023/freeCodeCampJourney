# Roman Numeral Converter

🔢 A JavaScript Function to Convert Numbers to Roman Numerals

Greetings! This is a JavaScript function I created for the Roman Numeral Converter activity in the freeCodeCamp JavaScript curriculum.

## Function Description

The provided JavaScript function converts a given number into its corresponding Roman numeral representation. The function is designed to handle numbers between 1 and 3999, providing accurate Roman numeral conversions within that range.

## How It Works

1. The `romanMap` array serves as a global variable containing numeral-value pairs, mapping the basic Roman numerals to their corresponding numerical values.
2. The function `convertToRoman(num)` takes a number `num` as input.
3. It first checks if the input number is within the valid range (1 to 3999) and throws an error if not.
4. The function then iterates through the `romanMap` array using a loop.
5. Inside the loop, the function repeatedly appends the appropriate numeral to the `result` string while subtracting the corresponding value from the input number.
6. The loop continues until the input number becomes zero.
7. The function finally returns the `result` string containing the Roman numeral representation of the input number.

Feel free to use the function to convert various numbers into Roman numerals and explore its accurate conversion mechanism.

Happy coding! 💻🚀
