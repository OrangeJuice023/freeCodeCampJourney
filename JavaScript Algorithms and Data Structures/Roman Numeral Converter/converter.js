// Declare the array as a global variable
var romanMap = [
    { numeral: 'M', value: 1000 },
    { numeral: 'CM', value: 900 },
    { numeral: 'D', value: 500 },
    { numeral: 'CD', value: 400 },
    { numeral: 'C', value: 100 },
    { numeral: 'XC', value: 90 },
    { numeral: 'L', value: 50 },
    { numeral: 'XL', value: 40 },
    { numeral: 'X', value: 10 },
    { numeral: 'IX', value: 9 },
    { numeral: 'V', value: 5 },
    { numeral: 'IV', value: 4 },
    { numeral: 'I', value: 1 },
  ];

function convertToRoman(num) {
  if (num <= 0 || num >= 4000) {
    throw new Error('Number out of range. Please enter a number between 1 and 3999.');
  }

  let result = '';
  for (const { numeral, value } of romanMap) {
    while (num >= value) {
      result += numeral;
      num -= value;
    }
  }

  return result;
}


convertToRoman(36);
