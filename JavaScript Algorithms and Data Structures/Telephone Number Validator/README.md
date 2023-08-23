# Telephone Number Validator

📞 A JavaScript Function to Validate US Phone Numbers

Greetings! I present to you a JavaScript function that I created as part of the Telephone Number Validator activity in the freeCodeCamp JavaScript curriculum.

## Function Description

The provided JavaScript function checks whether a given string is a valid US phone number format. It aims to match various formats, including those with or without country codes, hyphens, or parentheses.

## How It Works

1. The regular expressions `regex1` and `regex2` are global variables declared to match the US phone number format.
2. The function `telephoneCheck(str)` takes a string `str` as input.
3. The function first tests `str` against `regex1`. If it matches, it returns `true`.
4. If `regex1` doesn't match, the function tests `str` against `regex2`. If it matches, it returns `true`. Otherwise, it returns `false`.
5. The ternary operator is used to perform the second test only if the first test fails.

Feel free to use the function to validate various US phone numbers with different formats and see how it accurately determines their validity.

Happy coding! 💻🚀
