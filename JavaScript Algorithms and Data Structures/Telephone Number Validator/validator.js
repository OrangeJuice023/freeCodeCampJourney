// Declare variables globally

// Regular expressions that matches the US phone number format
const regex1 = /^(1\s?)?\d{3}([-\s]?)\d{3}\2\d{4}$/;
const regex2 = /^(1\s?)?\(\d{3}\)\s?\d{3}[-\s]?\d{4}$/;

function telephoneCheck(str) {
  
  if (regex1.test(str)) {
    return true;
  } else {
    return regex2.test(str) ? true : false;
  }
}

console.log(telephoneCheck("555-555-5555")); // Output: true
