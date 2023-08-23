# Caesar's Cipher

🔐 A JavaScript Function for Caesar's Cipher

Hello! This is a JavaScript function I crafted as part of the Caesar's Cipher activity in the freeCodeCamp JavaScript curriculum.

## Function Description

The provided JavaScript function performs a simple encryption known as Caesar's Cipher, named after Julius Caesar, who is said to have used it for confidential communication. In this encryption, each letter in the plaintext is shifted a certain number of places down or up the alphabet.

## How It Works

1. The `decodedArr` array serves as a global variable to store the decoded characters.
2. The function `rot13(str)` takes a string `str` as input.
3. Before each function call, the global `decodedArr` array is cleared.
4. The function iterates through each character in the input string using a loop.
5. For each character, its character code is retrieved using `charCodeAt()`.
6. If the character is an uppercase letter (ASCII range 65 to 90), the ROT13 shift is applied by adding 13 to the character code, ensuring the value wraps around within the alphabet.
7. Non-alphabetic characters remain unchanged.
8. The decoded character is pushed to the `decodedArr` array.
9. After processing all characters, the array of decoded characters is joined back into a string and returned.

Feel free to test the function with various inputs and observe how the simple Caesar's Cipher encryption works.

Happy coding! 💻🚀
