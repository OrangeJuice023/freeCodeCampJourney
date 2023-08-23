// Declare global variables

// Declare the decodedArr as a global variable outside the function
const decodedArr = [];

function rot13(str) {
  // Clear the global decodedArr before each function call
  decodedArr.length = 0

  // Loop through each character in the input string
  for (let i = 0; i < str.length; i++) {
    const charCode = str.charCodeAt(i);
    let decodedCharCode;

    // Check if the character is an uppercase letter (ASCII range 65 to 90)
    if (charCode >= 65 && charCode <= 90) {
      // Apply the ROT13 shift by adding 13 to the character code
      decodedCharCode = ((charCode - 65 + 13) % 26) + 65;
    } else {
      // Non-alphabetic characters remain unchanged
      decodedCharCode = charCode;
    }

    // Push the decoded character to the array
    decodedArr.push(String.fromCharCode(decodedCharCode));
  }

  // Convert the array of decoded characters back to a string and return
  return decodedArr.join('');
}


rot13("SERR PBQR PNZC");
