# Palindrome Checker

🔍 A JavaScript Function to Check for Palindromes

Hello there! This is a JavaScript function I created as part of the Palindrome Checker activity in the freeCodeCamp JavaScript curriculum.

## Function Description

The provided JavaScript function checks whether a given string is a palindrome or not. A palindrome is a word, phrase, or sequence of characters that reads the same backward as forward, ignoring spaces, punctuation, and capitalization.

## How It Works

1. The function takes a string `str` as input.
2. It cleans the input string by converting it to lowercase and removing non-alphanumeric characters using regular expressions.
3. The cleaned string is then split into an array of characters.
4. The `every` array method is used to compare each character with its corresponding character from the end of the string.
5. If all character pairs are equal, the function returns `true`, indicating that the input string is a palindrome. Otherwise, it returns `false`.

Feel free to test the function with different strings and see how it performs in checking for palindromes.

Happy coding! 💻🚀
